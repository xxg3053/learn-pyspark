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
./spark-submit --master local[2] --name spark_test spark_test.py

```

## Spark Core核心RDD常用算子编程
##### RDD常用Transformation算子编程
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
词频统计：word_count
TopN   
