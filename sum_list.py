# Q: Given a list [...........], print sum of all even numbers and odd numbers in it.
#
# E.g: [1, 2, 3, 4, 5]. Output: even: 6, odd: 9.

list = []
esum = 0
osum = 0
n = int(input('Enter number of elements ='))
for i in range(0,n):
    element = int(input())
    list.append(element)
print(list)

for num in list:
    if(num % 2 == 0):
        esum = esum + num
    else:
        osum = osum + num
print('Even:',esum)
print('Odd:',osum)
