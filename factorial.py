number=int(input("Enter the number:"))
def factorial(num):
 if num==1:
  return 1
 else:
    return num*factorial(num-1)
result=factorial(number)
print(result)