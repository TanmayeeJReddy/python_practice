x = input('Enter temperature in celsius = ')
try:
    cel = float(x)
   
except:
    print('Invalid input.')
    quit()
fahr = (cel*1.8)+32
print('Temperature in fahrenheit is : ', fahr)
    
