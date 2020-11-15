a = int(input())
set_A = set(map(int, input().split()))
print('Set-A:',set_A)
n = int(input())

for i in range(n):
    x = input().split()
    set_B = set(map(int, input().split()))
    #print('Set-B:', set_B)

    if x[0] == 'intersection_update':
        set_A.intersection_update(set_B)     #or (set_A) &= (set_B)
    elif x[0] == 'update':
        set_A.update(set_B)         #or (set_A) |= (set_B)           
    elif x[0] == 'symmetric_difference_update':
        set_A.symmetric_difference_update(set_B)    #or (set_A) ^= (set_B)
    else:
        set_A.difference_update(set_B)     #or (set_A) -= (set_B)
print('Final Set:',set_A)

sum = 0
for num in set_A:
    sum = sum + num
print('Sum:', sum)