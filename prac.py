n = int(input())
for i in range(0,n-1):
    row = []
    for j in range(0,i):
        row.append(n-j)
    row.append(n-i)
    for j in reversed(range(0,i)):
        row.append(n-j)
print(row)