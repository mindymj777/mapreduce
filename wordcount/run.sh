hadoop jar '/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar'  \
-mapper 'python mapper.py' \
-file /home/hadoop/test/mapper.py \
-reducer 'python reducer.py' \
-file /home/hadoop/test/reducer.py \
-input hdfs:/user/hadoop/test/book.txt \
-output /test/result
