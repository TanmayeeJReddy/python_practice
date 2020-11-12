n = int(input())
i = input().split()
ls = []
for num in i:
    x = int(num)
    ls.append(x)
print(ls)
avg = sum(ls)/len(ls)
print(avg)