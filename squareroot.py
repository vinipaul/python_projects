#to find square root of a number
def find_squareroot(number):
    i=1
    global result
    result=0
    while(i<=number/i):
        if i==number/i and number%i==0:
            result=int(number/i)
            return result
        else:
             out=number/i
             average=(out+i)/2
             result=abs(average)
        i=i+1
    return abs(result)
thenumber=int(input("Enter the number: "))
root=find_squareroot(thenumber)
print(f"squre root of {thenumber} is {root}")
