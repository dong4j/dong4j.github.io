import unittest
import json
from pydantic import BaseModel
from utils import clean_md_whitespace
from openaiapi.client import generate as client_openaiapi
from ollama.client import generate as client_ollama

class Document(BaseModel):
    summary: str

def generate(content, type="openaiapi"):
    # 构造 prompt
    prompt = f"""
    你是一个专业的内容总结生成助手。你的任务是为给定的博客内容进行总结以及帮助进行自动生成标签。
    1. 生成的总结内容，长度在 100 到 300 字符之间。
    2. 仅返回一个完整的总结，不要添加额外的信息。
    3. 如果内容中包含 HTML 标签，请忽略这些标签，仅提取文本内容进行分析。
    4. 总结内容不能包含 HTML 标签和 Markdown 相关的语法标签。
    """

    if type == "openaiapi":
        return client_openaiapi(prompt, content, response_format=Document)
    elif type == "ollama":
        prompt = prompt + f"""
        请分析'CONTENT START HERE'和'CONTENT END HERE'之间的文本

        CONTENT START HERE

        {content}

        CONTENT END HERE
        你必须以JSON格式响应，键为'summary'，值是字符串格式的总结内容。
        """
        return client_ollama(prompt)

class TestMathFunctions(unittest.TestCase):
    def test_generate(self):
        blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2024/comfyui-install.md")

        # 调用 generate 函数
        result_ollama = generate(blog_content, type="ollama")
        result_openai = generate(blog_content, type="openaiapi")

        # 验证返回结果是否是 JSON 对象
        for result in [result_ollama, result_openai]:
            # 如果返回的是 JSON 格式字符串，则需要解析
            if isinstance(result, str):
                result = json.loads(result)

            # 打印返回数据
            print("Generated result:", result)

            self.assertIn("summary", result, "Result does not contain 'summary' field.")
            self.assertIsInstance(result["summary"], str, "'summary' is not a string.")

if __name__ == "__main__":
    unittest.main()

