from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import TimestampType
from pyspark.sql import functions as F

spark = SparkSession\
    .builder\
    .appName("DummyApp")\
    .getOrCreate()

sc = spark.sparkContext

"""
Aca hice el ejericio normal sin usar glue porque no tengo accesso a aws
"""
sqlContext = SQLContext(sc)
df = sqlContext.read.\
    load("dummy_app_data.json", format="json")
df = df.withColumn("parsed", (F.col("event_time").cast(TimestampType())))
df = df.withColumn("event_date", (F.col("parsed").cast("date")))

df.groupBy(
    'event_date',
    'id',
    'country',
    'region',
    'platform',
    'language',
    'device_brand')\
    .agg(
        F.sum(
            F.when(F.col('event_type') == 'session', 1).otherwise(0)
        ).alias('ev_session'),
        F.sum(
            F.when(F.col('event_type') == 'gpy', 1).otherwise(0)
        ).alias('ev_gpy'),
        F.count(F.col('event_type')))\
    .save("agg_dummy_app_data.parquet", format="parquet")
