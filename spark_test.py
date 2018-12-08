from pyspark import SparkConf,SparkContext

# 创建SparkConf
conf = SparkConf().setMaster("local[2]").setAppName("spark0301")

# 创建SparkContext
sc = SparkContext(conf=conf)

# 业务逻辑
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
print(distData.collect())

# 结束
sc.stop()