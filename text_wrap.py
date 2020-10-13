str = input('String:')
w = int(input('Width:'))
length = len(str)
print(length)
s = 0
w1 = w
while s < length:
    x = str[s:w1]
    print(x)
    s = w1
    w1 = w1 + w
print(str[s:length])
