#a=[1,2,3,1,1,3]
a=[1,2,3]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j] and i<j:
            count+=1
print(count)
