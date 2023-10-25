hadoop jar '/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar'  \
-mapper 'python mapper3.py' \
-file /home/hadoop/HW/tfidf/Job3/mapper3.py \
-reducer 'python reducer3.py' \
-file /home/hadoop/HW/tfidf/Job3/reducer3.py \
-input hdfs:/HW1/tfidf/result2/part-00000 \
-output /HW1/tfidf/result3
