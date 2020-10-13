a=[8,1,2,2,3]
r=[]
#c=0
for i in (a):
    c=0
    for j in (a):
        if j<i:
            c+=1

    r.append(c)
print(r)

