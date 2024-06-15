n=int (input ("enter the number till which you want to print fibonacci series"))
if n<=0:
    fib_series=[]
elif n==1:
    fib_series = [0]
elif n==2:
    fib_series = [0,1]
else:
    fib_series = [0,1]
    for i in range(2,n):
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
print("the requires sequence is ",fib_series)
