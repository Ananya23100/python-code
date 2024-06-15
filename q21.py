list1=[]
counted=[]
while(1):
    a=input("enter number .to stop type 'quit'")
    if (a=='quit'):
        break
    num=int(a)
    list1.append(num)
b=len(list1)
for i in range(0,b):
    if list1[i] in counted:
        continue
    else:
       count=0
       for j in range(0,b):
          if list1[i]==list1[j]:
               count=count+1


       print("the count of",list1[i],"in the list is ",count)
       counted.append(list1[i])
