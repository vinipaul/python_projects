"""x=str(5) #casting
y=int(9.5)
print (x)
print (y)
print (type(x)) #to know variable  value type
print(type(y))"""

"""x=y=z=10
print ("the value of " ,z)"""

"""my_name_is_vini="vini"
print ("My name is ",my_name_is_vini)"""

"""fruits=["banana" ,"appale" ,"oarange"]
x,y,z=fruits
print (x)
print (y) 
print (z) """

#output variables
"""x="5"
y="vini"
print(x + " "+y ) #or print(x, y)"""

x=5
def fun1():
     x=2
     y=8
     global var
     var=10
     print(x+y)
     print("local x",x)
     print(x)
def fun2():
    x="vini"
    y="paul"
    print(x+y)
    print("local x",x)
fun1()
fun2()
print("x is global here",x,var)



