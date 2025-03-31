def factorial(a):
    sum = 1
    i=1
    if(a == 0):
        return 1
    else:
        while(i<=a):
            sum = sum * i
            i+=1
        return sum
    
print(factorial(4))



