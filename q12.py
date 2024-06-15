a=int(input("enter the number"))
if a==0:
   sum=0
elif a==1:
    sum=1
else:
    sum=0
    while(a>0):
     b=a%10
     sum = sum +b
     a=a//10#performs integer division
print("The sum of the digits is ",sum)