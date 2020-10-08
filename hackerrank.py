str = input()
i,c = input().split()
x = int(i)

string = str[:x] + c +str[x+1:]
print(string)