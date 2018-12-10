from pyspark import SparkConf,SparkContext


if __name__ == '__main__':

    conf = SparkConf().setMaster("local[2]").setAppName("topn")
    sc = SparkContext(conf=conf)

    counts = sc.textFile('topn.txt')\
        .map(lambda x:x.split("\t"))\
        .map(lambda x:x[0].split(" ")[1])\
        .map(lambda x:(x, 1))\
        .reduceByKey(lambda a,b:a+b)\
        .map(lambda x:(x[1], x[0]))\
        .sortByKey(False)\
        .map(lambda x:(x[1], x[0]))\
        .take(5)

    for(word, count) in counts:
        print("%s: %i" % (word, count))




    sc.stop()