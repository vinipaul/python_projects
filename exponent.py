#to find exponent of a number
def find_exponent(base,exponent):
    i=1
    result=1
    while(i<=exponent):
        result=result*base
        i=i+1
    print(f"{base}^{exponent} is {result}")
bbase=int(input("Enter the base number: " ))
eexponent=int(input("Enter the exponenet: "))
find_exponent(bbase,eexponent)
