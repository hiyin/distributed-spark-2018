This zipped file contains

# A preprocessed file i.e. ALLvideos3.2.csv from original file that contains useful columns
# use PreprocessRawData.sh on original file to obtain this file if not found/truncated
 - ALLvideos3.2.csv
 - PreprocessRawData.sh

# Mapper and Reducer Python implementation script
 - Mapper.py
 - Reducer.py

# Introduction on how to perform this assignment task)
 - README.txt

## Instructions on how to setup and run this assignment task
#  Setup
 - export env path JAVA_HOME as where Java 1.8 JDK is installed
 - get Hadoop binary distribution and install by unpack it to a location
 - export env path HADOOP_HOME as where Hadoop is installed
 - install openssl server to enable login without password; ensure ~/.ssh directory only read and write by user
 - do `chmod +x` on mapreduce implementation scripts that Hadoop need to execute

## Example usage
# Start Hadoop psudo-distrubuted single node follow instruction here https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
  $HADOOP_HOME/sbin/start-dfs.sh

# Starting NameNode at http://localhost:50070/ by default
# Create hdfs structure
  $HADOOP_HOME/bin/hdfs dfs -mkdir /user
  $HADOOP_HOME/bin/hdfs dfs -mkdir /user/$USER

# Import input
  $HADOOP_HOME/bin/hdfs dfs -put ./dyin0637COMP5349Assignment1_3.1/ALLvideos3.1.csv input

# Run Hadoop
  $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -input input/ALLvideos3.2.csv -output output/ALLvideos3.2v3.csv -mapper Mapper.py -reducer Reducer.py

# Get output
  $HADOOP_HOME/bin/hdfs dfs -get output/ALLvideos3.2v3.csv output

## Below are the correct results this student obtained/you should expect
#  by perform this assignment task following the instructions above
#  Note
#   Results below is the same as stated in the assignment specification PDF file on the course canvas.

FR	w_7q4-aMjCE	3595.0	%
US	fN5HV79_8B8	2243.6	%
FR	r0zj_ZFXA8Y	1799.2	%
FR	s9LNDzLIeMg	2535.4	%
FR	ntGhMoXzry4	10860.2	%
CA	MGYJuETPQEg	1046.7	%
US	25Uouf_9DUk	1032.4	%
FR	Dm_J73x7_Pk	1701.1	%
FR	PP_TVFqp-kE	2716.9	%
US	BzzG-yDxA1c	1524.9	%
FR	1aI8G_uksqc	1220.4	%
US	U5sCjnezw4o	1035.6	%
US	w6rzRBHy1tk	1268.3	%
US	ySFJtla2LY4	1401.5	%
FR	iph6D-da4uI	1377.8	%
CA	qq3FniWlrxI	1380.4	%
CA	UCEYHvdlFgY	1436.8	%
FR	pqKjvilTPaE	1672.3	%
FR	gW9xvZ_IyP0	1037.8	%
CA	hpsugpjc3dE	2836.0	%
CA	_I_D_8Z4sJE	8438.1	%
CA	3v0c6smpHSk	1153.4	%
FR	maBqda6lgzM	1194.2	%
CA	COpBcuZL99g	1876.2	%
FR	sDWyVZfd9R8	2338.7	%
US	plnzNgtvvJo	3004.9	%
FR	wIh3M_68HUo	1325.3	%
US	ijVLdH5dt-c	1014.1	%
US	oMOljrWUUXc	1178.8	%
CA	UCoogBnurWk	1155.6	%
US	dN1FTF3HF6c	1298.0	%
CA	WVeVXtC00YY	1171.8	%
CA	GrDKt7NwfPs	1604.7	%
FR	yQIGVuBDak4	1190.5	%
CA	S26do5SQY_U	1090.0	%
FR	LsoLEjrDogU	2170.4	%
US	8LPVjHxXvJM	2539.3	%
US	TyHvyGVs42U	3612.0	%
US	NZFhMSgbKKM	2179.8	%
CA	3TtxYU7oKOI	3404.2	%
CA	2byhW3BOKTU	1516.5	%
CA	TRohaoCuWiY	6576.1	%
US	S_HixQBiVH0	3095.4	%
FR	NGh31vSJtF4	1620.9	%
US	WIWb8f1WIyQ	3933.2	%
US	Ev9rOA2Yjs0	1079.9	%
CA	NV-3s2wwC8c	6443.8	%
US	cqg5oc20nxk	1991.4	%
CA	LsoLEjrDogU	2170.4	%
CA	l8B5dqjsZUs	1815.9	%
CA	515lLZS082U	1277.3	%
US	LsoLEjrDogU	2247.5	%
CA	6Y65fxIRs8Q	1103.4	%
FR	FeRi86DcfyA	2996.4	%
CA	QY3Y6lUH6A4	3123.9	%
CA	7qmSwj8Pwys	1704.2	%
US	TPcV_3D3V2A	1341.4	%
FR	7h9fibMVsV0	1038.8	%
US	BQ31l1gPGKM	2039.1	%
FR	m50utO7lnqI	5162.5	%
CA	aZRrNCA0oMk	1465.7	%
CA	-JuoCd2tocw	2871.9	%
CA	oMOljrWUUXc	1178.8	%
CA	n-1QWWaRUZI	1286.6	%
FR	5BTToG-BvMc	1124.0	%
FR	r_9SlypIA98	5185.9	%
US	gA-NDZb29I4	2498.4	%
US	Z0vLiQLpsc8	1613.3	%
FR	XMVqDensxmc	2697.5	%
CA	4pyV0G7HeEc	4758.1	%
US	6J-D86wfxiE	1522.9	%
CA	Ub_oaMgiWvw	1387.7	%
US	M3mJkSqZbX4	1968.1	%
CA	hguRjCX4FiU	1060.7	%
GB	liczsmUSMA4	1419.8	%
US	6Y65fxIRs8Q	1103.4	%
CA	-K9ujx8vO_A	8298.3	%
CA	nqzIQh2D_Es	1183.1	%