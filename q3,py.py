n=int(input("enter the number you want to find factorial of"))
if n==0:
    print("factorial is 1")
elif n==1:
    print("factorial is 1")
else:
    if (n>1):
        fact=1
        for i in range(1,n+1):
            fact = fact*i

        print("the factorial of " , n , "is ",fact)