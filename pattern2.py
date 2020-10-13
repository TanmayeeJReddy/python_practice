import string
ls = list(string.ascii_lowercase)

n = 5
for i in range(1,n+1):
    print('\n''a', end='')
    for j in range(1,i):
        print('-'+ls[j], end='')
    