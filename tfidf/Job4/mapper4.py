import sys 
from math import log
wordcount={}
for line in sys.stdin:
    line = line.strip()
    word_document,count,document_num=line.split('\t')
    word,document=word_document.split(',')
    count,total_count,document_count=count.split(',')
    tf=float(float(count)/float(total_count))
    idf=log(float(document_num)/float(document_count))
    tfidf=tf*idf
    print (f"{word}\t{document}\t{tfidf}")
