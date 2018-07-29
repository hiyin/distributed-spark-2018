This zipped file contains:
- ALLvideos3.1.csv
- CategoryTrendingCorrelation.py
- README.txt

## (Student) Setup in MacOs High Sierra through steps below
 # Ensure passwordless `ssh localhost` especially to `chmod -R 0700 ~/.ssh` beforehand
 $ ls -l ~/.ssh
 total 40
 -rwx------  1 dyin  staff  1980 23 Apr 21:51 authorized_keys
 -rwx------  1 dyin  staff  1679 23 Apr 21:50 id_rsa
 -rwx------  1 dyin  staff   396 23 Apr 21:50 id_rsa.pub
 -rwx------  1 dyin  staff  6948 23 Apr 21:55 known_hosts

 # Use `brew install` for following dependencies
 - Java JDK v1.8 (compatible with current Scala where version > 1.8 is not)
   $brew cask search java
   $brew cask install java8
 - Scala v2.12.5
   $brew install scala
 - Apache Spark v2.3.0
   $brew install apache-spark

 # Configure environment follow instruction at https://gist.github.com/ololobus/4c221a0891775eaa86b0
 # edit .bash_profile add following env paths
 export JAVA_HOME=export $(/usr/libexec/java_home -v1.8)
 export SPARK_VERSION=`ls /usr/local/Cellar/apache-spark/ | sort | tail -1`
 export SPARK_HOME="/usr/local/Cellar/apache-spark/$SPARK_VERSION/libexec"
 export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
 export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.6-src.zip:$PYTHONPATH

 # Open PyCharm Community 2016.2
 File > Default Settings > Project Interpreter > Click "+" to add package > Search "pyspark" and "findspark" then install

## Initiate Spark standalone cluster
 Go to Spark installation directory e.g. $SPARK_HOME and launch or stop cluster with the following shell scripts
 available in $SPARK_HOME/sbin:
 - sbin/start-master.sh (get Spark master URL from http://localhost:8080 by default and copy paste below in setMaster(URL))
 - sbin/start-slaves.sh (register workers)

## Run
Execute script CategoryTrendingCorrelation.py via PyCharm (Menu > Run > Run) or inside Spark's own pyspark

## Below are the correct results this student obtained/you should expect in the console
#  by perform this assignment task following the instructions above
#  Note:
#   Results below is the same as stated in the assignment specification PDF file on the course canvas.
#   Actual results is distributedly written into chunks of files to .csv output path (see in the script),
#   however the results displayed on console and results stored in .csv files (you get) should be the same.

+--------------------+-----+-------+
|            Category|Total|% in US|
+--------------------+-----+-------+
|           Education|   33|   42.4|
|              Gaming|  129|   11.6|
|       Entertainment|  617|   31.6|
|     Travel & Events|   10|   30.0|
|Science & Technology|   39|   74.4|
|              Sports|  163|   16.6|
|       Howto & Style|  186|   33.9|
|Nonprofits & Acti...|    4|   25.0|
|    Film & Animation|  129|   32.6|
|      People & Blogs|  242|   26.0|
|     News & Politics|  100|   28.0|
|      Pets & Animals|   31|   74.2|
|    Autos & Vehicles|   13|   53.8|
|               Music|  591|   38.2|
|              Comedy|  148|   46.6|
+--------------------+-----+-------+