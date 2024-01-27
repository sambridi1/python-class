def leap_year(year):
    if (year%4==0) and (year % 100 != 0 or year % 400 == 0):
        print("its a leap year")
    else:
        print("its not a leap year")

find=int (input("enter a year"))
leap_year(find)