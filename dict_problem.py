if __name__ == '__main__':
    n = int(input())
record = dict()
for i in range(n):
    name, *marks = input().split()
    #print([name,marks])
    scores = list(map(float,marks))
    #print(scores)
    record[name] = scores
#print(record)
queryname = input()
sum = 0
for name in record:
    if name == queryname:
        x = record[name]
        for i in x:
            sum = sum + i
            avg = sum/len(x)
        print('%.2f'%avg)
    else:
        continue