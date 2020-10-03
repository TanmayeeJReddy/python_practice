print('To print smallest number in the given list.')
list = [7, 12, 5, 0, 6, -1, 25]
smallest = list[0]
for num in list:
    if num < smallest :
        smallest = num
        print(num, smallest)
    else :
        print(num, smallest)

print('Smallest value in the list is:', smallest)
