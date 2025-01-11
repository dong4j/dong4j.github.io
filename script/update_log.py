import os
import datetime

# 获取脚本的当前路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 日志文件路径
LOG_FILE = os.path.join(SCRIPT_DIR, "../source/update/index.md")

def read_file(file_path):
    """读取文件内容"""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()

def write_file(file_path, content):
    """将内容写入文件"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(content)

def get_git_commits(num_commits=15):
    """获取最新的 Git 提交记录"""
    try:
        import subprocess
        result = subprocess.run(
            ["git", "log", f"-{num_commits}", "--pretty=format:%h %an %ad %s", "--date=format:%Y-%m-%d.%H:%M:%S"],
            stdout=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip().split("\n")
        else:
            print("Error: Failed to get Git commit log.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def format_commit_message(commit):
    """格式化提交记录"""
    # 去除commit字符串中的换行符
    commit = commit.strip()
    parts = commit.split(" ", 3)
    if len(parts) < 4:
        return None
    commit_hash, author, timestamp, message = parts
    
    print(f"{commit_hash} {author} {timestamp} {message}")
    
    # 尝试按空格分割日期和时间
    timestamp_parts = timestamp.split(".")
    if len(timestamp_parts) == 2:
        date_str, time_str = timestamp_parts
    else:
        # 如果没有空格，输出错误信息并返回None
        print(f"Error: Timestamp format is incorrect: {timestamp}")
        return None

    return f"- 【提交时间】{time_str} ({author})  {message}", date_str


def update_log():
    """更新日志文件"""
    # 获取当前日期
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    # 读取文件内容
    content = read_file(LOG_FILE)
    if content is None:
        # 如果文件不存在，则初始化文件
        content = [
            "---\n",
            "title: 站点更新日志\n",
            f"date: {today}\n",
            "aside: false\n",
            "top_img: false\n",
            "comments: false\n",
            "---\n\n",
            "{% timeline 更新日志,orange %}\n\n",
            "<!-- endtimeline -->\n",
        ]

    # 获取 Git 提交记录
    commits = get_git_commits()
    if not commits:
        return

    # 格式化提交记录并按日期分组
    formatted_commits = {}
    for commit in commits:
        commit_entry, commit_date = format_commit_message(commit)
        if not commit_entry:
            print("Error: Failed to format commit message.")
            continue
        if commit_date not in formatted_commits:
            formatted_commits[commit_date] = []
        formatted_commits[commit_date].append(commit_entry)

    # 更新文件内容
    for date, entries in formatted_commits.items():
        today_timeline = f"<!-- timeline {date} -->"
        end_timeline = "<!-- endtimeline -->"
        if today_timeline in "".join(content):
            # 今天的 timeline 已存在
            for i, line in enumerate(content):
                if today_timeline in line:
                    # 在 endtimeline 之前追加记录
                    while i < len(content) and end_timeline not in content[i]:
                        i += 1
                    if i < len(content):
                        for entry in entries:
                            if entry not in content:
                                content.insert(i, f"{entry}\n")
                                i += 1
                        break
        else:
            # 今天的 timeline 不存在，新增
            for i, line in enumerate(content):
                if "{% timeline 更新日志" in line:
                    content.insert(i + 1, f"{today_timeline}\n\n")
                    i += 2
                    for entry in entries:
                        content.insert(i, f"{entry}\n")
                        i += 1
                    content.insert(i, f"\n{end_timeline}\n")
                    break

    # 写回文件
    write_file(LOG_FILE, content)
    print(f"Log file '{LOG_FILE}' updated successfully.")

if __name__ == "__main__":
    update_log()
