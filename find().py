s = "abcdcdc"
str = "cdc"
#First occurrence of str[0] in 's'
x = s.find(str[0])
print(x)
#Second occurrence
y = s.find(str[0],x+1,len(s))
print(y)
#Third occurrence
z = s.find(str[0],y+1,len(s))
print(z)

name = "Tananamayee"
str = "ana"
x = name.find(str[0])
print(x)
x1 = name.count(str,x,len(name))
print(x1)
y = name.find(str[0],x+1,len(name))
print(y)
y1 = name.count(str,y,len(name))
print(y1)
z = name.find(str[0],y+1,len(name))
print(z)
z1 = name.count(str,z,len(name))
print(z1)

count = x1+y1+z1
print('Count=',count)