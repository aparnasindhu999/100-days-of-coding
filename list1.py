a=[2,3,5,6]
b=[6,7,8,9]
for i in b:
    if i in a:
        pass
    else:
        a.append(i)
print(a)
