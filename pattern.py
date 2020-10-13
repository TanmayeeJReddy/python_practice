n = int(input('Enter an integer: '))

#Pattern 1
for i in range(1,n+1):
    print(end='\n')
    for j in range(0,i):
        print((1+j), end=' ')
print('\n')

#Pattern 2
for i in range(1,n+1):
    print(end='\n')
    for j in range(0,i):
        print( (1+j)**2, end=' ') 
 