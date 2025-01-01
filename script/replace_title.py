import os
import sys
import time
import json
import threading
import queue
from utils import log, get_process_md_files, split_md, dump_md_yaml, clean_md_whitespace, get_md_title, save_processed_file, load_processed_files
from generate_title import generate as generate_titles_from_ai

# 配置路径
PROCESSED_FILE = "./processed_title_files.txt"  # 已处理的文件记录

# 全局队列
task_queue = queue.Queue()
result_queue = queue.Queue()

def fetch_titles_from_ai(md_file):
    """
    调用 ai 接口生成标题。
    这是占位函数，具体逻辑请实现后替换。
    """

    content = clean_md_whitespace(md_file)
    titles = generate_titles_from_ai(content)
    if titles:
        return json.loads(titles)
    return None

def replace_md_title(md_file, original_title, new_title):
    # 调用函数并获取 body 和 data
    result = split_md(md_file)
    if not result:
        return
    
    data = result['data']
    body = result['body']

    # 替换 title
    data['title'] = new_title
    dump_md_yaml(md_file, data, body)  # 保存更新后的 YAML 和 body

    log(f"{original_title} -> {new_title}")

def ai_worker():
    """
    负责调用 ai 的线程。
    """
    while True:
        md_file = task_queue.get()
        if md_file is None:  # 检查是否结束
            break
        titles = fetch_titles_from_ai(md_file)
        result_queue.put((md_file, titles))
        task_queue.task_done()

def interactive_worker():
    """
    负责交互式处理的线程。
    """
    processed_files = load_processed_files(PROCESSED_FILE)

    while True:
        md_file, titles = result_queue.get()
        
        if titles is None:  # 标识当前任务还未完成，阻塞等待
            log(f"正在等待为 {md_file} 生成标题...")
            result_queue.put((md_file, None))  # 重新将任务放回队列以等待生成完成
            time.sleep(1)  # 等待片刻再检查
            continue
        
        if not titles:  # 如果明确返回空列表，说明标题生成失败
            log(f"未生成标题，跳过 {md_file}")
            continue
        
        # 提取标题列表
        title_list = titles.get("title", [])

        # 处理标题逻辑
        print(f"\n为文件 {md_file} 生成的标题如下：")
        for i, title in enumerate(title_list):
            print(f"{i + 1}: {title}")
        
        original_title = get_md_title(md_file)
        print(f"0: 不替换(原标题: {original_title})")
        print(f"m: 手动输入新标题")

        choice = input("请选择标题编号: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(title_list):
                new_title = title_list[choice - 1]
                replace_md_title(md_file, original_title, new_title)
            else:
                log(f"未替换 {md_file} 的标题。")
        elif choice == 'm':
            new_title = input("请输入新的标题: ").strip()
            if new_title:  
                replace_md_title(md_file, original_title, new_title)
            else:
                log(f"未输入新标题，未替换 {md_file} 的标题。")
        else:
            log(f"无效输入，未替换 {md_file} 的标题。")

        save_processed_file(md_file, PROCESSED_FILE)
        processed_files.add(md_file)
        result_queue.task_done()

def main():
    dicts = get_process_md_files(sys.argv[1:])

    # 确保发布目录存在
    os.makedirs(dicts.get('publish_dir'), exist_ok=True)

    md_files_to_process = dicts.get('files')

    # 加载已处理文件
    processed_files = load_processed_files(PROCESSED_FILE)

    # 获取所有 Markdown 文件
    md_files_to_process = [f for f in md_files_to_process if f not in processed_files]

    # 检查是否有未处理的文件
    if not md_files_to_process:
        log("没有需要处理的 Markdown 文件。")
        return

    # 启动 ai 线程
    threading.Thread(target=ai_worker, daemon=True).start()

    # 将任务添加到队列
    for md_file in md_files_to_process:
        task_queue.put(md_file)

    # 启动交互线程
    threading.Thread(target=interactive_worker, daemon=True).start()

    # 等待任务完成
    task_queue.join()
    result_queue.join()
    log("==================title 处理完成==================")

if __name__ == "__main__":
    main()