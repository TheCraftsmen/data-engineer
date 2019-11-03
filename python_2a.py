from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import TimestampType
from pyspark.sql import functions as F

spark = SparkSession\
    .builder\
    .appName("DummyApp")\
    .getOrCreate()

sc = spark.sparkContext


sqlContext = SQLContext(sc)
df = sqlContext.read.\
    load("dummy_app_data.json", format="json")
df = df.withColumn("parsed", (F.col("event_time").cast(TimestampType())))
df = df.withColumn("date", (F.col("parsed").cast("date")))
df = df.withColumn("hour", F.hour(F.col("parsed")))

df.printSchema()

df.orderBy('event_time', 'event_type')\
    .write.partitionBy('date', 'hour')\
    .save("dummy_app_data.parquet", format="parquet")
