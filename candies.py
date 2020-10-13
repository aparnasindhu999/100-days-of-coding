candies=[2,3,5,1,3]
extra_candies=3
result=[]
for i in candies:
    if i+extra_candies>=max(candies):
        result.append(True)
    else:
        result.append(False)
print(result)

#Alternative
#m=max(candies)
#x=3
#l=[True if i+x>=m else False for i in candies]
