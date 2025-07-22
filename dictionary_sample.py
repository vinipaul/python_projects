my_dict = {"name": "Alice", "age": 30, "city": "Dubai"}
temps=my_dict.items()
print(temps)
a1=my_dict.keys()
print(a1)
a2=my_dict.values()
print(a2)
result=[dict(zip(my_dict.keys(),my_dict.values()))]
print(result)
input=[
    {
        "address": "kochi",
        "created_at": "Thu, 05 Oct 2000 00:00:00 GMT",
        "customer_id": 2,
        "email": "divyapaulp@gmail.com",
        "name": "divya",
        "phone": "5757"
    }
]
b1=input[0]
print(b1)
print(b1['address'])
