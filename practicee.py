#name = input('Enter you name : ')
#print('WELCOME',name)


#hr = float(input('Enter hours : '))
#rt = float(input('Rate per hour : '))
#pay = hr*rt
#print('Gross pay = ', pay)


#hours = float(input('Enter hours : '))
#rate = float(input('Rate per hour : '))
#if hours > 40 :
#   pay = (40*rate)+(hours-40)*rate*1.5
#else:
#   pay = hours*rate

#print('Gross pay =', pay)


x = float(input('Enter score : '))
if (x > 0.0 and x < 1.0):
    if(x >= 0.9):
        print('A')
    elif(x >= 0.8):
        print('B')
    elif(x >= 0.7):
        print('C')
    elif(x >= 0.6):
        print('D')
    else:
        print('F')
else:
    print('Error.')