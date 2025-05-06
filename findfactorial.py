#recursive function example
#factorial of a number
def factorial(number):
    if number==1:
        return number
    else:
        fact=number*factorial(number-1)
        return fact
inputnumber=input("enter the number:")
result=factorial(int(inputnumber))
print("factorial of ",inputnumber,"is ",result)
