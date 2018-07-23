import findspark
findspark.init()

# Or the following command
findspark.init("/path/to/spark_home")

from pyspark import SparkContext, SparkConf