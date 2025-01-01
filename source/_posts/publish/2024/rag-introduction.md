---
title: 基于 RAG 的企业知识库建设方案
abbrlink: f3b0024e
date: 2024-11-06 22:16:06
tags:
  - LLM
  - 微调
  - 提示调整
  - 自然语言处理
  - 知识库问答系统
categories:
  - AI:人工智能
cover:
ai:
  - 本文探讨了企业如何利用LLM和生成式人工智能构建专注于其特定领域的AI产品。由于大语言模型在处理通用问题方面表现较好，但在垂直专业领域存在知识深度和时效性不足的问题，因此需要不断将自身的知识库输入到大语言模型中进行训练。文章介绍了两种常见的方法实现：微调和提示调整。并详细说明了如何使用LLM作为用户和搜索系统沟通的介质，发挥其强大的自然语言处理能力，对用户请求进行纠错、提取关键点等预处理实现“理解”，并对输出结果在保证正确性的基础上二次加工。最后，文章推荐了Langchain-Chatchat
    + chatglm3-6b作为最终方案。
description: 本文探讨了企业如何利用LLM和生成式人工智能构建专注于其特定领域的AI产品。由于大语言模型在处理通用问题方面表现较好，但在垂直专业领域存在知识深度和时效性不足的问题，因此需要不断将自身的知识库输入到大语言模型中进行训练。文章介绍了两种常见的方法实现：微调和提示调整。并详细说明了如何使用LLM作为用户和搜索系统沟通的介质，发挥其强大的自然语言处理能力，对用户请求进行纠错、提取关键点等预处理实现“理解”，并对输出结果在保证正确性的基础上二次加工。最后，文章推荐了Langchain-Chatchat
  + chatglm3-6b作为最终方案。
keywords:
  - LLM
  - 微调
  - 提示调整
  - 自然语言处理
  - 知识库问答系统
---

![AI-应用.drawio.svg](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/AI-%E5%BA%94%E7%94%A8.drawio.svg)

![dify.drawio.svg](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/dify.drawio.svg)

越来越多的企业和个人希望能够利用 LLM 和生成式人工智能来构建专注于其特定领域的具备 AI 能力的产品。目前，大语言模型在处理通用问题方面表现较好，但由于训练语料和大模型的生成限制，对于垂直专业领域，则会存在知识深度和时效性不足的问题。在信息时代，由于企业的知识库更新频率越来越高，并且企业所拥有的垂直领域知识库（例如文档、图像、音视频等）往往是未公开或不可公开的。因此，对于企业而言，如果想在大语言模型的基础上构建属于特定垂直领域的 AI 产品，就需要不断将自身的知识库输入到大语言模型中进行训练。

目前有两种常见的方法实现：

- 微调（Fine-tuning）：通过提供新的数据集对已有模型的权重进行微调，不断更新输入以调整输出，以达到所需的结果。这适用于数据集规模不大或针对特定类型任务或风格进行训练，但训练成本和价格较高。
- 提示调整（Prompt-tuning）：通过调整输入提示而非修改模型权重，从而实现调整输出的目的。相较于微调，提示调整具有较低的计算成本，需要的资源和训练时间也较少，同时更加灵活。

综上所述，微调的方案投入成本较高，更新频率较低，并不适合所有企业。提示调整的方案是在向量库中构建企业的知识资产，通过 LLM+ 向量库构建垂直领域的深度服务。本质是利用数据库进行提示工程（Prompt Engineering）将企业知识库文档和实时信息通过向量特征提取然后存储到向量数据库，结合 LLM 可以让 Chatbot 的回答更具专业性和时效性，也更适合中小型企业构建企业专属 Chatbot。

在机器学习领域，为了能够处理大量的非结构化的数据，通常会使用人工智能技术提取这些非结构化数据的特征，并将其转化为特征向量，再对这些特征向量进行分析和检索以实现对非结构化数据的处理。将这种能存储、分析和检索特征向量的数据库称之为向量数据库。

## 技术选型

### 需求描述

打造 **特定领域知识 (Domain-specific Knowledge)** **问答** 系统，具体需求有：

- 通过自然语言问答的形式，和用户交互，同时支持中文和英文。
- 理解用户不同形式的问题，找到与之匹配的答案。可以对答案进行二次处理，比如将关联的多个知识点进行去重、汇总等。
- 支持上下文。有些问题可能比较复杂，或者原始知识不能覆盖，需要从历史会话中提取信息。
- 准确。不要出现似是而非或无意义的回答。

---

### 整体方案

使用 LLM 作为用户和搜索系统件沟通的介质，发挥其强大的 [自然语言处理](https://cloud.tencent.com/product/nlp?from_column=20065&from=20065) 能力：对用户请求进行纠错、提取关键点等预处理实现 “理解”；对输出结果在保证正确性的基础上二次加工，比如——概括、分析、推理等。

整个方案设计如下图所示由两部分组成：

![20241229144920_ZXCsfntf.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144920_ZXCsfntf.webp)

说明如下：

1. 使用 OpenAI 的 Embedding 接口将专业领域知识转化为向量，连同原始材料一并保存在 Redis 中。
2. 用户提问的搜索处理：
3. 使用 OpenAI API 对用户的问题进行 Embedding，获得向量。
4. 使用问题向量在 Redis 中搜索，找到与之最匹配的若干记录。将这些记录的原始材料返回。
5. 使用 **OpenAI** 的 Completion API 对这些原始材料进行加工完善，并将最终结果返回。

具体的做法是将知识库的内容通过某些格式保存到数据库中，然后每次提问的时候，先取数据库检索相关的内容，然后将内容和问题按照类似上面的 prompt 提交给 ChatGPT，经过 ChatGPT 来生成高质量的回答。而这个保存了书内容的数据库就是**外挂知识库**。

其中保存到数据库的过程是对原文本进行 Tokenizer（分词） + Embedding（向量化），数据库则称为 Vector Store （向量数据库）

**整个过程如下：**

![20241229144920_SnCXbO1D.webp](https://blog-1258270892.cos.ap-chengdu.myqcloud.com/source/image/20241229144920_SnCXbO1D.webp)

名词解释：

- 分词（Tokenizer）： 将文本拆分成单个单词或词语，结构化为计算机可以处理的结构化形式，，比如 我每天六点下班 可以拆分为 “我”，“每天”，“六点下班”，常见的分词器有 markdown 分词器 [MarkdownTextSplitter](https://www.langchain.com.cn/modules/indexes/text_splitters/examples/markdown)
- 向量化（Embedding）：将文本数据转换为向量的过程。计算机无法直接处理文本，因此需要将文本转换为数学向量形式，以便算法能够理解和处理。文本和数学向量之间互相映射，但数学向量更便于计算机运算。对中文比较友好的向量模型库有 [shibing624/text2vec-base-chinese](https://github.com/shibing624/text2vec)
- 向量数据库（Vector Store）: 存储和管理向量化后的文本数据的数据库，能快速检索相似文本或进行文本相似性比较。 比如 [FAISS](https://github.com/facebookresearch/faiss) 这个库

---

### LLM

[Awesome Chinese LLM](https://github.com/HqWu-HITCS/Awesome-Chinese-LLM)

在上述方案中, 推荐选择具有 OpenAI API 的 LLM, 后期可以无感知的升级底层的 LLM. 常见的开源的 LLM 有以下几种:

#### ChatGLM3

<https://github.com/THUDM/ChatGLM3>

ChatGLM3-6B 是 ChatGLM3 系列中的开源模型，在保留了前两代模型对话流畅、部署门槛低等众多优秀特性的基础上，ChatGLM3-6B 引入了如下特性：更强大的基础模型： ChatGLM3-6B 的基础模型 ChatGLM3-6B-Base 采用了更多样的训练数据、更充分的训练步数和更合理的训练策略；更完整的功能支持： ChatGLM3-6B 采用了全新设计的 Prompt 格式，除正常的多轮对话外。同时原生支持工具调用（Function Call）、代码执行（Code Interpreter）和 Agent 任务等复杂场景；更全面的开源序列： 除了对话模型 ChatGLM3-6B 外，还开源了基础模型 ChatGLM3-6B-Base、长文本对话模型 ChatGLM3-6B-32K。以上所有权重对学术研究完全开放，在填写问卷进行登记后亦允许免费商业使用。

#### LLaMA2

<https://github.com/michael-wzhu/Chinese-LlaMA2>

该项目基于可商用的 LLaMA-2 进行二次开发决定在次开展 Llama 2 的中文汉化工作，包括 Chinese-LlaMA2: 对 Llama 2 进行中文预训练；第一步：先在 42G 中文预料上进行训练；后续将会加大训练规模；Chinese-LlaMA2-chat: 对 Chinese-LlaMA2 进行指令微调和多轮对话微调，以适应各种应用场景和多轮对话交互。同时我们也考虑更为快速的中文适配方案：Chinese-LlaMA2-sft-v0: 采用现有的开源中文指令微调或者是对话数据，对 LlaMA-2 进行直接微调 (将于近期开源)。

#### Baichuan

<https://github.com/baichuan-inc/Baichuan2>

由百川智能开发的一个开源可商用的大规模预训练语言模型。基于 Transformer 结构，在大约 1.2 万亿 tokens 上训练的 70 亿参数模型，支持中英双语，上下文窗口长度为 4096。在标准的中文和英文权威 benchmark（C-EVAL/MMLU）上均取得同尺寸最好的效果。

#### Qwen

<https://github.com/QwenLM/Qwen>

通义千问 是阿里云研发的通义千问大模型系列模型，包括参数规模为 18 亿（1.8B）、70 亿（7B）、140 亿（14B）和 720 亿（72B）。各个规模的模型包括基础模型 Qwen，即 Qwen-1.8B、Qwen-7B、Qwen-14B、Qwen-72B，以及对话模型 Qwen-Chat，即 Qwen-1.8B-Chat、Qwen-7B-Chat、Qwen-14B-Chat 和 Qwen-72B-Chat。数据集包括文本和代码等多种数据类型，覆盖通用领域和专业领域，能支持 8K 的上下文长度，针对插件调用相关的对齐数据做了特定优化，当前模型能有效调用插件以及升级为 Agent。

#### Mixtral

<https://github.com/HIT-SCIR/Chinese-Mixtral-8x7B>

该项目基于 Mixtral-8x7B 稀疏混合专家模型进行了中文扩词表增量预训练，开源了 Chinese-Mixtral-8x7B 扩词表模型以及训练代码。该模型的的中文编解码效率较原模型显著提高。同时通过在大规模开源语料上进行的增量预训练，该模型具备了强大的中文生成和理解能力

---

### 向量模型

向量模型可以将任意文本映射为低维稠密向量，以用于检索、分类、聚类或语义匹配等任务，并可支持为大模型调用外部知识。

简单而言就相当于一个“桥梁” —— 翻译：把图片，文字，视频以及音频全部转换为数字，并且包含了数据的信息，使得大模型都能”懂“，能利用这些数字去做训练和推理.

embedding 模型的应用主要包含以下几点:

- embedding 模型可以将各种数据（语言、图片等）转化为向量，并使用向量之间的距离来衡量数据的相关性。
- 在大模型时代，这种技术有助于解决大模型在回答问题时可能出现的问题，可以帮助大模型获取最新的知识。
- OpenAI、Google、Meta 等大厂也都推出了自己的语义向量模型和 API 服务，催生了大量的应用和工具，如 LangChain、Pinecone 等

各模型对应的地址如下:

text2vec-base-chinese: [https://huggingface.co/shibing624/text2vec-base-chinese](https://link.zhihu.com/?target=https%3A//huggingface.co/shibing624/text2vec-base-chinese)

text2vec-bge-large-chinese: [https://huggingface.co/shibing624/text2vec-bge-large-chinese](https://link.zhihu.com/?target=https%3A//huggingface.co/shibing624/text2vec-bge-large-chinese)

M3E: <https://github.com/wangyuxinwhy/uniem>

BGE: <https://github.com/FlagOpen/FlagEmbedding/blob/master/README_zh.md>

OpenAi: [https://platform.openai.com/docs/api-reference/embeddings](https://link.zhihu.com/?target=https%3A//platform.openai.com/docs/api-reference/embeddings)

千帆大模型: [https://cloud.baidu.com/doc/WEN](https://link.zhihu.com/?target=https%3A//cloud.baidu.com/doc/WENXINWORKSHOP/s/alj562vvu)

---

### 向量数据库

因为喂给 Transformer 的知识首先需要做 embedding，所以用于存储 embedding 之后数据的数据库即可称为向量数据库。

因为向量数据库是基于 embedding 之后的向量的存储与检索。所以首先需要提供存储能力，其次更重要的是检索。 即如何根据一个 query 快速找到相关的 embedding 内容。 关于检索，主要是计算两个向量之间的相似度。

[向量数据库｜一文全面了解向量数据库的基本概念、原理、算法、选型](https://cloud.tencent.com/developer/article/2312534)

[主流向量数据库一览](https://zhuanlan.zhihu.com/p/628148081)

#### Weaviate

Weaviate 是一个开源矢量数据库，它同时存储对象和矢量，允许将矢量搜索与结构化过滤与云原生数据库的容错和可扩展性相结合，所有这些都可以通过 GraphQL、REST 和各种语言客户端访问。

#### Milvus

<https://www.milvus-io.com/overview>

#### Pinecone

<https://www.pinecone-io.com/>

#### pgvector

<https://github.com/pgvector/pgvector>

pgvector 是 PostgreSQL 的一个**向量搜索扩展**,它可以在 PostgreSQL 数据库中进行高效的向量相似度搜索。这种架构能够实现**功能强大且智能**的知识库问答服务,并且具有较高的性能、可靠性和可扩展性,是构建知识库型 AI 系统的一个非常好的选择。

---

### 方案选择

目前已经有许多开源的方案，也有许多商业化的方案，基本上可以分为：

1. ChatGPT + Fine-tune： 微调出一个自己的模型，从一些大佬的反馈来看，这种方式成本高，需要花费很多精力去训练，效果不一定能够很好。可以看看 [如何使用 OpenAI fine-tuning(微调)训练属于自己的专有模型？ - 知乎](https://www.zhihu.com/question/591066880) 和 [大模型外挂(向量)知识库 - 知乎](https://zhuanlan.zhihu.com/p/633671394)
2. ChatGPT + 外挂知识库: 这个有两个方案，第一个就是官方提供的插件 [chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) 来处理文档向量，缺点就是只能在 ChatGPT 源站点使用，并且要有插件开发者权限。另一个是利用 LangChain 处理生成向量库，然后调用 ChatGPT openapi ， 带上检索出来的相关数据和问题去使用。
3. 开源 LLM + 微调: 就是利用开源的 LLM 微调训练目标的知识库，比如 [ChatGLM3](https://github.com/THUDM/ChatGLM3)，当然训练成本也是在的，但可以做到数据不泄露，前面 2 种始终需要通过 ChatGPT，难免出现一些数据泄露。
4. LangChain + 开源 LLM: 如果不想自己训练，又想保证数据安全，那么结合 2，3 点的方案则是安全可靠的，用 LangChain 对文档进行向量化，然后检索内容，在调用 LLM 对得到的内容进行总结输出。
5. 成熟的开源项目: 主要有 [FastGPT](https://fastgpt.run/) 和 [Dify](https://dify.ai/zh)
6. 使用 [TianliGPT](https://docs_s.tianli0.top/) 作为技术文档的摘要.

上面几种方案，2，4 都是比较简单的方案，区别就是模型的问题和数据是否私有化，这里选择方案 4，不依赖 Openai，可以少处理点坑。最终选择的方案就是 [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) + [chatglm3-6b](https://huggingface.co/THUDM/chatglm3-6b)
