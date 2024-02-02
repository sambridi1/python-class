A=[1,2,3,5,56,6,7,7,77,7,5,4,4,3,2,2,2]
temp_value=A[0]
for element in A:
    if element > temp_value:
        temp_value = element
        max_value=temp_value
print(max_value)