import sys 
wordcount={}
for line in sys.stdin:
    line = line.strip()
    word_document,count=line.split('\t')
    word,document=word_document.split(',')
    print (f"{word}\t{document},{count},1")
