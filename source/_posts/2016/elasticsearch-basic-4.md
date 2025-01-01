---
title: 使用 validate API 验证 Elasticsearch 查询语句的合法性与解释
keywords:
  - Spring
categories:
  - Spring
tags:
  - 查询验证
  - API使用
  - Elasticsearch
  - 字段映射
  - 分析器
abbrlink: f20ffdb
date: 2016-11-20 00:00:00
ai:
  - 本文讲述了如何使用validate API验证ES查询语句是否合法。通过提供GET请求并包含匹配和查询参数，我们能够检查语句的有效性。当查询非法时，API会返回一个JSON响应，其中包含有效性和错误信息。要理解错误原因，可以进一步使用explain参数获取更详细的解释。此外，文章还说明了在不同的索引中对同一个查询词进行拆分查询的原因，这是由于不同索引可能具有不同的映射关系和分析器。
description: 本文讲述了如何使用validate API验证ES查询语句是否合法。通过提供GET请求并包含匹配和查询参数，我们能够检查语句的有效性。当查询非法时，API会返回一个JSON响应，其中包含有效性和错误信息。要理解错误原因，可以进一步使用explain参数获取更详细的解释。此外，文章还说明了在不同的索引中对同一个查询词进行拆分查询的原因，这是由于不同索引可能具有不同的映射关系和分析器。
---

## 验证查询

查询语句可以变得非常复杂，特别是与不同的分析器和字段映射相结合后，就会有些难度。  
validate API 可以验证一条查询语句是否合法。

```json
GET /gb/tweet/_validate/query
{
   "query": {
      "tweet" : {
         "match" : "really powerful"
      }
   }
}
```

以上请求的返回值告诉我们这条语句是非法的：

```json
{
  "valid": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  }
}
```

### 理解错误信息

想知道语句非法的具体错误信息，需要加上 explain 参数：

```json
GET /gb/tweet/_validate/query?explain <1>
{
   "query": {
      "tweet" : {
         "match" : "really powerful"
      }
   }
}
```

> <1> explain 参数可以提供语句错误的更多详情。  
> 很显然，我们把 query 语句的 match 与字段名位置弄反了：

```json
{
  "valid" :     false,
  "_shards" :   { ... },
  "explanations" : [ {
    "index" :   "gb",
    "valid" :   false,
    "error" :   "org.elasticsearch.index.query.QueryParsingException:
                 [gb] No query registered for [tweet]"
  } ]
}
```

### 理解查询语句

如果是合法语句的话，使用 explain 参数可以返回一个带有查询语句的可阅读描述， 可以帮助了解查询语句在 ES 中是如何执行的：

```json
GET /_validate/query?explain
{
   "query": {
      "match" : {
         "tweet" : "really powerful"
      }
   }
}
```

explanation 会为每一个索引返回一段描述，因为每个索引会有不同的映射关系和分析器：

```json
{
  "valid" :         true,
  "_shards" :       { ... },
  "explanations" : [ {
    "index" :       "us",
    "valid" :       true,
    "explanation" : "tweet:really tweet:powerful"
  }, {
    "index" :       "gb",
    "valid" :       true,
    "explanation" : "tweet:really tweet:power"
  } ]
}
```

从返回的 explanation 你会看到 match 是如何为查询字符串 "really powerful" 进行查询的， 首先，它被拆分成两个独立的词分别在 tweet 字段中进行查询。

而且，在索引 us 中这两个词为 "really" 和 "powerful"，在索引 gb 中被拆分成 "really" 和 "power"。 这是因为我们在索引 gb 中使用了 english 分析器。
