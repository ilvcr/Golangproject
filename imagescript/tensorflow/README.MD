###使用心得

#####第一
tensorflow里的graph能够记住状态（state），这使得TFRecordReader能够记住tfrecord的位置，并且始终能返回下一个。而这就要求我们在使用之前，必须初始化整个graph，这里我们使用了函数tf.initialize_all_variables()来进行初始化。

#####第二
tensorflow中的队列和普通的队列差不多，不过它里面的operation和tensor都是符号型的（symbolic），在调用sess.run()时才执行。

#####第三
TFRecordReader会一直弹出队列中文件的名字，直到队列为空。

###总结

    1、生成tfrecord文件;
    2、定义record reader解析tfrecord文件;
    3、构造一个批生成器（batcher）;
    4、构建其他的操作;
    5、初始化所有的操作;
    6、启动QueueRunner;
