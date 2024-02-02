A=[1,2,3,4,5,6,7]
even_list,odd_list =[] , []
for element in A:
    if element % 2 == 0:
        even_list.append(element)
    else:
        odd_list.append(element)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

# imp list comprehensive technique

C=[element+3 for element in A]
print(C)


D=[element for element in A if element%2 ==0]
print(D)

E=[element for element in A if element%2 !=0]
print(E)

Z=[-1,6,-2,3,-4,5]
F=[element for element in Z  if element>0]
G=[element for element in Z if element<=0]
print(F)
print(G)
H=[element for element in sorted(Z)]
print(H)
