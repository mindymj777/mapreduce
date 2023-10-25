import sys 
documentcount={}
word_document={}
for line in sys.stdin:
    line = line.strip()
    document,word,count=line.split('\t')
    # print (f"{document}\t{word}\t{count}")
    try:
        count=int(count)
    except ValueError:
        continue
    try:
        documentcount[document]=documentcount[document]+count
    except:
        documentcount[document]=count
        
    word_document[word,document]=count
    
for word,document in word_document.keys():

    print(f"{word},{document}\t{word_document[word,document]},{documentcount[document]}")

