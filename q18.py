str1=input("enter first string")
str2=input("enter second string")
a=len(str1)
b=len(str2)
temp=0
if a==b:
    for i in range(0,a):
        temp=0
        for j in range (0,b):
            if str1[i]==str2[j]:
                temp=1
                break



if temp==1:
    print("they are anagrams !!")
elif temp == 0 or temp == 2:
    print("they are not anagrams")
