str1=input("enter a string")
str2=input("enter the substring you want to check in string?")
a=str2 in str1
if a==False:
    print("Not found")
else:
    print("found!!")
