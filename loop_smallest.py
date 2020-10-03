smallest = None
print('To find the smallest value in the list.')

for num in [12, 5, -1, 2, -3, 75, 8] :
    if smallest == None :                       #this 'if' statement of true only for the first time because 'smallest' is 'none' only for one time
        smallest = num                          #for the first time 'smallest' is true to be 'none' i.e it had no value, the statement turns true and the first 
    elif num < smallest :                       #item in the list i.e here 12 is taken into smallest.     
        smallest = num                          #From next iteration, the 'if' statement is always gonna be false since the smallest has some value in it
    print( num, smallest)                       # and is not empty ('None').

print('The smallest value is :', smallest)