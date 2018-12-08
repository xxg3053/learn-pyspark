import sys
from pyspark import SparkConf,SparkContext


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: wordcount <input> <output>", file=sys.stderr)
        sys.exit(-1)

    conf = SparkConf()
    sc = SparkContext(conf=conf)

    def print_result():
        counts = sc.textFile(sys.argv[1])\
            .flatMap(lambda line:line.split(" "))\
            .map(lambda x:(x,1))\
            .reduceByKey(lambda a,b:a+b)

        output = counts.collect()

        for(word, count) in output:
            print("%s: %i" % (word, count))

    def save_file():
        sc.textFile(sys.argv[1]) \
            .flatMap(lambda line:line.split(" ")) \
            .map(lambda x:(x,1)) \
            .reduceByKey(lambda a,b:a+b)\
            .saveAsTextFile(sys.argv[2])


    print_result()
    save_file()

    sc.stop()