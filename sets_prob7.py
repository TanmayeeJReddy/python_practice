k = int(input())
lis = list(map(int, input().split()))
print('List:',lis)
set_ = set(lis)
print('Set:',set_)
for i in set_:
    lis.remove(i)
    if i not in lis:
        print(i)
        break