records = list()
while True:
    try:
        records.append(input())
    except EOFError:
        break
        
for line in records:
    print(line)