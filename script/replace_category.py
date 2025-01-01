import os
import sys
import time
import json
import threading
import queue
from utils import log, get_process_md_files, split_md, dump_md_yaml, clean_md_whitespace, get_md_category
from generate_category import generate as generate_category_from_ai

# 配置路径
PROCESSED_FILE = "./processed_category_files.txt"  # 已处理的文件记录

# 全局队列
task_queue = queue.Queue()
result_queue = queue.Queue()

def fetch_category_from_ai(md_file, auto_replace111):
    """
    调用 ai 接口生成分类。
    这是占位函数，具体逻辑请实现后替换。
    """
    content = clean_md_whitespace(md_file)
    # print(blog_content)
    category = generate_category_from_ai(content, auto_replace=auto_replace111)
    if category:
        return json.loads(category)
    return None

def replace_md_category(md_file, original_categorie, new_category):
    # 调用函数并获取 body 和 data
    result = split_md(md_file)
    if not result:
        return
    
    data = result['data']
    body = result['body']

    # 替换 categories
    data['categories'] = [new_category]
    dump_md_yaml(md_file, data, body)  # 保存更新后的 YAML 和 body

    log(f"修改分类: {md_file}")
    log(f"{original_categorie} -> {new_category}")

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

def ai_worker(auto_replace):
    """
    负责调用 ai 的线程。
    """
    while True:
        md_file = task_queue.get()
        if md_file is None:  # 检查是否结束
            break
        data = fetch_category_from_ai(md_file, auto_replace)
        result_queue.put((md_file, data))
        task_queue.task_done()

def interactive_worker(auto_replace):
    """
    负责交互式处理的线程。
    """
    processed_files = load_processed_files()

    while True:
        md_file, data = result_queue.get()
        
        if data is None:  # 标识当前任务还未完成，阻塞等待
            log(f"正在等待为 {md_file} 生成分类...")
            result_queue.put((md_file, None))  # 重新将任务放回队列以等待生成完成
            time.sleep(1)  # 等待片刻再检查
            continue
        
        if not data:  # 如果明确返回空列表，说明分类生成失败
            log(f"未生成分类，跳过 {md_file}")
            continue
        
        original_category = get_md_category(md_file)

        if auto_replace:
            # 提取分类列表
            new_category = data.get("recommend", '')
            replace_md_category(md_file, original_category, new_category)
        else:
            # 提取分类列表
            options = data.get("options", [])
            # 处理分类逻辑
            print(f"\n为文件 {md_file} 生成的分类如下：")
            for i, option in enumerate(options):
                print(f"{i + 1}: {option}")

            choice = input("请选择分类编号: ").strip()
            if choice.isdigit():
                choice = int(choice)
                if choice > 0 and choice <= len(options):
                    new_category = options[choice - 1]
                    replace_md_category(md_file, original_category, new_category)
                else:
                    log(f"未替换 {md_file} 的分类。")

        save_processed_file(md_file)
        processed_files.add(md_file)
        result_queue.task_done()
       
def main():
    # True 使用 AI 自动替换, False 使用交互式替换
    auto_replace = True

    dicts = get_process_md_files(sys.argv[1:])
    # 确保发布目录存在
    os.makedirs(dicts.get('publish_dir'), exist_ok=True)

    md_files_to_process = dicts.get('files')

    # 加载已处理文件
    processed_files = load_processed_files()

    # 获取所有 Markdown 文件
    md_files_to_process = [f for f in md_files_to_process if f not in processed_files]

    # 检查是否有未处理的文件
    if not md_files_to_process:
        log("没有需要处理的 Markdown 文件。")
        return

    # 启动 Ollama 调用线程
    threading.Thread(target=ai_worker, args=(auto_replace,), daemon=True).start()

    # 将任务添加到队列
    for md_file in md_files_to_process:
        task_queue.put(md_file)

    # 启动交互线程
    threading.Thread(target=interactive_worker, args=(auto_replace,), daemon=True).start()

    # 等待任务完成
    task_queue.join()
    result_queue.join()
    log("==================category 处理完成==================")

if __name__ == "__main__":
    main()