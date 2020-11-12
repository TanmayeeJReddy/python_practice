n = int(input())
i = input().split()
#splitting the space separated input given by the user and putting them into a list
ls = []
for num in i:
    x = int(num)
    ls.append(x)
print(ls)