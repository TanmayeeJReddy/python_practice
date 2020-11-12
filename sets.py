def average(array):
    # your code goes here
    x = set(arr)
    avg = sum(x)/len(x)
    return avg

if __name__ == '__main__':
    n = int(input())
    i = input().split()
    arr = []
    for num in i:
        x = int(num)
        arr.append(x)
    result = average(arr)
    print(result)