str = 'Tan#ayee'
ls = []
for i in range(0,len(str)):
    ls.append(str[i])
print(ls)
ls[3] = 'm'
name = ''.join(ls)
print(name)

#Alternative method:[Using slicing and joining]

str = 'Tan#ayee'
str = str[:3] + 'm' + str[4:]
print(str)