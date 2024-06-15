list1=[]
min=1000000
max=-1000000
while 1:
    a = input("Enter the number .To stop entering,type quit")
    if (a=='quit'):
        break
    num=int(a)
    list1.append(a)
    if num<min:
          min=num
    if num>max:
          max=num
print("minimun of entered values :",min,"and maximum of entered values:",max)

