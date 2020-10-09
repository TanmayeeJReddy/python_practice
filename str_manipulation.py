name = 'Hello World'
print(name, len(name))
#Uppercase
print(name.upper())
#Lowercase
print(name.lower())
#Capitalize first letter
print(name.capitalize())
#Slicing
print(name[:7])
#Finding
print(name.find('llo'))
#Finding between indexes
print(name.find('l',7,len(name)))
#Replacing strings
print(name.replace('World','Planet'))
#Splitting
print(name.split())
#Removing leading, trailing whitespaces(if any)
print(name.strip())
