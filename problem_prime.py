n = int(input('Enter a number : '))

for i in range(2, n):
    if(i == 2):
        print(i)
    else:
        is_prime = True
        for p in range(2, i-1):
            if(i % p == 0):
                is_prime = False
                break
        if is_prime:
            print(i)

print('Done.')