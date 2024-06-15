str= input("enter a string")
a=len(str)
counted = []
for i in range(0,a):
    if str[i] not in counted:
         count=0
         for j in range (0,a):
            if str[i]==str[j]:
                count=count+1
         print("the frequency of ",str[i],"is",count)
         counted.append(str[i])