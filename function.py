num = input('Enter a number :')
try :
    int(num)
except :
    print('Error.')
    quit()

big = max(num)
print(big)