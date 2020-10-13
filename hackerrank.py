n = int(input())
m = int(input())
x = (n-1)//2
y = (m-1)//2
c = '.|.'

#Upper design
for i in range(0,x):
    print((c*i).rjust(y-1,'-') + c + (c*i).ljust(y-1,'-'))
#Center line
print("WELCOME".center(m,'-'))
#Bottom design
for i in reversed(range(x)):
    print((c*i).rjust(y-1,'-') + c + (c*i).ljust(y-1,'-'))
