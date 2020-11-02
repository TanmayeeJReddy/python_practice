if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    list = []
    for i in integer_list:
        list.append(i)
t = tuple(list)
print(t)
print(hash(t))
