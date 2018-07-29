"""
This module includes a complete pipeline to retrieve input and process it
through a series of Spark transformation and action operations to allow
distributed computing in Spark standalone mode using its standalone cluster.
The whole process is submitted as jobs to Spark standalone cluster manager.

"""

import datetime
import findspark
findspark.init()
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import *
from pyspark.sql import *
from pyspark import SparkContext, SparkConf
# submit jobs to Spark standalone running cluster within python code
conf = SparkConf().setAppName('appName').setMaster('spark://localhost:7077')
sc = SparkContext(conf=conf)
# session to enable Dataframe and SQL operation
spark = SparkSession.builder.getOrCreate()

# for testing on any other computer please set this 'cwd' path relative to your computer
cwd = "/Users/dyin/Documents/mit2018/python_resources/comp5349/AnalyticsAssignment/"

# csvkit (use `pip install csvkit`) is used to preprocess original dataset in format: video_id,trending_date,category,country
# https://stackoverflow.com/questions/29642102/how-to-make-awk-ignore-the-field-delimiter-inside-double-quotes
# header and redundant data therefore are removed early for easy and speedy data processing
data = sc.textFile(cwd + "ALLvideos3.1.csv")

# create key/value pair => ((category, country), video_id) to get unique video id
# same video ids correspond to multiple trending date treated as one video id
def pairVidToCountryCategory(record):
    vid, trending_date, category, country = record.split(",")
    result = ((country, category), vid)
    return result

# create key/value pair => (country, (category, value)) for reorganization of data structure
def getVidOnCategoryByCountry(record):
    key, value = record
    country, category = key
    return (country, (category, value))

# perform transformations (map) and actions (groupByKey) on data RDD
dataVidByKey = data.map(pairVidToCountryCategory).distinct()
# all video ids grouped per category and country
dataVidGroupedByKey = dataVidByKey.groupByKey().mapValues(list)
# all video ids grouped per category and country but reorganized for further data processing
dataVidRegroupedByKey = dataVidGroupedByKey.map(getVidOnCategoryByCountry).groupByKey().mapValues(list)

# Produce dataframe with columns i.e. category, total number of video ids for country A and percentage of its in country B
# @Input is the Spark RDD after series of transformation and action operations
# @countryA, @countryB are strings of country code as in ALLVideos.csv e.g. any given pair in [US, CA, FR, DE, GB]
def corrCategoryTrendingBetweenCountries(input, countryA, countryB):
    dataA = input.filter(lambda x: x[0]==countryA).values().collect()[0]
    dataB = input.filter(lambda x: x[0]==countryB).values().collect()[0]
    dfA = spark.createDataFrame(dataA, ["CategoryA", "VideoIdA"])
    dfB = spark.createDataFrame(dataB, ["CategoryB", "VideoIdB"])
    dfJoined = dfA.join(dfB, dfA.CategoryA == dfB.CategoryB)

    # Find list of video ids of Country A that are in Country B
    def contains(videoA, videoB):
        videoAInB = [item for item in videoA if item in videoB]
        return videoAInB
    contains_udf = udf(contains)
    dfJoined = dfJoined.withColumn('VideoIdAInB', contains_udf(dfJoined['VideoIdA'],dfJoined['VideoIdB']))

    # Get length of field values in a column, i.e. length of VideoId array
    getLen = udf(lambda x: len(x), IntegerType())
    dfJoined = dfJoined.withColumn('Total', getLen(dfJoined.VideoIdA))
    dfJoined = dfJoined.withColumn("CountVideoIdAInB", getLen(dfJoined.VideoIdAInB))

    dfCalculated = dfJoined.withColumn('%VideoIdAInB', round((dfJoined.CountVideoIdAInB/dfJoined.Total)*100,1))
    dfFinal = dfCalculated.select("CategoryA", "Total", "%VideoIdAInB").withColumnRenamed("CategoryA", "Category").withColumnRenamed("%VideoIdAInB", "% in " + countryB)
    dfFinal.show()
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    dfFinal.write.csv(cwd + now + "Correlation" + countryA + "_" + countryB + ".csv", header=True)

# Main
def main():
    corrCategoryTrendingBetweenCountries(dataVidRegroupedByKey, "CA", "US")

if __name__ == "__main__":
    main()

