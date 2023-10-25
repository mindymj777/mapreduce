import sys 

numberlist=[]

for line in sys.stdin:

    line = line.strip()
    numberlist.append(int(line))

numberlist.sort()

for num in numberlist:

    print(f"{num}")
