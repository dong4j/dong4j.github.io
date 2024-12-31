---
title: RabbitMQ 基础二
keywords:
  - RabbitMQ
categories:
  - RabbitMQ
tags:
  - RabbitMQ
  - 队列持久化
  - 消息持久化
  - 工作分发均衡
  - 动态消费者管理
abbrlink: ab083149
date: 2013-03-14 00:00:00
ai:
  - 通过设置消息和队列的持久化以及限制消费者的消息处理数量来优化消息队列中的负载平衡。这确保了即使在动态增加消费者时也能立即分配任务给新加入的工作者。同时，利用应答机制（ack）可以更高效地管理消费过程，避免大量未被确认的消息积累。
description: 通过设置消息和队列的持久化以及限制消费者的消息处理数量来优化消息队列中的负载平衡。这确保了即使在动态增加消费者时也能立即分配任务给新加入的工作者。同时，利用应答机制（ack）可以更高效地管理消费过程，避免大量未被确认的消息积累。
---

> 工作队列的主要任务是：避免立刻执行资源密集型任务，然后必须等待其完成。相反地，我们进行任务调度：我们把任务封装为消息发送给队列。工作进行在后台运行并不断的从队列中取出任务然后执行。当你运行了多个工作进程时，任务队列中的任务将会被工作进程共享执行。  
> 这样的概念在 web 应用中极其有用，当在很短的 HTTP 请求间需要执行复杂的任务

生产者:

```java
public class NewTask {
    //队列名称
    private final static String QUEUE_NAME = "workqueue";
    public static void main(String[] args) throws IOException
    {
        //创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel    channel    = connection.createChannel();
        //声明队列
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        //发送10条消息，依次在消息后面附加1-10个点
        for (int i = 0; i < 10; i++)
        {
            String dots = "";
            for (int j = 0; j <= i; j++)
            {
                dots += ".";
            }
            String message = "helloworld" + dots+dots.length();
            channel.basicPublish("", QUEUE_NAME, null, message.getBytes());
            System.out.println(" [x] Sent '" + message + "'");
        }
        //关闭频道和资源
        channel.close();
        connection.close();
    }
}
```

消费者 1:

```java
public class Work_1 {
    //队列名称
    private final static String QUEUE_NAME = "workqueue";

    public static void main(String[] argv) throws java.io.IOException,
            java.lang.InterruptedException
    {
        //区分不同工作进程的输出
        int hashCode = Work.class.hashCode();
        //创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel    channel    = connection.createChannel();
        //声明队列
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println(hashCode
                                   + " [*] Waiting for messages. To exit press CTRL+C");
        QueueingConsumer consumer = new QueueingConsumer(channel);
        // 指定消费队列
        // 关闭消息应答机制
        boolean ack = true;
        channel.basicConsume(QUEUE_NAME, ack, consumer);
        while (true)
        {
            QueueingConsumer.Delivery delivery = consumer.nextDelivery();
            String message = new String(delivery.getBody());
            System.out.println(hashCode + " [x] Received '" + message + "'");
            doWork(message);
            System.out.println(hashCode + " [x] Done");
        }
    }

    /**
     * 每个点耗时1s
     * @param task
     * @throws InterruptedException
     */
    private static void doWork(String task) throws InterruptedException
    {
        for (char ch : task.toCharArray())
        {
            if (ch == '.')
                Thread.sleep(1000);
        }
    }
}

```

消费者 2:

```java
public class Work_2 {
    //队列名称
    private final static String QUEUE_NAME = "workqueue";

    public static void main(String[] argv) throws java.io.IOException,
            java.lang.InterruptedException
    {
        //区分不同工作进程的输出
        int hashCode = Work.class.hashCode();
        //创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel    channel    = connection.createChannel();
        //声明队列
        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println(hashCode
                                   + " [*] Waiting for messages. To exit press CTRL+C");
        QueueingConsumer consumer = new QueueingConsumer(channel);
        // 指定消费队列
        // 关闭消息应答机制
        boolean ack = true;
        channel.basicConsume(QUEUE_NAME, ack, consumer);
        while (true)
        {
            QueueingConsumer.Delivery delivery = consumer.nextDelivery();
            String message = new String(delivery.getBody());
            System.out.println(hashCode + " [x] Received '" + message + "'");
            doWork(message);
            System.out.println(hashCode + " [x] Done");
        }
    }

    /**
     * 每个点耗时1s
     * @param task
     * @throws InterruptedException
     */
    private static void doWork(String task) throws InterruptedException
    {
        for (char ch : task.toCharArray())
        {
            if (ch == '.')
                Thread.sleep(1000);
        }
    }
}
```

执行结果  
消费者 1:  
`

```
895328852 [*] Waiting for messages. To exit press CTRL+C
895328852 [x] Received 'helloworld.1'
895328852 [x] Done
895328852 [x] Received 'helloworld…3'
895328852 [x] Done
895328852 [x] Received 'helloworld…..5'
895328852 [x] Done
895328852 [x] Received 'helloworld…….7'
895328852 [x] Done
895328852 [x] Received 'helloworld………9'
```

消费者 2:

```
1581781576 [*] Waiting for messages. To exit press CTRL+C
1581781576 [x] Received 'helloworld..2'
1581781576 [x] Done
1581781576 [x] Received 'helloworld….4'
1581781576 [x] Done
1581781576 [x] Received 'helloworld……6'
1581781576 [x] Done
1581781576 [x] Received 'helloworld……..8'
1581781576 [x] Done
1581781576 [x] Received 'helloworld……….10'
1581781576 [x] Done
```

### 值得注意的几点

1. 默认的，RabbitMQ 会一个一个的发送信息给下一个消费者 (consumer)，而不考虑每个任务的时长等等，且是**一次性分配**，并非一个一个分配。平均的每个消费者将会获得相等数量的消息。这样分发消息的方式叫做**round-robin**,即**轮询调度**。
2. 执行一个任务需要花费几秒钟。你可能会担心当一个工作者在执行任务时发生中断。我们上面的代码，一旦 RabbItMQ 交付了一个信息给消费者，会马上从内存中移除这个信息。在这种情况下，如果杀死正在执行任务的某个工作者，我们会丢失它正在处理的信息。我们也会丢失已经转发给这个工作者且它还未执行的消息。
3. 当我们杀死一个正在工作的进程时,分配给该进程的任务就不会执行,从而丢失消息.为了防止这种情况发生, RabbitMQ 使用了消息应答（message acknowledgments),消费者发送应答给 RabbitMQ，告诉它信息已经被接收和处理，然后 RabbitMQ 可以自由的进行信息删除。

## 消息应答机制 （message acknowledgments）

如果消费者被杀死而没有发送应答，RabbitMQ 会认为该信息没有被完全的处理，然后将会**重新转发给别的消费者**。通过这种方式，你可以确认信息不会被丢失，即使消者偶尔被杀死。  
这种机制并没有超时时间这么一说，RabbitMQ 只有在消费者连接断开时重新转发此信息。如果消费者处理一个信息需要耗费特别特别长的时间是允许的。

boolean ack = false; // 开启消息应答  
修改后的输出结果:  
消费者 1:(中途中断)

```
895328852 [*] Waiting for messages. To exit press CTRL+C
895328852 [x] Received 'helloworld.1'
895328852 [x] Done
895328852 [x] Received 'helloworld…3'
```

Process finished with exit code 130

消费者 2:

```
1581781576 [*] Waiting for messages. To exit press CTRL+C
1581781576 [x] Received 'helloworld..2'
1581781576 [x] Done
1581781576 [x] Received 'helloworld….4'
1581781576 [x] Done
1581781576 [x] Received 'helloworld……6'
1581781576 [x] Done
1581781576 [x] Received 'helloworld……..8'
1581781576 [x] Done
1581781576 [x] Received 'helloworld……….10'
1581781576 [x] Done
1581781576 [x] Received 'helloworld.1'
1581781576 [x] Done
1581781576 [x] Received 'helloworld…3'
1581781576 [x] Done
1581781576 [x] Received 'helloworld…..5'
1581781576 [x] Done
1581781576 [x] Received 'helloworld…….7'
1581781576 [x] Done
1581781576 [x] Received 'helloworld………9'
1581781576 [x] Done
```

### 值得注意的几点:

1. 在消费者 1 执行到第 2 个任务时中断了,消费者执行完分配的任务后,开始执行分配给消费者 1 的任务
2. 任务重复执行了
3. 当开启了消息应答的消费者任务中断后,此消费者的任务会重新分配给其他消费者,且是一次分配,且不管是否已经完成的工作,都会分配给其他消费者

## 消息持久化（Message durability）

通过消息应答机制,即使消费者被杀死，消息也不会被丢失。但是如果此时 RabbitMQ 服务被停止，我们的消息仍然会丢失。  
当 RabbitMQ 退出或者异常退出，将会丢失所有的队列和信息，除非你告诉它不要丢失。我们需要做两件事来确保信息不会被丢失：我们需要给所有的队列和消息设置持久化的标志。

1. 我们需要确认 RabbitMQ 永远不会丢失我们的队列。为了这样，我们需要声明它为持久化的。  
   boolean durable = true;  
   channel.queueDeclare("task_queue", durable, false, false, null);  
   注：RabbitMQ 不允许使用不同的参数重新定义一个队列，所以已经存在的队列，我们无法修改其属性。

2. 我们需要标识我们的信息为持久化的。通过设置 MessageProperties（implements BasicProperties）值为 PERSISTENT_TEXT_PLAIN。  
   channel.basicPublish("", "task_queue",MessageProperties.PERSISTENT_TEXT_PLAIN,message.getBytes());  
   现在你可以执行一个发送消息的程序，然后关闭服务，再重新启动服务，运行消费者程序做下实验。**只有第一个消费者才会处理消息**.

## 公平转发（Fair dispatch）

或许会发现，目前的消息转发机制（Round-robin）并非是我们想要的。例如，这样一种情况，对于两个消费者，有一系列的任务，奇数任务特别耗时，而偶数任务却很轻松，这样造成一个消费者一直繁忙，另一个消费者却很快执行完任务后等待。  
造成这样的原因是因为 RabbitMQ 仅仅是当消息到达队列进行转发消息。并不在乎有多少任务消费者并未传递一个应答给 RabbitMQ。仅仅盲目转发所有的奇数给一个消费者，偶数给另一个消费者。  
为了解决这样的问题，我们可以使用 basicQos 方法，传递参数为 prefetchCount = 1。这样告诉 RabbitMQ 不要在同一时间给一个消费者超过一条消息。换句话说，只有在消费者空闲的时候会发送下一条信息。

生产者:

```java
public class NewTask
{
    // 队列名称
    private final static String QUEUE_NAME = "workqueue_persistence";
    public static void main(String[] args) throws IOException
    {
        // 创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();
        // 声明队列
        boolean durable = true;// 1、设置队列持久化
        channel.queueDeclare(QUEUE_NAME, durable, false, false, null);
        // 发送10条消息，依次在消息后面附加1-10个点
        for (int i = 5; i > 0; i--)
        {
            String dots = "";
            for (int j = 0; j <= i; j++)
            {
                dots += ".";
            }
            String message = "helloworld" + dots + dots.length();
            // MessageProperties 2、设置消息持久化
            channel.basicPublish("", QUEUE_NAME,
                    MessageProperties.PERSISTENT_TEXT_PLAIN, message.getBytes());
            System.out.println(" [x] Sent '" + message + "'");
        }
        // 关闭频道和资源
        channel.close();
        connection.close();
    }
}
```

消费者 1:

```java
public class Work_1
{
    // 队列名称
    private final static String QUEUE_NAME = "workqueue_persistence";

    public static void main(String[] argv) throws java.io.IOException,
            java.lang.InterruptedException
    {
        // 区分不同工作进程的输出
        int hashCode = Work.class.hashCode();
        // 创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();
        // 声明队列
        boolean durable = true;
        channel.queueDeclare(QUEUE_NAME, durable, false, false, null);
        System.out.println(hashCode
                + " [*] Waiting for messages. To exit press CTRL+C");
        //设置最大服务转发消息数量
        int prefetchCount = 1;
        channel.basicQos(prefetchCount);
        QueueingConsumer consumer = new QueueingConsumer(channel);
        // 指定消费队列
        boolean ack = false; // 打开应答机制
        channel.basicConsume(QUEUE_NAME, ack, consumer);
        while (true)
        {
            QueueingConsumer.Delivery delivery = consumer.nextDelivery();
            String message = new String(delivery.getBody());

            System.out.println(hashCode + " [x] Received '" + message + "'");
            doWork(message);
            System.out.println(hashCode + " [x] Done");
            //channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
            channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);

        }

    }

    /**
     * 每个点耗时1s
     *
     * @param task
     * @throws InterruptedException
     */
    private static void doWork(String task) throws InterruptedException
    {
        for (char ch : task.toCharArray())
        {
            if (ch == '.')
                Thread.sleep(1000);
        }
    }
}
```

消费者 2:

```java
public class Work_2
{
    // 队列名称
    private final static String QUEUE_NAME = "workqueue_persistence";

    public static void main(String[] argv) throws java.io.IOException,
            java.lang.InterruptedException
    {
        // 区分不同工作进程的输出
        int hashCode = Work.class.hashCode();
        // 创建连接和频道
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();
        // 声明队列
        boolean durable = true;
        channel.queueDeclare(QUEUE_NAME, durable, false, false, null);
        System.out.println(hashCode
                + " [*] Waiting for messages. To exit press CTRL+C");
        //设置最大服务转发消息数量
        int prefetchCount = 1;
        channel.basicQos(prefetchCount);
        QueueingConsumer consumer = new QueueingConsumer(channel);
        // 指定消费队列
        boolean ack = false; // 打开应答机制
        channel.basicConsume(QUEUE_NAME, ack, consumer);
        while (true)
        {
            QueueingConsumer.Delivery delivery = consumer.nextDelivery();
            String message = new String(delivery.getBody());

            System.out.println(hashCode + " [x] Received '" + message + "'");
            doWork(message);
            System.out.println(hashCode + " [x] Done");
            //channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
            channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);

        }

    }

    /**
     * 每个点耗时1s
     *
     * @param task
     * @throws InterruptedException
     */
    private static void doWork(String task) throws InterruptedException
    {
        for (char ch : task.toCharArray())
        {
            if (ch == '.')
                Thread.sleep(1000);
        }
    }
}
```

此时并没有按照之前的 Round-robin 机制进行转发消息，而是当消费者不忙时进行转发。且这种模式下支持动态增加消费者，因为消息并没有发送出去，动态增加了消费者马上投入工作。而默认的转发机制会造成，即使动态增加了消费者，此时的消息已经分配完毕，无法立即加入工作，即使有很多未完成的任务。
