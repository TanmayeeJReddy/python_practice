str = input()
ans = False
for i in str:
    if i.isalnum() == True:
        ans = True
        print(ans)
        break
if ans == False:
    print(ans)
ans2 = False
for x in str:
    if x.isalpha() == True:
        ans2 = True
        print(ans2)
        break
if ans2 == False:
    print(ans2)
ans3 = False
for y in str:
    if y.isdigit() == True:
        ans2 = True
        print(ans2)
        break
if ans2 == False:
    print(ans2)
ans3 = False
for z in str:
    if z.islower() == True:
        ans3 = True
        print(ans3)
        break
if ans3 == False:
    print(ans3)
ans4 = False
for a in str:
    if a.isupper() == True:
        ans4 = True
        print(ans4)
        break
if ans4 == False:
    print(ans4)