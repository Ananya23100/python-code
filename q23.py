a= float(input("Enter the temperature"))
b= input("Enter it's unit (C or F)")
if b=='C':
    conv_temp=((9*a)/5)+32
    print("the required temperature in faranheit is ",conv_temp)
elif b =='F':
    conv_temp = (5*(a-32))/9
    print("the required temperature in celsius is  ", conv_temp)
else :
    print("invalid ")


