t = int(input('Number of test cases:'))

for i in range(t):
    x = int(input())
    set_a = set(map(int, input().split()))
    print('Set-A:',set_a)
    y = int(input())
    set_b = set(map(int, input().split()))
    print('Set-B:',set_b)

    print(set_a.issubset(set_b))
