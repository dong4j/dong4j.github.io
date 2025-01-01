from openai import OpenAI

def generate(prompt, content, usemodel="glm-4-9b-chat-1m", response_format=None):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    completion = client.beta.chat.completions.parse(
        model=usemodel,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ],
        temperature=0.7,  # 根据需要调整这个参数
        response_format=response_format,  # 动态传入的格式
    )
    return completion.choices[0].message.content