count = 0
total = 0
while True :
    x = input('Enter a number: ')
    if x == 'done' :
        break
    try :
        y = float(x)
        #print(y)
    except :
        print('Invalid Input.')
        continue
    count = count + 1
    total = total + y

print(total, count, total/count)
    
    
    
 