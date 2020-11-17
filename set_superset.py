set_A = set(input('Set:').split())
print('Set:',set_A)
n = int(input('Number of other sets: '))
ans = True
for i in range(n):
    x = set(input().split())
    if set_A.issuperset(x) == False:
        ans = False
print(ans)
