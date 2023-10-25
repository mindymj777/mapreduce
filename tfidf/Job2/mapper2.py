import sys 
wordcount={}
for line in sys.stdin:
    line = line.strip()
    word,document,count=line.split('\t')
    print (f"{document}\t{word}\t{count}")


