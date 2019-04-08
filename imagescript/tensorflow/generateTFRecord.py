# -*- coding: utf-8 -*-
"""
Created on Mon Apr 08 21:12:15 2019

@author: gao->ilvcr

Description： 使用tf.train.Example来定义我们要填入的数据格式，
              然后使用tf.python_io.TFRecordWriter来写入TFRecords文件
"""

__author__ = "yoghourt->gao"


import os
import tensorflow as tf 
from PIL import Image

cwd = os.getcwd()

'''
此处我加载的数据目录如下：
-- img1.jpg
     img2.jpg
     img3.jpg
     ...
-- img1.jpg
     img2.jpg
     ...
-- ...
...
'''
writer = tf.python_io.TFRecordWriter("train.tfrecords")
for index, name in enumerate(classes):
    class_path = cwd + name + "/"
    for img_name in os.listdir(class_path):
        img_path = class_path + img_name
            img = Image.open(img_path)
            img = img.resize((224, 224))
        img_raw = img.tobytes()              #将图片转化为原生bytes
        example = tf.train.Example(features=tf.train.Features(feature={
            "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
            'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
        }))
        writer.write(example.SerializeToString())  #序列化为字符串
writer.close()


for serialized_example in tf.python_io.tf_record_iterator("train.tfrecords"):
    example = tf.train.Example()
    example.ParseFromString(serialized_example)

    image = example.features.feature['image'].bytes_list.value
    label = example.features.feature['label'].int64_list.value
    # 可以做一些预处理之类的
    print image, label
