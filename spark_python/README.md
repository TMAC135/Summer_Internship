#  Spark For Python
Spark is a fast and general engine for large-scale data processing, Here i will
briefly introduce the spark in python, after reading this file, you should be able
to run your pyspark in your ipython notebook and process data from clustering files systems(like HDFS).  
For more detailed information,refer to the official site for [spark](http://spark.apache.org/).

##  Dependencies
- [JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html),you need to setting up the JAVA enviroments like JAVA_HOME.  
- Python(2.x or 3.x) and ipython notebook, you also need to add it to the Enviroment PATH. If you are using anaconda, no worries about this.
- Spark, [download](http://spark.apache.org/downloads.html) the spark in the apache, I choose release(1.6.0), package type(pre-built for Hadoop 2.6), download type(direct download), which works well so far.

##  Setting up the spark for Python
- Unzip the download files into the directory you want to place, for my config, I make a directory under ~ named spark.    
> cd ~  
mkdir spark  
mv YOUR_UNZIPED_SPARK_files ~/spark

- Setting the Enviroment Variables for PySpark  
add  
> export SPARK_HOME="/Users/tianran/spark/spark-1.6.0-bin-hadoop2.6"  
alias pyspark='$SPARK_HOME/bin/pyspark --master local[2]'

Notice set the SPARK_HOME to the directory in your first step, and you can set any alias for startin g the pyspark shell.

- Now you can test to run the pyspark in the commend line, simply type pyspark(base on the alias setting in step2), you will be able to enter the pyspark shell.

#### test codes on the pyspark shell
Try some simple codes for your first trials on pyspark,for more detailed api, refer to this [link](http://spark.apache.org/examples.html):
> data = sc.textFile("/Users/tianran/Desktop/test.py")  
data.count()  
data.first()  
\#print all the whole file  
for i in data.collect():  
print i

#### Read csv files as DataFrame object
In order to get the DataFrame object in spark, we need external java packages when we enter the pyspark shell, so type following commend on the commend line:
> pyspark --packages com.databricks:spark-csv_2.11:1.4.0


Now you can parse the csv files as spark DataFrame,refer to more detailed [api](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame) for DataFrame in pyspark:
>
from pyspark.sql import SQLContext  
sqlContext = SQLContext(sc)
df = sqlContext.read.format('com.databricks.spark.csv').options(header='true',inferschema='true').load('FILE_PATH')
\# do some manipulations on DataFrame object in pyspark
df.show()  
df.printSchema()   
df.select("COLUMN_NAME").show()  
df.filter(df[‘COLUMN_NAME’] > 21).show()  
df.groupBy(“COLUMN_NAME”),count.show()  

For more information when parse the csv files to DataFrame, refer to the [site](https://github.com/databricks/spark-csv).

#### Transfer from DataFrame in spark to Pandas DataFrame
Now you can simply use one line code to transfer DataFrame in spark to Pandas DataFrame:
>df_pandas = df.toPandas()

#### Bound the ipython notebook with pyspark
Suppose you OK on the previous steps, now you can bound the pyspark with ipython notebook, refer to the [link](https://gist.github.com/ololobus/4c221a0891775eaa86b0)
.   
To lunch the notebook, type in the commend line:
>IPYTHON_OPTS="notebook" pyspark --packages com.databricks:spark-csv_2.11:1.4.0

There is a test1.ipynb in the directory, just try it to test whether you are bound notebook and pyspark correctly.  
Reminder: Don't forget to include the external package when lunching the notebook.


# Possible Problems and Notifications
- Notice the version of the external package spark-csv, based on my trials, version spark-csv_2.10:1.0.3 is not working when parsing the csv files, but spark-csv_2.11:1.4.0 is fine.
- About the FILE_PATH when load the csv file from local or HDFS
The FILE_PATH in the local should be the absolute path. The FILE_PATH in the HDFS clustering should be in the form:  
hdfs://YOUR_SETTING_IN_NAMENODE:port/path  
YOUR_SETTING_IN_NAMENODE corresponds to the hdfs-site.xml in namenode machine, the port number is 8020 by default.
>df=sqlContext.read.format('com.databricks.spark.csv').options(header='true',inferschema='true').load('FILE_PATH')
- Feel free to make alias when lunching the notebook with pyspark.
- Other references:
   - [python spark 入门](http://blog.jobbole.com/86232/)
