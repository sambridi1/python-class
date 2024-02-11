grades={
    "praj":90,
    "prabhat":80,
    "keshav":70,
    "abhinab":40,
    "nidhi":45,
    "sameer":75
}

# new_dict={}
# for key,value in grades.items():
#     if value>70:
#         new_dict[key]=value
# print(new_dict)

# new_dict={}
# new_dict={key:value for key,value in grades.items() if value>70}
# print(new_dict)

new2_dict={}
new2_dict={key:value for key,value in grades.items() if key[0]=="p"}
print(new2_dict)



new3_dict={}
new3_dict={key:value/2 for key,value in grades.items() if value>70}
print(new3_dict)

# new4_dict={}

# for key,value in new3_dict.items():
#     if value>70:
#         value=value/2
#         new4_dict[key]=value
# print(new4_dict)







#making odd marks even and even marks odd and printing
# even_dict={}
# odd_dict={}
# for key,value in grades.items():
#     if value%2==0:
#         value+=1
#         odd_dict[key]=value
#     else:
#         value+=1
#         even_dict[key]=value
# print(odd_dict)
# print(even_dict)