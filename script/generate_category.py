from pydantic import BaseModel
from openaiapi.client import generate as client_openaiapi
from ollama.client import generate as client_ollama
import unittest
import json
from utils import clean_md_whitespace

class Document(BaseModel):
    recommend: str
    options: list[str]

def generate(content, type="openaiapi", auto_replace=True):
    categories ={
        "options": [
            "新时代码农",
            "HomeLab:中年男人的快乐源泉",
            "AI:人工智能",
            "生活:生下来活下去",
            "转载内容",
            "经验分享",
            "我的项目",
            "闲聊杂谈",
            "软件推荐",
            "好物推荐",
            "翻译内容"
        ]
    }
    if not auto_replace:
        return json.dumps(categories)

    # 构造 prompt
    prompt = f"""
    请根据我提供给你的博客内容的核心主题为其选择一个最合适的文章分类。
    附加说明：
    1. 生成的分类必须是我给定的以下几个选项之一:
        {categories['options']}
    2. 如果涉及到编程与开发相关的关键字, 比如 Java, Spring, Redis, Rabbitmq, SQL, MySQL, JVM等, 全部划分到 '新时代码农' 这个分类。
    3. 你必须以JSON格式响应，键为'recommend'，值是字符串格式的分类名称, 键为'options'，值是我给定的分类列表。
    """

    if type == "openaiapi":
        return client_openaiapi(prompt, content, response_format=Document)
    elif type == "ollama":
        prompt = prompt + f"""
        请分析'CONTENT START HERE'和'CONTENT END HERE'之间的文本

        CONTENT START HERE

        {content}

        CONTENT END HERE
        """
        return client_ollama(prompt)

class TestMathFunctions(unittest.TestCase):
    def test_generate1(self):
        blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2024/comfyui-install.md")
    
        # 调用 generate 函数
        # result_ollama = generate(blog_content, type="ollama")
        result_openai = generate(blog_content, type="openaiapi")

        # 验证返回结果是否是 JSON 对象
        for result in [result_openai]:
            # 如果返回的是 JSON 格式字符串，则需要解析
            if isinstance(result, str):
                result = json.loads(result)

            # 打印返回数据
            print("Generated result:", result)

            self.assertIn("recommend", result, "Result does not contain 'recommend' field.")
            self.assertIn("options", result, "Result does not contain 'options' field.")
            self.assertIsInstance(result["recommend"], str, "'recommend' is not a string.")
            self.assertIsInstance(result["options"], list, "'options' is not a list.")

    def test_generate2(self):
        blog_content = clean_md_whitespace("/Users/dong4j/Developer/3.Knowledge/site/hexo/source/_posts/2024/comfyui-install.md")

        # 调用 generate 函数
        result_ollama = generate(blog_content, type="ollama", auto_replace=False)
        result_openai = generate(blog_content, type="openaiapi", auto_replace=False)

        # 验证返回结果是否是 JSON 对象
        for result in [result_ollama, result_openai]:
            # 如果返回的是 JSON 格式字符串，则需要解析
            if isinstance(result, str):
                result = json.loads(result)

            # 打印返回数据
            print("Generated result:", result)

            self.assertIn("options", result, "Result does not contain 'options' field.")
            self.assertIsInstance(result["options"], list, "'options' is not a list.")

if __name__ == "__main__":
    unittest.main()