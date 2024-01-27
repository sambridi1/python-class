def check_prime(number):
    counter=0
    prime=False
    for i in range(1,number+1):
        if number%i==0:
            counter=counter+1
    if counter==2:
        prime=True
    return prime

def multiplication_table(number):
    for i in range(1,11):
        print(f"{number}*{i}={number*i}")
number=int(input("enter a number"))

if check_prime(number)==True:
    multiplication_table(number)