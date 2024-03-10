# f_x=lambda x: x**2+5*x+3
# five=f_x(5)
# print(five)
# f_x=lambda x,y: x**2+5*x*y+3
# fivee=f_x(5,3)
# print(fivee)

def func_x(x):
    y=x**2+5*x+3
    return y

numbers=[1,2,3,4,5,6,7,8,9,10]

num=[]
for i in numbers:
    num=func_x(i)
    print(num)

#using list comprehension
y=[func_x(x) for x in numbers]
print(y)