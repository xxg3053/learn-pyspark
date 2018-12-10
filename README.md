# pyspark

## 环境搭建
#### 服务端环境搭建
服务器：centos 7   
1. 下载相关包版本：  
hadoop-2.6.0.tar.gz     
Python-3.6.7.tgz    
scala-2.11.8.tgz    
spark-2.3.0-bin-hadoop2.6.tgz  

2. 配置环境变量
```
cat ~/.bash_profile
export SCALA_HOME=/home/kenfo/app/scala-2.11.8
export PATH=$SCALA_HOME/bin:$PATH

export HADOOP_HOME=/home/kenfo/app/hadoop-2.6.0
export PATH=$HADOOP_HOME/bin:$PATH

export SPARK_HOME=/home/kenfo/app/spark-2.3.0-bin-hadoop2.6
export PATH=$SPARK_HOME/bin:$PATH  
```

3. 修改hadoop配置

4. 启动hdfs
start-dfs.sh   
5. 启动yarn
start-yarn.sh  

#### 本地开发环境搭建
1. 在idea中edit configuration中添加两个环境变量：   
PYTHONPATH：~/spark-2.3.0-bin-hadoop2.6/python
SPARK_HOME: ~/spark-2.3.0-bin-hadoop2.6    

2. 在project structure中modules中添加 Add Content Root中
添加spark-2.3.0-bin-hadoop2.6/python/lib下的两个zip包

3. 编写测试代码

4. 在服务端运行代码
```
./spark-submit --master local --name spark_test spark_test.py
./spark-submit --master standalone --name spark_test spark_test.py
./spark-submit --master yarn --name spark_test spark_test.py

```

## Spark Core核心RDD常用算子编程
Spark Core的核心是：RDD  
RDD的五大特点：  
1. 
2. 
3.  
4. 
5.   
五大特点对应的方式是：  


 
##### RDD常用Transformation算子编程
[代码](https://github.com/xxg3053/learn-pyspark/blob/master/rdd_base.py)
- map
- flatMap
- filter 
- groupByKey
- reduceByKey
- sortByKey
- join

#### RDD常用Action算子编程
- collect
- count
- take
- reduce
- saveAsTextFile
- foreach


#### 小例子
词频统计：word_count [代码](https://github.com/xxg3053/learn-pyspark/blob/master/word_count.py)  
TopN [代码](https://github.com/xxg3053/learn-pyspark/blob/master/topn.py)   


## 运行模式
local ：    
standalone：每个节点都需要部署spark，需要启动spark集群（master,worker节点）     
yarn：只需要一个节点，然后提交作业即可，这个是不需要spark集群  
    yarn支持client和cluster模式：driver运行在哪里
    client: 提交作业的进程是不能停止的，否则作业就挂了
    cluster: 提交完作业，那么提交作业端就可以断开，因为diriver是运行在am里面   
yarn查看日志：yarn logs -applicationId application_2423412343234_0004  (日志聚合功能必须打开)   
   
不管spark运行在哪里，应用程序都不需要修改   

## Spark Core
1. 核心概念  
2. 运行架构  
3. Spark和Hadoop重要概念区分  


## Spark SQL


## Spark Stream
Spark Streaming receives live input data streams and divides the data into batches, 
which are then processed by the Spark engine to generate the final stream of results in batches

Spark Stream的核心抽象是：DStream   
