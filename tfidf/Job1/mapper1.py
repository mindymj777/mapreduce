import sys
for line in sys.stdin:
    line = line.strip()
    line=line.replace(".","")    
    line=line.replace(",","")    
    line_contents = line.split(" ")
    doc_name = line_contents[0]
    # print(doc_name)
    line_contents.remove(doc_name)
    for content in line_contents:
        key=content+"\t"+doc_name.replace(":","")  
        print(f"{key}\t1")



