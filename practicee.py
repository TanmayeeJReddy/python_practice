#def bigsum(ar):
#    sum = 0
#    for x in ar:
#        sum = sum + x
#    return sum


#n = int(input())
#ele = input().split()
#list = []
#for i in ele:
#    int(i)
#    list.append(int(i))
#print(list)
#total = bigsum(list)
#print(total)


def aVeryBigSum(ar):
    sum = 0
    for x in ar:
        sum = sum + x
    return sum

if __name__ == '__main__':
    n = int(input())
    ele = input().split()
    list = []
    for i in ele:
       int(i)
       list.append(int(i))
    total = aVeryBigSum(list)
    print(total) 