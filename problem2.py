hours = input('Enter hours :')
rate = input('Enter rate per hour :')
try :
    pay = float(hours)*float(rate)
except :
    print('Error, enter a numeric value.')
    quit()        #preventing the code to execute further

print('Gross Pay =', pay)