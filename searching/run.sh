hadoop jar '/home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar'  \
-mapper 'python mapper.py' \
-file /home/hadoop/HW/searching/mapper.py \
-reducer 'python reducer.py' \
-file /home/hadoop/HW/searching/reducer.py \
-input hdfs:/HW1/searching/data.txt \
-output /HW1/searching/result
