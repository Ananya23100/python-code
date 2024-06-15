list1=[]
sum=0
while(1):
    b=input("enter a number.To stop the program enter'Quit'")
    if b=='Quit':
        break
    list1.append(b)
    sum = sum+int(b)

print("the list you enterd is",list1)
print("the sum of the numbers in the list is ",sum)
