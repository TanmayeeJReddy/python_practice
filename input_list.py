# Q: Read N integers and create a list out of it. N is an input.
# 
# Output :-
# Input N: 5
# 1 2 3 4 5
# Output list: [1, 2, 3, 4, 5]


list = []                           #Initialising an empty list
n = int(input('Input N: '))
for i in range(0,n):                #To read the elements entered by the user
    element = int(input())          #Reads all the elements entered by the user and stores it in 'element'

    list.append(element)            #Adding the read elements into the empty list initialised in the beginning  

print(list)                         #Prints the final list
