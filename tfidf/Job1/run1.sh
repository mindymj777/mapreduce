hadoop jar '/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar'  \
-mapper 'python mapper1.py' \
-file /home/hadoop/HW/tfidf/Job1/mapper1.py \
-reducer 'python reducer1.py' \
-file /home/hadoop/HW/tfidf/Job1/reducer1.py \
-input hdfs:/HW1/tfidf/data.txt \
-output /HW1/tfidf/result1
