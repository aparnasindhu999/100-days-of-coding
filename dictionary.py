a={}
n=int(input("Enter number of keys: "))
for i in range(0,n):
    k=input('Enter a key: ')
    v=[]
    s=int(input("Enter value count: "))
    for j in range(0,s):
        m=int(input('Enter marks: '))
        v.append(m)
    a[k]=v
print(a)


