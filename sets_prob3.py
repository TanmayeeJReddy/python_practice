n = int(input())
set_a = set(map(int, input().split()))
print('Set A:',set_a)
b = int(input())
set_b = set(map(int, input().split()))
print('Set B:',set_b)

set_c = set_a.intersection(set_b)
print('Students in both Set-A & Set-B:',set_c)

sum = 0
for num in set_c:
    sum += 1
print('Total Number of Students:',sum)