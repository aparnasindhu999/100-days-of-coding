M,N = map(int,input().split())
mid=M//2+1
#Top part
for i in range(1,mid):
    a=((i*2-1)*str(".|."))
    print(a.center(N,'-'))
b=str("Welcome")    
print(b.center(N,'-'))  
#bottom part
for i in range(mid-1,0,-1):
    c=((i*2-1)*str(".|."))
    print(c.center(N,'-'))
