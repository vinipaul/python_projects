def addition():
    num1=input("enter number 1:")
    num2=input("enter number 2:")
    ans=int(num2)+int(num1)
    print(type(num2))
    return ans

def factorial():
    number=int(input("enter the number:"))
    print(type(number))
    if number==1:
        ans=1
        return ans
    else:
        number=number*(number-1)
        return number
def factorial(fact):
    if fact==1:
        return fact
    else:
            fact=fact*factorial(fact-1)
            print(f"{fact}!={fact}*{(fact-1)}!")
    return fact
# ans=addition()
number=int(input("enter the number:"))
ans=factorial(number)
print(ans)