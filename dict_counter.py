d = dict()
print('Enter a line of text :')
line = input()
x = line.split()
print('Words:', x)

for word in x:
    d[word] = d.get(word, 0) + 1
print('Final count :', d)
