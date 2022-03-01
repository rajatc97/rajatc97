#Addition of two
def add(a,b):
    print(a+b)

num1=5
num2=5
add(num1,num2)

#Substraction of two
def sub(a,b):
    print(a-b)

num1=5
num2=3
sub(num1,num2)

#Sum of (A+B)2
def sumab(a,b):
    print(a**2+b**2+2*a*b)

num1=3
num2=5
sumab(num1,num2)

#Sum of (A-B)2
def subab(a,b):
    print(a**2+b**2-2*a*b)

num1=3
num2=5
subab(num1,num2)

#Area of rectangle
def arectangle(l,w):
    print(l*w)

num1=3
num2=5
arectangle(num1,num2)

#Area of square
def asquare(a):
    print(a*a)

num1=3
asquare(num1)

#Area of triangle
def atriangle(b,h):
    print(0.5*b*h)

num1=3
num2=5
atriangle(num1,num2)

#Celcious to fahrenheit
def ctof(celsius):
    print(1.8*celsius+32)

num1=3
ctof(num1)

#Divison of two
def div(a,b):
    print(a//b)

num1=10
num2=5
div(num1,num2)

#Km To meter
def kmtom(kilometers):
    print(kilometers*1000)

num1=5
kmtom(num1)

#Multiplication
def mul(a,b,c):
    print(a*b*c)

num1=3
num2=5
num3=8
mul(num1,num2,num3)

#Simple intrest
def si(p,r,t):
    print((p*r*t)/100)

num1=3
num2=5
num3=7
si(num1,num2,num3)

#Swaping of two
def swap():
    x=int(input("Enter the value a : "))
    y=int(input("Enter the value b : "))
    print("Before swapping a : ",x)
    print("Before swapping b : ",y)
    x,y=y,x 
    print("After swapping a : ",x)
    print("After swapping b : ",y)

swap()

#Swapping of two using third
def swaptwo():
    x=int(input("Enter the value c : "))
    y=int(input("Enter the value d : "))
    print("Before swapping c : ",x)
    print("Before swapping d : ",y)
    temp=x
    x,y=y,x
    y=temp
    print("After swapping c : ",x)
    print("After swapping d : ",y)

swaptwo()