import sys 

wordcount={}
for line in sys.stdin:
    
    line = line.strip()
    word,document,count=line.split('\t')
    # print (word,document,count)
    try:
        count=int(count)
    except ValueError:
        continue
    try:
        wordcount[(word,document)]=wordcount[(word,document)]+count
    except:
        wordcount[(word,document)]=count


for word,document in wordcount.keys():

    print(f"{word}\t{document}\t{wordcount[(word,document)]}")
