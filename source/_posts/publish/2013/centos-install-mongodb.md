---
title: CentOS7 安装 MongoDB 3.0 服务器
keywords:
  - Shell
categories:
  - Shell
tags:
  - 数据库
  - MongoDB
  - NoSQL
  - 教程
  - 操作指南
abbrlink: 53cebd27
date: 2013-02-16 00:00:00
ai:
  - MongoDB是一个面向文档的NoSQL数据库管理系统，3.0版本操作简便且性能高效。它不支持复杂的join查询，主要关注数据快速访问和高效率处理。与互联网业务场景契合，MongoDB提供灵活的数据模型，并在扩展性方面表现良好。学习了如何安装和配置MongoDB，包括设置不同的端口、绑定特定IP地址等。同时，也了解了MongoDB的可视化工具Robo
    3T的应用，这有助于更直观地管理和操作数据库。在总结中提到，在未来会继续研究MongoDB的功能和高级用法。
description: MongoDB是一个面向文档的NoSQL数据库管理系统，3.0版本操作简便且性能高效。它不支持复杂的join查询，主要关注数据快速访问和高效率处理。与互联网业务场景契合，MongoDB提供灵活的数据模型，并在扩展性方面表现良好。学习了如何安装和配置MongoDB，包括设置不同的端口、绑定特定IP地址等。同时，也了解了MongoDB的可视化工具Robo
  3T的应用，这有助于更直观地管理和操作数据库。在总结中提到，在未来会继续研究MongoDB的功能和高级用法。
---

### 1. 下载 & 安装

MongoDB 3.0 正式版本发布! 这标志着 MongoDB 数据库进入了一个全新的发展阶段，提供强大、灵活而且易于管理的数据库管理系统。MongoDB 宣称，3.0 新版本不只提升 7 到 10 倍的写入效率以及增加 80% 的数据压缩率，还能减少 95% 的运维成本。 
　　 MongoDB 3.0 主要新特性包括： 
　　· 可插入式的存储引擎 API 
　　· 支持 WiredTiger 存储引擎  
　　·MMAPv1 提升  
　　· 复制集全面提升  
　　· 集群方面的改进  
　　· 提升了安全性  
　　· 工具的提升  
WiredTiger 存储引擎是一项难以置信的技术实现，提供无门闩、非堵塞算法来利用先进的硬件平台 (如大容量芯片缓存和线程化架构) 来提升性能。通过 WiredTiger，MongoDB 3.0 实现了文档级别的并发控制，因此大幅提升了大并发下的写负载。

MongoDB 提供了 centos yum 安装方式。

vi /etc/yum.repos.d/mongodb-org-3.0.repo

```shell
[mongodb-org-3.0]
name=MongoDB Repository
baseurl=http://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.0/x86_64/
gpgcheck=0
enabled=1
```

安装 mongodb

```shell
yum install -y mongodb-org
```

安装了所有相关服务。

```shell
......
Running transaction
  Installing : mongodb-org-shell-3.0.2-1.el7.x86_64      1/5
  Installing : mongodb-org-tools-3.0.2-1.el7.x86_64      2/5
  Installing : mongodb-org-mongos-3.0.2-1.el7.x86_64     3/5
  Installing : mongodb-org-server-3.0.2-1.el7.x86_64     4/5
  Installing : mongodb-org-3.0.2-1.el7.x86_64            5/5
  Verifying  : mongodb-org-3.0.2-1.el7.x86_64           1/5
  Verifying  : mongodb-org-server-3.0.2-1.el7.x86_64    2/5
  Verifying  : mongodb-org-mongos-3.0.2-1.el7.x86_64    3/5
  Verifying  : mongodb-org-tools-3.0.2-1.el7.x86_64     4/5
  Verifying  : mongodb-org-shell-3.0.2-1.el7.x86_64     5/5
```

配置文件在：/etc/mongod.conf  数据文件在：/var/lib/mongo  日志文件在：/var/log/mongodb  mongodb 服务使用

```shell
#启动
service mongod start
#停止
service mongod stop
#重启
service mongod restart
#增加开机启动
chkconfig mongod on
```

### 2. MongoDB CRUD

连接到 MongoDB，很简单，执行 mongo 就可以了。

```shell
# mongo
MongoDB shell version: 3.0.2
connecting to: test
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        http://docs.mongodb.org/
Questions? Try the support group
        http://groups.google.com/group/mongodb-user
Server has startup warnings:
I STORAGE  [initandlisten]
I STORAGE  [initandlisten] ** WARNING: Readahead for /var/lib/mongo is set to 4096KB
I STORAGE  [initandlisten] **          We suggest setting it to 256KB (512 sectors) or less
I STORAGE  [initandlisten] **          http://dochub.mongodb.org/core/readahead
I CONTROL  [initandlisten]
I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/enabled is 'always'.
I CONTROL  [initandlisten] **        We suggest setting it to 'never'
I CONTROL  [initandlisten]
I CONTROL  [initandlisten] ** WARNING: /sys/kernel/mm/transparent_hugepage/defrag is 'always'.
I CONTROL  [initandlisten] **        We suggest setting it to 'never'
I CONTROL  [initandlisten]
I CONTROL  [initandlisten] ** WARNING: soft rlimits too low. rlimits set to 4096 processes, 64000 files. Number of processes should be at least 32000 : 0.5 times number of files.
I CONTROL  [initandlisten]
>
```

#### 2.1. 创建数据：

http://docs.mongodb.org/manual/tutorial/insert-documents/  http://docs.mongodb.org/manual/reference/method/db.collection.insert/

```shell
> db.users.insert(
... {
... name:"zhang san",
... age:26,
... city:"bei jing"
... }
... )
WriteResult({ "nInserted" : 1 })
> db.users.insert(
... {
... _id:1,
... name:"zhang san",
... age:26,
... city:"bei jing"
... }
... )
WriteResult({ "nInserted" : 1 })
> db.users.insert(
... {
... _id:1,
... name:"zhang san",
... age:26,
... city:"bei jing"
... }
... )
WriteResult({
        "nInserted" : 0,
        "writeError" : {
                "code" : 11000,
                "errmsg" : "E11000 duplicate key error index: test.users.$_id_ dup key: { : 1.0 }"
        }
})
> db.users.insert(
... {
... _id:2,
... name:"li si",
... age:28,
... city:"shang hai"
... }
... )
WriteResult({ "nInserted" : 1 })
```

数据可以没有主键 id，如果没有，会自动生成一个。如果设置了 `_id` 主键，就必须不重复。  否则报主键冲突：`E11000 duplicate key error index: test.users.$_id* dup key: { : 1.0}`

#### 2.2. 更新数据：

http://docs.mongodb.org/manual/tutorial/modify-documents/

```shell
> db.users.update(
... {_id:2},
... {
... $set: {
... city:"guang zhou"
... }
... }
... )
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.users.update(
... {_id:3},
... {
... $set: {
... city:"si chuan"
... }
... },
... { upsert: true }
... )
WriteResult({ "nMatched" : 0, "nUpserted" : 1, "nModified" : 0, "_id" : 3 })
```

更新使用 update，如果增加 {upsert: true}，则表示没有查询到数据直接插入。

#### 2.3. 删除：

http://docs.mongodb.org/manual/tutorial/remove-documents/

```shell
> db.users.remove({_id:3})
WriteResult({ "nRemoved" : 1 })
> db.users.remove({_id:4})
WriteResult({ "nRemoved" : 0 })
```

查询到数据才进行删除，并且返回删除数量。

#### 2.4. 查询：

http://docs.mongodb.org/manual/tutorial/query-documents/

```shell
> db.users.find({age:{ $gt: 26}})
{ "_id" : 2, "name" : "li si", "age" : 28, "city" : "guang zhou" }
> db.users.find({age:{ $gt: 25}})
{ "_id" : ObjectId("5540adf29b0f52a6786de216"), "name" : "zhang san", "age" : 26, "city" : "bei jing" }
{ "_id" : 1, "name" : "zhang san", "age" : 26, "city" : "bei jing" }
{ "_id" : 2, "name" : "li si", "age" : 28, "city" : "guang zhou" }
#查询全部数据
> db.users.find()
{ "_id" : ObjectId("5540adf29b0f52a6786de216"), "name" : "zhang san", "age" : 26, "city" : "bei jing" }
{ "_id" : 1, "name" : "zhang san", "age" : 26, "city" : "bei jing" }
{ "_id" : 2, "name" : "li si", "age" : 28, "city" : "guang zhou" }
```

#### 2.5. 更多方法

db.collection.aggregate()  db.collection.count()  db.collection.copyTo()  db.collection.createIndex()  db.collection.getIndexStats()  db.collection.indexStats()  db.collection.dataSize()  db.collection.distinct()  db.collection.drop()  db.collection.dropIndex()  db.collection.dropIndexes()  db.collection.ensureIndex()  db.collection.explain()  db.collection.find()  db.collection.findAndModify()  db.collection.findOne()  db.collection.getIndexes()  db.collection.getShardDistribution()  db.collection.getShardVersion()  db.collection.group()  db.collection.insert()  db.collection.isCapped()  db.collection.mapReduce()  db.collection.reIndex()  db.collection.remove()  db.collection.renameCollection()  db.collection.save()  db.collection.stats()  db.collection.storageSize()  db.collection.totalSize()  db.collection.totalIndexSize()  db.collection.update()  db.collection.validate()

### 3. MongoDB 可视化工具

http://www.robomongo.org/

使用可视化工具，方便使用 MongoDB 管理。  首先要修改下端口和 ip  vi /etc/mongod.conf

```shell
port=27017

dbpath=/var/lib/mongo

# location of pidfile
pidfilepath=/var/run/mongodb/mongod.pid

# Listen to local interface only. Comment out to listen on all interfaces.
bind_ip=192.168.1.36
```

然后重启 MongoDB

```shell
service mongod restart
```

### 4. 总结

MongoDB 3.0 操作起来还是很方便的。能高效的使用。  同时 MongoDB 扩展也很方便。接下来研究。  对应互联网业务来说没有复杂的 join 查询。只追求高效，快速访问。
