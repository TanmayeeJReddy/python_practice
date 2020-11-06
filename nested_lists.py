n = int(input('Enter number of students:'))
list = []
for student in range(n):
    name = input('')
    marks = float(input(''))
    list.append([marks,name])
list.sort()
print(list)

list_2 = []
for i in list:
    list_2.append(i[0])
print(list_2)

sec_low = 0
for num in range(len(list_2)):
    if list_2[0] == list_2[num]:
        continue
    else:
        sec_low = list_2[num]
        break
print(sec_low)
low_names = []
for i in list:
    if sec_low == i[0]:
        low_names.append(i[1])
    else:
        continue
print(low_names)
low_names.sort()
print(low_names)
for n in low_names:
    print(n)
