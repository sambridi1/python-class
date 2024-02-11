random_dict={
    1:"one",
    2:"two"

}
print(random_dict)
# print(random_dict[1])
# print(random_dict[2])
# print(random_dict.get(2))
# print(random_dict.get(3))
# print(random_dict.items())
# for key,value in random_dict.items():
#     print(key)
#     print(" ")
#     print(value)

print(random_dict.keys())
for key in random_dict.keys():
    print(key)

for value in random_dict.values():
    print(value)

print(random_dict.pop(1))
print(random_dict)

dict2= {
    "name":"praj",
    "age":20,
    "address":{
          "city":"dahachowk",
          "street":"petrolPump"
    }
  
}
print(dict2.get("address").get("city"))
#or
print(dict2["address"]["street"])