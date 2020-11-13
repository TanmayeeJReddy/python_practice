m = int(input())
list_1 = list(map(int,input().split()))
set_a = set(list_1)
n = int(input())
list_2 = list(map(int,input().split()))
set_b = set(list_2)
print('Set A :',set_a)
print('Set B :',set_b)

result = (set_a ^ set_b)
x = sorted(result)
print(x)
for i in x:
    print(i)