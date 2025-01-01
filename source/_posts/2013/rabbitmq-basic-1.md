---
title: RabbitMQ入门：深入理解消息队列核心概念
keywords:
  - RabbitMQ
categories:
  - 新时代码农
tags:
  - RabbitMQ
  - 分布式系统
  - 异步通信
  - 消息传递
  - 队列管理
  - 交换机
  - 权限隔离
abbrlink: 90881fe0
date: 2013-03-12 00:00:00
ai:
  - 本段文本提供了关于消息队列系统，特别是RabbitMQ的深入理解。主要介绍了Broker、Exchange、Queue、Binding、Routing Key和Vhost等概念，并详细描述了消息队列使用过程中的各个步骤。此外，文中还强调了消息队列持久化的重要性及其实现方式，包括exchange、queue以及消息本身的持久化设置。
description: 本段文本提供了关于消息队列系统，特别是RabbitMQ的深入理解。主要介绍了Broker、Exchange、Queue、Binding、Routing
  Key和Vhost等概念，并详细描述了消息队列使用过程中的各个步骤。此外，文中还强调了消息队列持久化的重要性及其实现方式，包括exchange、queue以及消息本身的持久化设置。
---

RabbitMQ 是一个由 erlang 开发的 AMQP（Advanced Message Queue ）的开源实现。AMQP 的出现其实也是应了广大人民群众的需求，虽然在同步消息通讯的世界里有很多公开标准（如 COBAR 的 IIOP ，或者是 SOAP 等），但是在异步消息处理中却不是这样，只有大企业有一些商业实现（如微软的 MSMQ ，IBM 的 Websphere MQ 等），因此，在 2006 年的 6 月，Cisco 、Redhat、iMatix 等联合制定了 AMQP 的公开标准。

RabbitMQ 是由 RabbitMQ Technologies Ltd 开发并且提供商业支持的。该公司在 2010 年 4 月被 SpringSource（VMWare 的一个部门）收购。在 2013 年 5 月被并入 Pivotal。其实 VMWare，Pivotal 和 EMC 本质上是一家的。不同的是 VMWare 是独立上市子公司，而 Pivotal 是整合了 EMC 的某些资源，现在并没有上市。

RabbitMQ 的官网是<http://www.rabbitmq.com>

## 应用

1. RabbitMQ Server： 也叫 broker server，它不是运送食物的卡车，而是一种传输服务。原话是 RabbitMQisn’t a food truck, it’s a delivery service. 他的角色就是维护一条从 Producer 到 Consumer 的路线，保证数据能够按照指定的方式进行传输。但是这个保证也不是 100% 的保证，但是对于普通的应用来说这已经足够了。当然对于商业系统来说，可以再做一层数据一致性的 guard，就可以彻底保证系统的一致性了。
2. Client A & B： 也叫 Producer，数据的发送方。createmessages and publish (send) them to a broker server (RabbitMQ).一个 Message 有两个部分：payload（有效载荷）和 label（标签）。payload 顾名思义就是传输的数据。label 是 exchange 的名字或者说是一个 tag，它描述了 payload，而且 RabbitMQ 也是通过这个 label 来决定把这个 Message 发给哪个 Consumer。AMQP 仅仅描述了 label，而 RabbitMQ 决定了如何使用这个 label 的规则。
3. Client 1，2，3：也叫 Consumer，数据的接收方。Consumersattach to a broker server (RabbitMQ) and subscribe to a queue。把 queue 比作是一个有名字的邮箱。当有 Message 到达某个邮箱后，RabbitMQ 把它发送给它的某个订阅者即 Consumer。当然可能会把同一个 Message 发送给很多的 Consumer。在这个 Message 中，只有 payload，label 已经被删掉了。对于 Consumer 来说，它是不知道谁发送的这个信息的。就是协议本身不支持。但是当然了如果 Producer 发送的 payload 包含了 Producer 的信息就另当别论了。

### 为什么使用 Channel，而不是直接使用 TCP 连接？

对于 OS 来说，建立和关闭 TCP 连接是有代价的，频繁的建立关闭 TCP 连接对于系统的性能有很大的影响，而且 TCP 的连接数也有限制，这也限制了系统处理高并发的能力。但是，在 TCP 连接中建立 Channel 是没有上述代价的。对于 Producer 或者 Consumer 来说，可以并发的使用多个 Channel 进行 Publish 或者 Receive。有实验表明，1s 的数据可以 Publish10K 的数据包。当然对于不同的硬件环境，不同的数据包大小这个数据肯定不一样，但是我只想说明，对于普通的 Consumer 或者 Producer 来说，这已经足够了。如果不够用，你考虑的应该是如何细化 split 你的设计。

## 创建步骤

生产者:

1. 创建连接
2. 创建频道
3. 创建消息体
4. 发送消息

消费者:

1. 创建连接 (循环等待连接)
2. 创建频道
3. 接收消息

使用场景：简单的发送与接收，没有特别的处理。

Producer: 生产者 发送方

```java
public class Send {
    //队列名称
    private final static String QUEUE_NAME = "hello";
    public static void main(String[] argv) throws java.io.IOException, InterruptedException {
        /**
         * 创建连接连接到MabbitMQ
         */
        ConnectionFactory factory = new ConnectionFactory();
        //设置MabbitMQ所在主机ip或者主机名
        factory.setHost("localhost");
        //创建一个连接
        Connection connection = factory.newConnection();
        //创建一个频道
        Channel channel = connection.createChannel();
        //指定一个队列
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        //发送的消息
        String message = "";
        //往队列中发出一条消息
        for(int i = 0; i < 10; i++){
            message = "hello world!" + i;
            channel.basicPublish("", QUEUE_NAME, null, message.getBytes());
            System.out.println(" [x] Sent '" + message + "'");
            Thread.sleep(1000);
        }
        //关闭频道和连接
        channel.close();
        connection.close();
    }
}
```

Consumer: 消费者

```java
public class Recv {
   //队列名称
   private final static String QUEUE_NAME = "hello";
   public static void main(String[] argv) throws java.io.IOException,
           java.lang.InterruptedException {
       //打开连接和创建频道，与发送端一样
       ConnectionFactory factory = new ConnectionFactory();
       factory.setHost("localhost");
       Connection connection = factory.newConnection();
       Channel    channel    = connection.createChannel();
       //声明队列，主要为了防止消息接收者先运行此程序，队列还不存在时创建队列。
       channel.queueDeclare(QUEUE_NAME, false, false, false, null);
       System.out.println(" [*] Waiting for messages. To exit press CTRL+C");
       //创建队列消费者
       QueueingConsumer consumer = new QueueingConsumer(channel);
       //指定消费队列
       channel.basicConsume(QUEUE_NAME, true, consumer);
       while (true) {
           //nextDelivery是一个阻塞方法（内部实现其实是阻塞队列的take方法）
           QueueingConsumer.Delivery delivery = consumer.nextDelivery();
           String                    message  = new String(delivery.getBody());
           System.out.println(" [x] Received '" + message + "'");
       }
   }
}
```

### 值得注意的几点

1. 队列只会在它不存在的时候创建，多次声明并不会重复创建
2. 生产者和消费者可以不再同一台机子上
3. 消息队列与 socket 类似 都是要有接受者和发送者 接受者循环等待发送者发送的消息
4. 接受者通过队列名来区分到底接收哪里发送过来的消息
5. 发送者发送消息时必须要用队列名标识,接受者通过队列名接收指定的消息
6. 发送者可以向相同的队列发送消息,多个接受者可以接收同一个队列的消息

### 几个概念说明：

**Broker**：简单来说就是消息队列服务器实体。  
**Exchange**：消息交换机，它指定消息按什么规则，路由到哪个队列。  
**Queue**：消息队列载体，每个消息都会被投入到一个或多个队列。  
**Binding**：绑定，它的作用就是把 exchange 和 queue 按照路由规则绑定起来。  
**Routing Key**：路由关键字，exchange 根据这个关键字进行消息投递。  
**vhost**：虚拟主机，一个 broker 里可以开设多个 vhost，用作不同用户的权限分离。  
**producer**：消息生产者，就是投递消息的程序。  
**consumer**：消息消费者，就是接受消息的程序。  
**channel**：消息通道，在客户端的每个连接里，可建立多个 channel，每个 channel 代表一个会话任务。  
消息队列的使用过程大概如下：  
（1）客户端连接到消息队列服务器，打开一个 channel。  
（2）客户端声明一个 exchange，并设置相关属性。  
（3）客户端声明一个 queue，并设置相关属性。  
（4）客户端使用 routing key，在 exchange 和 queue 之间建立好绑定关系。  
（5）客户端投递消息到 exchange。  
exchange 接收到消息后，就根据消息的 key 和已经设置的 binding，进行消息路由，将消息投递到一个或多个队列里。  
exchange 也有几个类型，完全根据 key 进行投递的叫做 Direct 交换机，例如，绑定时设置了 routing key 为”abc”，那么客户端提交的消息，只有设置了 key 为”abc”的才会投递到队列。对 key 进行模式匹配后进行投递的叫做 Topic 交换机，符号”#”匹配一个或多个词，符号”_”匹配正好一个词。例如”abc.#”匹配”abc.def.ghi”，”abc._”只匹配”abc.def”。还有一种不需要 key 的，叫做 Fanout 交换机，它采取广播模式，一个消息进来时，投递到与该交换机绑定的所有队列。  
RabbitMQ 支持消息的持久化，也就是数据写在磁盘上，为了数据安全考虑，我想大多数用户都会选择持久化。消息队列持久化包括 3 个部分：  
（1）exchange 持久化，在声明时指定 durable => 1  
（2）queue 持久化，在声明时指定 durable => 1  
（3）消息持久化，在投递时指定 delivery_mode => 2（1 是非持久化）  
如果 exchange 和 queue 都是持久化的，那么它们之间的 binding 也是持久化的。如果 exchange 和 queue 两者之间有一个持久化，一个非持久化，就不允许建立绑定。
