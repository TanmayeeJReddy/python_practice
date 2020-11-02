d = dict()
d['Apple'] = 5
d['Banana'] = 7
print(d)
d['Apple'] = d['Apple']+2
d['Banana'] = d['Banana']-1
print(d)

#If an element exists add 1, or else make a new one and set the count to 1
list = ['Apple','Apple','Banana','Orange','Pineapple','Pineapple','Kiwi','Olive','Olive']
for fruit in list:
    if fruit in d:
        d[fruit] = d[fruit] + 1
    else:
        d[fruit] = 1
print(d)