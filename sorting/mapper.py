import sys 
for line in sys.stdin:

    line = line.strip()
    numbers = line.split(",")
    for number in numbers:
        print(f"{number}")
