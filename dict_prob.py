dictionary = dict()
handle = open('words.txt')
for line in handle:
    words = line.split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1

bigcount = None
bigword = None
for word,value in dictionary.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = word
print(bigword, bigcount)
