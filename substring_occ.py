name = 'Tananamayee'
str = 'ana'

count = 0
x = 0
while x < len(name):
    start = name.find(str,x,len(name))
    ans = name.count(str,start,len(name))
    if ans != 0:
        count += 1
        x = start + 1
    else:
        break
print(count)