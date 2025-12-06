def factorial(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1

    else:
        result = 1
        for i in range(1,x+1):
            result*=i

        return result


x = int(input("Enter the number :"))
print("The Factorial of ",x,"is",factorial(x))