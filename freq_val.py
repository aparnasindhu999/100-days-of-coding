a=[1,2,3,4]
l=[]
for i in range(0,len(a),2):
    l.extend([str(a[i+1])]*a[i])
print(l)
