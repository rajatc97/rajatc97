number=int(input("Enter any number : "))

if((number % 5 == 0) and (number % 15 == 0)):
    print("Given Number {0} is Divisible by 5 and 15".format(number))
elif (number % 11 == 0):
    print("Given Number {0} is Divisible by 11".format(number))
else:
     print("Given Number {0} is Not Divisible by 5 and 11 and 15".format(number))