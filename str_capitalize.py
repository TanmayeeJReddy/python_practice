s = input('Enter string :')
x = s.split(' ')
#print(x)
list = []
for i in x:
    z = i.capitalize()
    #print(z)
    list.append(z)
#print(list)
ans = ' '.join(list)
print('Capitalized string is: ',ans)
