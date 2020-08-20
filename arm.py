n=int(input("Enter number"))
arm=0
n1=n
while n!=0:
    rem=n%10
    arm+=rem*rem*rem
    n//=10
if arm ==n1:
    print("Armstrong")
else:
    print("Not Armstrong")
    
