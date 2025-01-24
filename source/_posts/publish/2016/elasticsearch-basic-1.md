---
title: 关系型数据库与Elasticsearch对比：索引、类型和文档解析
keywords:
  - Elasticsearch
  - 数据库对比
  - 关系型数据库
  - 文档存储
categories:
  - 新时代码农
tags:
  - Elasticsearch
  - 数据库对比
  - 关系型数据库
  - 文档存储
abbrlink: 24a1ab9d
date: 2016-11-06 00:00:00
ai:
  - 本文对比了关系型数据库和Elasticsearch（ES）的结构和工作方式。关系型数据库以表格形式存储数据，而ES使用倒排索引来加速搜索。文章介绍了如何创建、删除和查询ES中的文档，以及多索引和多类型搜索的用法。还提到了深度分页问题和查询方式的说明。
description: 本文对比了关系型数据库和Elasticsearch（ES）的结构和工作方式。关系型数据库以表格形式存储数据，而ES使用倒排索引来加速搜索。文章介绍了如何创建、删除和查询ES中的文档，以及多索引和多类型搜索的用法。还提到了深度分页问题和查询方式的说明。
---

<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover)

关系型数据库和 ES 对比

```
Relational DB -> Databases -> Tables -> Rows -> Columns
Elasticsearch -> Indexing   -> Types  -> Documents -> Fields
```

Elasticsearch 集群可以包含多个索引 (indices)（数据库），每一个索引可以包含多个类型 (types)（表），每一个类型包含多个文档 (documents)（行），然后每个文档包含多个字段 (Fields)（列）

> # 「索引」含义的区分

> 你可能已经注意到索引 (index) 这个词在 Elasticsearch 中有着不同的含义，所以有必要在此做一下区分:  
> 索引（名词） 如上文所述，一个索引 (index) 就像是传统关系数据库中的数据库，它是相关文档存储的地方，index 的复数是 indices 或 indexes。  
> 索引（动词） 「索引一个文档」表示把一个文档存储到索引（名词）里，以便它可以被检索或者查询。这很像 SQL 中的 INSERT 关键字，差别是，如果文档已经存在，新的文档将覆盖旧的文档。  
> 倒排索引 传统数据库为特定列增加一个索引，例如 B-Tree 索引来加速检索。Elasticsearch 和 Lucene 使用一种叫做倒排索引 (inverted index) 的数据结构来达到相同目的。

创建一个员工信息

```json
PUT /megacorp/employee/1
{
    "first_name" : "John",
    "last_name" :  "Smith",
    "age" :        25,
    "about" :      "I love to go rock climbing",
    "interests": [ "sports", "music" ]
}
```

**删除使用** delete  
**查询** 使用 get  
**查询全部** 在最后加上 `_search`
**自动生成 id** 使用 post

> 自动生成的 ID 有 22 个字符长，URL-safe, Base64-encoded string universally unique identifiers, 或者叫 UUIDs。

**根据关键字查询**  
`GET /megacorp/employee/_search?q=last_name:Smith`

我们在请求中依旧使用 `_search` 关键字，然后将查询语句传递给参数 q=。

Elasticsearch 致力于隐藏分布式系统的复杂性。以下这些操作都是在底层自动完成的：

> 将你的文档分区到不同的容器或者分片 (shards) 中，它们可以存在于一个或多个节点中。  
> 将分片均匀的分配到各个节点，对索引和搜索做负载均衡。  
> 冗余每一个分片，防止硬件故障造成的数据丢失。  
> 将集群中任意一个节点上的请求路由到相应数据所在的节点。  
> 无论是增加节点，还是移除节点，分片都可以做到无缝的扩展和迁移。

## 创建一个新文档

> 当索引一个文档，我们如何确定是完全创建了一个新的还是覆盖了一个已经存在的呢？  
> 请记住 `_index`、`_type`、`_id` 三者唯一确定一个文档。所以要想保证文档是新加入的，最简单的方式是使用 POST 方法让 Elasticsearch 自动生成唯一 `_id`：

```json
POST /website/blog/
{ ... }
```

然而，如果想使用自定义的 `_id`，我们必须告诉 Elasticsearch 应该在 `_index`、`_type`、`_id` 三者都不同时才接受请求。为了做到这点有两种方法，它们其实做的是同一件事情。你可以选择适合自己的方式：1

1. 第一种方法使用 op_type 查询参数：

```json
PUT /website/blog/123?op_type=create
{ ... }
```

2. 或者第二种方法是在 URL 后加 `/_create` 做为端点：

```json
PUT /website/blog/123/_create
{ ... }
```

如果请求成功的创建了一个新文档，Elasticsearch 将返回正常的元数据且响应状态码是 201 Created。

另一方面，如果包含相同的 `_index`、`_type` 和 `_id` 的文档已经存在，Elasticsearch 将返回 409 Conflict 响应状态码，错误信息类似如下：

```json
{
  "error" : "DocumentAlreadyExistsException[[website][4] [blog][123]:
             document already exists]",
  "status" : 409
}
```

## 多索引和多类型搜索

```
/_search

在所有索引的所有类型中搜索
/gb/_search

在索引gb的所有类型中搜索
/gb,us/_search

在索引gb和us的所有类型中搜索
/g*,u*/_search

在以g或u开头的索引的所有类型中搜索
/gb/user/_search

在索引gb的类型user中搜索
/gb,us/user,tweet/_search

在索引gb和us的类型为user和tweet中搜索
/_all/user,tweet/_search
```

## 分页

```json
GET /_search?size=5
GET /_search?size=5&from=5
GET /_search?size=5&from=10
```

深度分页问题

## 查询方式

1. 简单查询  
   直接在 url 后面拼接参数

```json
GET /_all/tweet/_search?q=tweet:elasticsearch
```

"+" 前缀表示语句匹配条件必须被满足。类似的 "-" 前缀表示条件必须不被满足。所有条件如果没有 + 或 - 表示是可选的——匹配越多，相关的文档就越多。
