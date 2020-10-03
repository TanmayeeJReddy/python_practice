print('To fi, nd the largest value i the given list.')
list = [85, 1, 2, 41, 12, 17, 5, 7, 100, -1] 
largest = list[0]

for val in list :
    if val > largest :
        largest = val
        print(val, largest)
    else :
        print(val, largest)

print('Largest value in the given list is:', largest)
print('END')
