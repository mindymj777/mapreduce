import sys 
import re

search_keyword='she'

num_sentence=0


for line in sys.stdin:
	line = line.strip()
	line=line.split(".")
	for i in range(len(line)):
	    if search_keyword in line[i]:
	    	num_sentence+=1
	    	if(num_sentence==1):
	    		print(f"This article has your searching word \"{search_keyword}\":")
	    	print(f"[{num_sentence}]{line[i]}.\n")

