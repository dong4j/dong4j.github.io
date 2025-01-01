import os
import sys
import time
import json
import threading
import queue
from utils import log, get_all_md_files, find_md_file, split_md, dump_md_yaml, clean_md_whitespace, get_md_category
from generate_category import generate as generate_category_from_ai

# 配置路径
PROCESSED_FILE = "./processed_category_files.txt"  # 已处理的文件记录

# 全局队列
task_queue = queue.Queue()
result_queue = queue.Queue()

def fetch_category_from_ollama(md_file):
    """
    调用 Ollama 接口生成分类。
    这是占位函数，具体逻辑请实现后替换。
    """

    content = clean_md_whitespace(md_file)
    # print(blog_content)
    category = generate_category_from_ai(content, usemodel="glm-4-9b-chat-1m")
    if category:
        results = json.loads(category)
        # print(json.dumps(results, indent=2,ensure_ascii=False))
        return results
    return None

def replace_md_category(md_file, original_categorie, new_category):
    # 调用函数并获取 body 和 data
    result = split_md(md_file)
    if not result:
        return
    
    data = result['data']
    body = result['body']

    # 检查 category
    categories = data.get('categories')
    
    # 替换 categories
    data['categories'] = [new_category]
    dump_md_yaml(md_file, data, body)  # 保存更新后的 YAML 和 body

    log(f"{original_categorie} -> {categories}")

def load_processed_files():
    """
    加载已处理文件的列表。
    """
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f.readlines())
    return set()

def save_processed_file(md_file):
    """
    保存已处理的文件。
    """
    with open(PROCESSED_FILE, 'a', encoding='utf-8') as f:
        f.write(md_file + "\n")

def ollama_worker():
    """
    负责调用 Ollama 的线程。
    """
    while True:
        md_file = task_queue.get()
        if md_file is None:  # 检查是否结束
            break
        category = fetch_category_from_ollama(md_file)
        result_queue.put((md_file, category))
        task_queue.task_done()

def interactive_worker():
    """
    负责交互式处理的线程。
    """
    processed_files = load_processed_files()

    while True:
        md_file, category = result_queue.get()
        
        if category is None:  # 标识当前任务还未完成，阻塞等待
            log(f"正在等待为 {md_file} 生成分类...")
            result_queue.put((md_file, None))  # 重新将任务放回队列以等待生成完成
            time.sleep(1)  # 等待片刻再检查
            continue
        
        if not category:  # 如果明确返回空列表，说明分类生成失败
            log(f"未生成分类，跳过 {md_file}")
            continue
        
        # 提取分类列表
        new_category = category.get("category", '')

        # 处理分类逻辑
        print(f"\n为文件 {md_file} 生成的分类如下：")
        print(f"{1}: {new_category}")
            
        
        original_category = get_md_category(md_file)
        print(f"0: 不替换(原分类: {original_category})")
        print(f"m: 手动输入新分类")

        choice = input("请选择分类编号: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                replace_md_category(md_file, original_category, new_category)
            else:
                log(f"未替换 {md_file} 的分类。")
        elif choice == 'm':
            new_category = input("请输入新的分类: ").strip()
            if new_category:  
                replace_md_category(md_file, original_category, new_category)
            else:
                log(f"未输入新分类，未替换 {md_file} 的分类。")
        else:
            log(f"无效输入，未替换 {md_file} 的分类。")

        save_processed_file(md_file)
        processed_files.add(md_file)
        result_queue.task_done()

def main():
    args = sys.argv[1:]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, '..', 'source/_posts')
    # 构建发布目录路径，确保它在source/_posts下
    publish_dir = os.path.join(base_dir, 'publish')
    # 确保发布目录存在
    os.makedirs(publish_dir, exist_ok=True)
    log(f"博客文章的基准目录：{base_dir}")

    # 初始化要处理的Markdown文件列表
    md_files_to_process = []

    if not args:
        # 处理所有Markdown文件
        md_files_to_process = get_all_md_files(base_dir, exclude_dir='publish')
    elif len(args) == 1 and args[0].isdigit():
        # 处理指定年份的Markdown文件
        year_dir = os.path.join(base_dir, args[0])
        if os.path.isdir(year_dir):
            md_files_to_process = get_all_md_files(year_dir, exclude_dir='publish')
        else:
            log(f"年份目录 {args[0]} 不存在。")
            return
    elif len(args) == 1 and args[0].endswith('.md'):
        # 处理指定的Markdown文件
        md_filename = args[0]
        md_file = find_md_file(base_dir, md_filename, exclude_dir='publish')
        if md_file:
            md_files_to_process.append(md_file)
        else:
            log(f"未找到Markdown文件 {md_filename}。")
            return
    else:
        log("参数数量错误。")
        return


    # 加载已处理文件
    processed_files = load_processed_files()

    # 获取所有 Markdown 文件
    md_files_to_process = [f for f in md_files_to_process if f not in processed_files]

    # 检查是否有未处理的文件
    if not md_files_to_process:
        log("没有需要处理的 Markdown 文件。")
        return

    # 启动 Ollama 调用线程
    threading.Thread(target=ollama_worker, daemon=True).start()

    # 将任务添加到队列
    for md_file in md_files_to_process:
        task_queue.put(md_file)

    # 启动交互线程
    threading.Thread(target=interactive_worker, daemon=True).start()

    # 等待任务完成
    task_queue.join()
    result_queue.join()
    log("所有文件处理完成！")

if __name__ == "__main__":
    main()