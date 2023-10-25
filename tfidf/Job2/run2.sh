hadoop jar '/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar'  \
-mapper 'python mapper2.py' \
-file /home/hadoop/HW/tfidf/Job2/mapper2.py \
-reducer 'python reducer2.py' \
-file /home/hadoop/HW/tfidf/Job2/reducer2.py \
-input hdfs:/HW1/tfidf/result1/part-00000 \
-output /HW1/tfidf/result2S
