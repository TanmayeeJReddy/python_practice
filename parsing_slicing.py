str = "X-DSPAM-Confidence: 0.8475 "
print('String: ',str)
pos = str.find(':')
print('Position of \':\'-',pos)
s = str[pos+1 :]
x = s.strip()
print(x)
y = float(x)
print("The float value of the numeric part of the string:",end='')
print(y)
