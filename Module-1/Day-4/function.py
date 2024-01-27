def check_prime(a):
    # a= int(input("enter a  number"))
    c=0
    for i in range(1, a+1):
        if(a%i==0):
            c=c+1
            if(c==2):
                return True
            else:
                return False
        else:
            return True
        

       
       
number=int (input("enter a number to check prime or not"))
value_of_check_prime=check_prime(number)
if value_of_check_prime==True:
     print("number is prime")
else:
     print("number isnt prime")    