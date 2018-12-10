from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == '__main__':
    sc = SparkContext("local[2]", "NetworkWordCount")
    ssc = StreamingContext(sc, 2)

    # TODO
    # 1. Define the input sources by creating input DStreams.
    lines = ssc.socketTextStream("localhost", 9998)
    # 2. Define the streaming computations by applying transformation
    words = lines.flatMap(lambda line: line.split(" "))
    pairs = words.map(lambda word: (word, 1))
    wordCounts = pairs.reduceByKey(lambda x, y: x + y)
    # 2.1 output operations to DStreams.
    wordCounts.pprint()

    # 3. Start receiving data and processing it
    ssc.start()
    # 4. Wait for the processing to be stopped
    ssc.awaitTermination()