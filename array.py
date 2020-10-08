def simpleArraySum(ar):
    total = 0
    for x in ar:
        total = total + x
    return total

if __name__ == '__main__':
    arr = []
    n = int(input())
    ele = input().split()
    for i in ele:
        int(i)
        arr.append(int(i))
    total = simpleArraySum(arr)
    print(total)    

        
    
    