import requests

def generate(prompt, model="qwen2"):
    # 设置 Ollama API 的 URL
    url = f"http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "format": "json",
        "stream": False
    }
    
    # 发送 POST 请求到 Ollama API
    try:
        response = requests.post(url, json=data, stream=False)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()

        # 提取生成的摘要
        if "response" in data:
            return data["response"]
        else:
            print("没有从响应中获取到摘要内容！")
            return None
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None