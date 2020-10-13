a=[2,0,4,0,5,0,0,0,332,33]
for i in a:
    if i==0:
        a.remove(i)
        a.append(0)
print(a)
