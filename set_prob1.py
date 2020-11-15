n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    x = input().split()
    #print(x)
    if x[0] == 'pop':
        s.pop()
    elif x[0] == 'remove':
        s.remove(int(x[1]))
    else:
        s.discard(int(x[1]))
print(sum(s))