# Q: Read N integers and create a list out of it. N is an input.
# 
# Output :-
# Input N: 5
# 1 2 3 4 5
# Output list: [1, 2, 3, 4, 5]


list = []
n = int(input('Input N: '))
for i in range(0,n):
    element = int(input())

    list.append(element)

print(list)
