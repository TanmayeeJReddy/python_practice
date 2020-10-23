fhand = open('mbox.txt')
for line in fhand:
    line.rstrip()
    if line.startswith('From'):
        x = line.split()
        if len(x) < 3:          #Guardian statement
            continue
        else:
            print('Words:',x)
            print(x[2])
    else:
        continue
print("End")