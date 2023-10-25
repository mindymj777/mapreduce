hadoop jar '/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar'  \
-mapper 'python mapper4.py' \
-file /home/hadoop/HW/tfidf/Job4/mapper4.py \
-reducer 'python reducer4.py' \
-file /home/hadoop/HW/tfidf/Job4/reducer4.py \
-input hdfs:/HW1/tfidf/result3/part-00000 \
-output /HW1/tfidf/result4
