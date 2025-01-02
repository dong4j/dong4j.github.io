---
title: RabbitMQ基础教程：Fanout交换器与多消费者模型
keywords:
  - RabbitMQ
  - 发布/订阅模式
  - 转发器
  - Direct Exchange
  - Topic Exchange
  - Fanout Exchange
  - 临时队列
  - 绑定
categories:
  - 软件推荐
tags:
  - RabbitMQ
  - 发布/订阅模式
  - 转发器
  - Direct Exchange
  - Topic Exchange
  - Fanout Exchange
  - 临时队列
  - 绑定
abbrlink: e954a744
date: 2013-03-15 00:00:00
ai:
  - 本文讨论了在RabbitMQ中实现发布/订阅模式的方法。通过创建一个简单的日志系统，展示了如何将消息发送给多个消费者。文章介绍了不同类型的转发器（Exchanges）及其工作原理，包括Direct、Topic和Fanout类型。同时，还讲解了如何使用临时队列和绑定机制来实现这种模式。最后，提供了生产者和消费者的完整Java代码示例，以展示如何在RabbitMQ中实现日志的发布/订阅功能。
description: 本文讨论了在RabbitMQ中实现发布/订阅模式的方法。通过创建一个简单的日志系统，展示了如何将消息发送给多个消费者。文章介绍了不同类型的转发器（Exchanges）及其工作原理，包括Direct、Topic和Fanout类型。同时，还讲解了如何使用临时队列和绑定机制来实现这种模式。最后，提供了生产者和消费者的完整Java代码示例，以展示如何在RabbitMQ中实现日志的发布/订阅功能。
---

使用场景：发布、订阅模式，发送端发送广播消息，多个接收端接收。

前面我们实现了工作队列，并且我们的工作队列中的一个任务只会发给一个工作者，除非某个工作者未完成任务意外被杀死，会转发给另外的工作者。这篇博客中，我们会做一些改变，就是把一个消息发给多个消费者，这种模式称之为发布/订阅（类似观察者模式）。

为了验证这种模式，我们准备构建一个简单的日志系统。这个系统包含两类程序，一类程序发动日志，另一类程序接收和处理日志。  
         在我们的日志系统中，每一个运行的接收者程序都会收到日志。然后我们实现，一个接收者将接收到的数据写到硬盘上，与此同时，另一个接收者把接收到的消息展现在屏幕上。  
         本质上来说，就是发布的日志消息会转发给所有的接收者。

## 转发器（Exchanges）

前面的博客中我们主要的介绍都是发送者发送消息给队列，接收者从队列接收消息。下面我们会引入**Exchanges**，展示 RabbitMQ 的完整的消息模型。  
RabbitMQ 消息模型的核心理念是生产者永远不会直接发送任何消息给队列，一般的情况生产者甚至不知道消息应该发送到哪些队列。  
相反的，生产者只能发送消息给转发器（Exchange）。转发器是非常简单的，一边接收从生产者发来的消息，另一边把消息推送到队列中。转发器必须清楚的知道消息如何处理它收到的每一条消息。是否应该追加到一个指定的队列？是否应该追加到多个队列？或者是否应该丢弃？这些规则通过转发器的类型进行定义。

下面列出一些可用的转发器类型：

### Direct

完全根据 key 进行投递

任何发送到 Direct Exchange 的消息都会被转发到 RouteKey 中指定的 Queue。

1. 一般情况可以使用 rabbitMQ 自带的 Exchange：”"(该 Exchange 的名字为空字符串，下文称其为 default Exchange)。
2. 这种模式下不需要将 Exchange 进行任何绑定 (binding) 操作
3. 消息传递时需要一个“RouteKey”，可以简单的理解为要发送到的队列名字。
4. 如果 vhost 中不存在 RouteKey 中指定的队列名，则该消息会被抛弃。

### Topic

对 key 进行模式匹配后进行投递

任何发送到 Topic Exchange 的消息都会被转发到所有关心 RouteKey 中指定话题的 Queue 上

1. 这种模式较为复杂，简单来说，就是每个队列都有其关心的主题，所有的消息都带有一个“标题”(RouteKey)，Exchange 会将消息转发到所有关注主题能与 RouteKey 模糊匹配的队列。
2. 这种模式需要 RouteKey，也许要提前绑定 Exchange 与 Queue。
3. 在进行绑定时，要提供一个该队列关心的主题，如“#.log.#”表示该队列关心所有涉及 log 的消息 (一个 RouteKey 为”MQ.log.error”的消息会被转发到该队列)。
4. “#”表示 0 个或若干个关键字，“_”表示一个关键字。如“log._”能与“log.warn”匹配，无法与“log.warn.timeout”匹配；但是“log.#”能与上述两者匹配。
5. 同样，如果 Exchange 没有发现能够与 RouteKey 匹配的 Queue，则会抛弃此消息。

### Headers

### Fanout

不需要 key,采取广播模式，一个消息进来时，投递到与该交换机绑定的所有队列。

任何发送到 Fanout Exchange 的消息都会被转发到与该 Exchange 绑定 (Binding) 的所有 Queue 上。

1. 可以理解为路由表的模式
2. 这种模式不需要 RouteKey
3. 这种模式需要提前将 Exchange 与 Queue 进行绑定，一个 Exchange 可以绑定多个 Queue，一个 Queue 可以同多个 Exchange 进行绑定。
4. 如果接受到消息的 Exchange 没有与任何 Queue 绑定，则消息会被抛弃。

目前我们关注最后一个 fanout，声明转发器类型的代码：  
`channel.exchangeDeclare("logs","fanout");`  
fanout 类型转发器特别简单，把所有它介绍到的消息，广播到所有它所知道的队列。不过这正是我们前述的日志系统所需要的。

### 匿名转发器（nameless exchange）

前面说到生产者只能发送消息给转发器（Exchange），但是我们前两篇博客中的例子并没有使用到转发器，我们仍然可以发送和接收消息。这是因为我们使用了一个默认的转发器，它的标识符为””。之前发送消息的代码：  
`channel.basicPublish("", QUEUE_NAME,MessageProperties.PERSISTENT_TEXT_PLAIN, message.getBytes());`  
第一个参数为转发器的名称，我们设置为”” : 如果存在 routingKey（第二个参数），消息由 routingKey 决定发送到哪个队列。  
现在我们可以指定消息发送到的转发器：  
`channel.basicPublish( "logs","", null, message.getBytes());`

### 临时队列（Temporary queues）

前面的博客中我们都为队列指定了一个特定的名称。能够为队列命名对我们来说是很关键的，我们需要指定消费者为某个队列。当我们希望在生产者和消费者间共享队列时，为队列命名是很重要的。不过，对于我们的日志系统我们并不关心队列的名称。我们想要接收到所有的消息，而且我们也只对当前正在传递的数据的感兴趣。为了满足我们的需求，需要做两件事：

1. 无论什么时间连接到 Rabbit 我们都需要一个新的空的队列。为了实现，我们可以使用随机数创建队列，或者更好的，让服务器给我们提供一个随机的名称。
2. 一旦消费者与 Rabbit 断开，消费者所接收的那个队列应该被自动删除。Java 中我们可以使用 queueDeclare() 方法，不传递任何参数，来创建一个非持久的、唯一的、自动删除的队列且队列名称由服务器随机产生。  
   `String queueName = channel.queueDeclare().getQueue();`一般情况这个名称与 amq.gen-JzTY20BRgKO-HjmUJj0wLg 类似。

### 绑定（Bindings）

我们已经创建了一个 fanout 转发器和队列，我们现在需要通过 binding 告诉转发器把消息发送给我们的队列。  
`channel.queueBind(queueName, “logs”, ””)` 参数 1：队列名称 ；参数 2：转发器名称

### 完整的例子

生产者:

```java
public class EmitLog {
    private final static String EXCHANGE_NAME = "ex_log";

    public static void main(String[] args) throws IOException {
        // 创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel    channel    = connection.createChannel();
        // 声明转发器和类型
        channel.exchangeDeclare(EXCHANGE_NAME, "fanout");

        String message = new Date().toLocaleString() + " : log something";
        // 往转发器上发送消息
        channel.basicPublish(EXCHANGE_NAME, "", null, message.getBytes());

        System.out.println(" [x] Sent '" + message + "'");

        channel.close();
        connection.close();
    }
}
```

消费者 1:

```java
public class ReceiveLogsToSave {
    private final static String EXCHANGE_NAME = "ex_log";

    public static void main(String[] argv) throws java.io.IOException,
            java.lang.InterruptedException {
        // 创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel    channel    = connection.createChannel();

        channel.exchangeDeclare(EXCHANGE_NAME, "fanout");
        // 创建一个非持久的、唯一的且自动删除的队列
        String queueName = channel.queueDeclare().getQueue();
        // 为转发器指定队列，设置binding
        channel.queueBind(queueName, EXCHANGE_NAME, "");

        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");

        QueueingConsumer consumer = new QueueingConsumer(channel);
        // 指定接收者，第二个参数为自动应答，无需手动应答
        channel.basicConsume(queueName, true, consumer);

        while (true) {
            QueueingConsumer.Delivery delivery = consumer.nextDelivery();
            String                    message  = new String(delivery.getBody());

            print2File(message);
        }
    }

    private static void print2File(String msg) {
        try {
            String dir = ReceiveLogsToSave.class.getClassLoader().getResource("").getPath();
            System.out.println(dir);
            String logFileName = new SimpleDateFormat("yyyy-MM-dd")
                    .format(new Date());
            File             file = new File(dir, logFileName + ".txt");
            FileOutputStream fos  = new FileOutputStream(file, true);
            fos.write((msg + "\r\n").getBytes());
            fos.flush();
            fos.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

消费者 2:

```java
public class ReceiveLogsToConsole {
    private final static String EXCHANGE_NAME = "ex_log";

    public static void main(String[] argv) throws java.io.IOException,
            java.lang.InterruptedException {
        // 创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel    channel    = connection.createChannel();
        channel.exchangeDeclare(EXCHANGE_NAME, "fanout");
        // 创建一个非持久的、唯一的且自动删除的队列
        String queueName = channel.queueDeclare().getQueue();
        // 为转发器指定队列，设置binding
        channel.queueBind(queueName, EXCHANGE_NAME, "");
        System.out.println(" [*] Waiting for messages. To exit press CTRL+C");
        QueueingConsumer consumer = new QueueingConsumer(channel);
        // 指定接收者，第二个参数为自动应答，无需手动应答
        channel.basicConsume(queueName, true, consumer);
        while (true) {
            QueueingConsumer.Delivery delivery = consumer.nextDelivery();
            String                    message  = new String(delivery.getBody());
            System.out.println(" [x] Received '" + message + "'");
        }
    }
}
```
