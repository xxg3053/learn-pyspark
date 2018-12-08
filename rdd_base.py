from pyspark import SparkConf,SparkContext
"""
map: map(func)
    将func函数作用到数据集的每一个元素上，生成一个新的分布式的数据集返回
    
"""
# 简单map操作
def map1(sc):
    data = [1, 2, 3, 4]
    rdd1 = sc.parallelize(data) # 转成RDD
    rdd2 = rdd1.map(lambda x:x*2)
    print(rdd2.collect())

# word -> (word, 1)
def map2(sc):
    a = sc.parallelize(["dog", "tiger", "lion"])
    b = a.map(lambda x:(x, 1))
    print(b.collect())


"""
filter： filter(func)
    选出所有func返回值为True的元素， 生成一个新的分布式数据集返回

"""
def filter1(sc):
    a = sc.parallelize([1, 2, 3, 4, 5, 6])
    b = a.filter(lambda x:x>3)
    print(b.collect())

def map_filter(sc):
    rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6]).map(lambda x:x*2).filter(lambda x:x>5)
    print(rdd1.collect())


"""
flatMap: flatMap(func)
    输入的item能够被map到0或者多个items输出，返回值是一个sequence
    打散数据
"""
# 将每个元素的单词按空格分割
def flat_map1(sc):
    data = ["hello spark", "hello world", "hello world"]
    rdd1 = sc.parallelize(data)
    print(rdd1.flatMap(lambda line:line.split(" ")).collect())


"""
groupByKey：
    把相同的key的数据分发到一起

"""
def group_by1(sc):
    data = ["hello spark", "hello world", "hello world"]
    rdd1 = sc.parallelize(data)
    rdd2 = rdd1.flatMap(lambda line:line.split(" "))
    rdd3 = rdd2.map(lambda x:(x, 1))
    gbrdd = rdd3.groupByKey()
    print(gbrdd.collect())
    print(gbrdd.map(lambda x:{x[0]:list(x[1])}).collect())


"""
reduceByKey：
    把相同的key的数据分发到一起并进行相应的计算

"""
# word count
def reduce_by1(sc):
    data = ["hello spark", "hello world", "hello world"]
    rdd = sc.parallelize(data)
    map_rdd = rdd.flatMap(lambda line:line.split(" ")).map(lambda x:(x, 1))
    reduce_by_key = map_rdd.reduceByKey(lambda a,b:a+b)
    print(reduce_by_key.collect())

"""
sortByKey: 
    根据key排序
"""
def sort_by1(sc):
    data = ["hello spark", "hello world", "hello world"]
    rdd = sc.parallelize(data)
    map_rdd = rdd.flatMap(lambda line:line.split(" ")).map(lambda x:(x, 1))
    print(map_rdd.reduceByKey(lambda a,b:a+b)
          .map(lambda x:(x[1], x[0]))
          .sortByKey(False)
          .map(lambda x:(x[1], x[0]))
          .collect()
          )


"""
union: 

"""
def union1(sc):
    a = sc.parallelize([1, 2, 3])
    b = sc.parallelize([3, 4, 5])
    print(a.union(b).collect()) #[1, 2, 3, 3, 4, 5]


"""
distinct: 

"""
def distinct1(sc):
    a = sc.parallelize([1, 2, 3])
    b = sc.parallelize([3, 4, 5])
    print(a.union(b).distinct().collect())


"""
join: 
    leftOuterJoin
    rightOuterJoin
    fullOuterJoin
"""
def inner_join1(sc):
    a = sc.parallelize([("A", "a1"), ("C", "c1"), ("D", "d1")])
    b = sc.parallelize([("A", "a2"), ("C", "c2"), ("C", "c3")])
    print(a.join(b).collect())

def left_outer_join1(sc):
    a = sc.parallelize([("A", "a1"), ("C", "c1"), ("D", "d1")])
    b = sc.parallelize([("A", "a2"), ("C", "c2"), ("C", "c3"),("E", "e1")])
    print(a.leftOuterJoin(b).collect())


"""
collect
count
take
max
min
sum
"""

def actions1(sc):
    rdd = sc.parallelize([1, 2, 3, 4, 5])
    print(rdd.collect())
    print(rdd.count())
    #print(rdd.take(3))
    print(rdd.max())
    print(rdd.min())
    print(rdd.sum())
    rdd.foreach(lambda x:print(x))
    print(rdd.reduce(lambda x,y:x+y))



if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("spark0301")
    sc = SparkContext(conf=conf)

    # map1(sc)
    # map2(sc)
    # filter1(sc)
    # map_filter(sc)
    #flat_map1(sc)
    # group_by1(sc)
    # reduce_by1(sc)
    # sort_by1(sc)
    # union1(sc)
    # distinct1(sc)
    # left_outer_join1(sc)
    actions1(sc)


    sc.stop()