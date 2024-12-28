---
title: Elasticsearch (二)
keywords:
  - Spring
categories:
  - Spring
tags:
  - Spring
abbrlink: 8b9030ff
date: 2016-11-10 00:00:00
---

查询过滤关键字

### term 过滤

term 主要用于精确匹配哪些值，比如数字，日期，布尔值或 not_analyzed 的字符串 (未经分析的文本数据类型)：

```json
{ "term": { "age":    26           }}
{ "term": { "date":   "2014-09-01" }}
{ "term": { "public": true         }}
{ "term": { "tag":    "full_text"  }}
```

### terms 过滤

terms 跟 term 有点类似，但 terms 允许指定多个匹配条件。 如果某个字段指定了多个值，那么文档需要一起去做匹配：

```json
{
  "terms": {
    "tag": ["search", "full_text", "nosql"]
  }
}
```

### range 过滤 (范围过滤)

range 过滤允许我们按照指定范围查找一批数据：

```json
{
  "range": {
    "age": {
      "gte": 20,
      "lt": 30
    }
  }
}
```

范围操作符包含：  
gt :: 大于  
gte:: 大于等于  
lt :: 小于  
lte:: 小于等于

### exists 和 missing 过滤

exists 和 missing 过滤可以用于查找文档中是否包含指定字段或没有某个字段，类似于 SQL 语句中的 IS_NULL 条件

```json
{
  "exists": {
    "field": "title"
  }
}
```

这两个过滤只是针对已经查出一批数据来，但是想区分出某个字段是否存在的时候使用。

### bool 过滤

bool 过滤可以用来合并多个过滤条件查询结果的布尔逻辑，它包含一下操作符：

must :: 多个查询条件的完全匹配,相当于 and。  
must_not :: 多个查询条件的相反匹配，相当于 not。  
should :: 至少有一个查询条件匹配, 相当于 or。

这些参数可以分别继承一个过滤条件或者一个过滤条件的数组：

```json
{
  "bool": {
    "must": { "term": { "folder": "inbox" } },
    "must_not": { "term": { "tag": "spam" } },
    "should": [{ "term": { "starred": true } }, { "term": { "unread": true } }]
  }
}
```

### bool 查询

bool 查询与 bool 过滤相似，用于合并多个查询子句。不同的是，bool 过滤可以直接给出是否匹配成功， 而 bool 查询要计算每一个查询子句的 `_score` （相关性分值）。

```
must:: 查询指定文档一定要被包含。
must_not:: 查询指定文档一定不要被包含。
should:: 查询指定文档，有则可以为文档相关性加分。
```

以下查询将会找到 title 字段中包含 "how to make millions"，并且 "tag" 字段没有被标为 spam。 如果有标识为 "starred" 或者发布日期为 2014 年之前，那么这些匹配的文档将比同类网站等级高：

```json
{
  "bool": {
    "must": { "match": { "title": "how to make millions" } },
    "must_not": { "match": { "tag": "spam" } },
    "should": [
      { "match": { "tag": "starred" } },
      { "range": { "date": { "gte": "2014-01-01" } } }
    ]
  }
}
```

> 提示： 如果 bool 查询下没有 must 子句，那至少应该有一个 should 子句。但是 如果有 must 子句，那么没有 should 子句也可以进行查询。

### match_all 查询

使用 match_all 可以查询到所有文档，是没有查询条件下的默认语句。

```json
{
  "match_all": {}
}
```

此查询常用于合并过滤条件。 比如说你需要检索所有的邮箱,所有的文档相关性都是相同的，所以得到的 `_score` 为 1

### match 查询

match 查询是一个标准查询，不管你需要全文本查询还是精确查询基本上都要用到它。  
如果你使用 match 查询一个全文本字段，它会在真正查询之前用分析器先分析 match 一下查询字符：

```json
{
  "match": {
    "tweet": "About Search"
  }
}
```

如果用 match 下指定了一个确切值，在遇到数字，日期，布尔值或者 not_analyzed 的字符串时，它将为你搜索你给定的值：

```json
{ "match": { "age":    26           }}
{ "match": { "date":   "2014-09-01" }}
{ "match": { "public": true         }}
{ "match": { "tag":    "full_text"  }}
```

> 提示： 做精确匹配搜索时，你最好用过滤语句，因为过滤语句可以缓存数据。

不像我们在《简单搜索》中介绍的字符查询，match 查询不可以用类似 "+usid:2 +tweet:search" 这样的语句。 它只能就指定某个确切字段某个确切的值进行搜索，而你要做的就是为它指定正确的字段名以避免语法错误。

### multi_match 查询

multi_match 查询允许你做 match 查询的基础上同时搜索多个字段：

```json
{
  "multi_match": {
    "query": "full text search",
    "fields": ["title", "body"]
  }
}
```
