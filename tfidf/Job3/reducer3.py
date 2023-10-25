import sys 
documenetcount={}
word_document={}
document_name=[]
for line in sys.stdin:
    line = line.strip()
    word,document_count=line.split('\t')
    document,count,total_count,value=document_count.split(',')
    # print (word,document,count)
    try:
        value=int(value)
    except ValueError:
        continue
    try:
        documenetcount[word]=documenetcount[word]+value
    except:
        documenetcount[word]=value
    word_document[(word,document)]=[count,total_count]

    if document not in document_name:
        document_name.append(document)

for word,document in word_document.keys():

    print(f"{word},{document}\t{word_document[(word,document)][0]},{word_document[(word,document)][1]},{documenetcount[word]}\t{len(document_name)}")
