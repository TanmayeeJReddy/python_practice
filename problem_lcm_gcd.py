n = int(input('Enter a number : '))
x = 1
print(x)

while x <= n :
    if(x % 2 == 0):
        if x == 2:
            print(x)
            x = x + 1
        else:
            x = x + 1
            continue
    
  

print('Done.')