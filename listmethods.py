fruits=["apple","banana","cherry","orange"]
print("banana" in fruits)
l1=fruits[-4:-1:2] 
l2=l1[::-1]
print("list1 ",l1)
print("list2 ",l2)
l3=list(reversed(fruits))
print("list 3",l3)
fruits.insert(2,"banana")
print(fruits)
fruits.append("watermelon")
print("appended list:",fruits)
num_list1=[10,20,30,40]
num_list2=[50,60,70,80]
num_list1.extend(num_list2)
print("after extends:",num_list1)
num_list1.remove(50)
print("after remove:",num_list1)
num_list1.pop()
print("after pop:",num_list1)
# fruits.clear()
# print("clearing the list: ",fruits)
print("the original list: ",fruits)
print("fruits list using for loop:")
for x in fruits:
    print(x)
print("fruits list using while loop:")
i=0
while(i<len(fruits)):
    print(fruits[i])
    i=i+1
print("fruits list using list comprehension: ")
new_list=[x for x in fruits if "a" in x ]
print(new_list)
fruits.sort()
print("after sorting,ascending order: ",fruits)
fruits.sort(reverse=True)
print("After sorting descending order:",fruits)
print("reversed fruits list: ")
fruits.reverse()
print(fruits)
fruits_copy=fruits.copy()
fruits.append("mango")
print("fruit_list: ",fruits)
print("fruit copy list: ",fruits_copy)






      