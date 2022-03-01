print("Enter The Details: ")
print("------------------------------------------------------")
print("\n")
name=input("Enter The Name: ")
rollno=int(input("Enter the Roll No: "))
enrollmentno=int(input("Enter The Enrollmentno: "))
sem=int(input("Enter the Sem: "))
year=int(input("Enter The Year Of Study: "))
mothername=input("Enter The Mothername: ")
date=input("Enter The Date: ")
month=input("Enter The Month: ")
year=input("Enter The Year: ")



from ast import MatchSequence


print("------------------------------------------------------")
print("Obtained Theory Marks")
print("\n")


while True:
    tsub1=int(input("Enter The Marks In Physics: "))
    if tsub1<=80 and tsub1>=0:
        print(tsub1)
        break
    else:
        print("Enter The Marks OF Physics: ")

while True:
    tsub2=int(input("Enter The Marks In Chemistry: "))
    if tsub2<=80 and tsub2>=0:
        print(tsub2)
        break
    else:
        print("Enter The Marks OF Chemistry: ")

while True:
    tsub3=int(input("Enter The Marks In Maths: "))
    if tsub3<=80 and tsub3>=0:
        print(tsub3)
        break
    else:
        print("Enter The Marks OF Maths: ")

while True:
    tsub4=int(input("Enter The Marks In BEE: "))
    if tsub4<=80 and tsub4>=0:
        print(tsub4)
        break
    else:
        print("Enter The Marks OF BEE: ")

while True:
    tsub5=int(input("Enter The Marks In EG: "))
    if tsub5<=80 and tsub5>=0:
        print(tsub5)
        break
    else:
        print("Enter The Marks OF EG: ")

while True:
    tsub6=int(input("Enter The Marks In CE: "))
    if tsub6<=80 and tsub6>=0:
        print(tsub6)
        break
    else:
        print("Enter The Marks OF CE: ")



print("------------------------------------------------------")
print("Obtained Assignment Marks")
print("\n")


while True:
    asub1=int(input("Enter The Assignment Marks In Physics: "))
    if asub1<=20 and asub1>=0:
        print(asub1)
        break
    else:
        print("Enter The Assignment Marks OF Physics: ")

while True:
    asub2=int(input("Enter The Assignment Marks In Chemistry: "))
    if asub2<=20 and asub2>=0:
        print(asub2)
        break
    else:
        print("Enter The Assignment Marks OF Chemistry: ")

while True:
    asub3=int(input("Enter The Assignment Marks In Maths: "))
    if asub3<=20 and asub3>=0:
        print(asub3)
        break
    else:
        print("Enter The Assignment Marks OF Maths: ")

while True:
    asub4=int(input("Enter The Assignment Marks In BEE: "))
    if asub4<=20 and asub4>=0:
        print(asub4)
        break
    else:
        print("Enter The Assignment Marks OF BEE: ")

while True:
    asub5=int(input("Enter The Assignment Marks In EG: "))
    if asub5<=20 and asub5>=0:
        print(asub5)
        break
    else:
        print("Enter The Assignment Marks OF EG: ")

while True:
    asub6=int(input("Enter The Assignment Marks In CE: "))
    if asub6<=20 and asub6>=0:
        print(asub6)
        break
    else:
        print("Enter The Assignment Marks OF CE: ")


print("------------------------------------------------------")
print("Obtained Practical Marks")
print("\n")


while True:
    psub1=int(input("Enter The Practical Marks In Physics: "))
    if psub1<=50 and psub1>=0:
        print(psub1)
        break
    else:
        print("Enter The Practical Marks OF Physics: ")

while True:
    psub2=int(input("Enter The Practical Marks In Chemistry: "))
    if psub2<=50 and psub2>=0:
        print(psub2)
        break
    else:
        print("Enter The Practical Marks OF Chemistry: ")

while True:
    psub3=int(input("Enter The Practical Marks In BEE: "))
    if psub3<=50 and psub3>=0:
        print(psub3)
        break
    else:
        print("Enter The Practical Marks OF BEE: ")

while True:
    psub4=int(input("Enter The Practical Marks In EG: "))
    if psub4<=50 and psub4>=0:
        print(psub4)
        break
    else:
        print("Enter The Practical Marks OF EG: ")


print("------------------------------------------------------")
print("Assignment Percentage")
print("\n")
totalt=tsub1+tsub2+tsub3+tsub4+tsub5+tsub6
average=totalt/6
percentage=(totalt/600)*100
print ("\nThe Total Marks Are : \t", totalt,"/600")
print ("\nThe Percentage Is :  \t", percentage,"%")

print("------------------------------------------------------")
print("Theory Percentage")
print("\n")
totala=asub1+asub2+asub3+asub4+asub5+asub6
average=totalt/6
percentage=(totalt/120)*100
print ("\nThe Total Marks Are : \t", totalt,"/120")
print ("\nThe Percentage Is :  \t", percentage,"%")

print("------------------------------------------------------")
print("Practical Percentage")
print("\n")
totalp=psub1+psub2+psub3+psub4
average=totalt/4
percentage=(totalt/200)*100
print ("\nThe Total Marks Are : \t", totalt,"/200")
print ("\nThe Percentage Is :  \t", percentage,"%")

print("------------------------------------------------------")
print("\n")
physics=tsub1+asub1+psub1
print("Physics : ",physics)

chemistry=tsub2+asub2+psub2
print("chemistry : ",chemistry)

maths=tsub3+asub3
print("Maths : ",maths)

bee=tsub4+asub4+psub3
print("BEE : ",bee)

eg=tsub5+asub5+psub4
print("EG : ",eg)

ce=tsub6+asub6
print("CE : ",ce)

print("------------------------------------------------------")
print("\n")
total=physics+chemistry+maths+bee+eg+ce
print("Total", total)

print("------------------------------------------------------")
print("Total Percentage")
print("\n")
average=total/6
percentage=(total/800)*100
print ("\nThe Total Marks Are : \t", total,"/800")
print ("\nThe Percentage Is :  \t", percentage,"%")

print("------------------------------------------------------")
print("\n")
print("Enter Marks Obtained in 6 Subjects: ")
physics = int(input("Physics : "))
chemistry = int(input("Chemistry : "))
maths = int(input("Maths : "))
bee = int(input("Bee : "))
eg = int(input("Eg : "))
ce = int(input("Ce : "))

tot = physics+chemistry+maths+bee+eg+ce
avg = tot/6

if avg>=131 and avg<=150:
    print("Your Grade is A")
elif avg>=111 and avg<131:
    print("Your Grade is B")
elif avg>=91 and avg<111:
    print("Your Grade is C")
elif avg>=71 and avg<91:
    print("Your Grade is D")
elif avg>=51 and avg<71:
    print("Your Grade is E")
elif avg>=31 and avg<51:
    print("Your Grade is F")
elif avg>=11 and avg<31:
    print("Your Grade is G")
elif avg>=0 and avg<11:
    print("Your Grade is H")

else:
    print("Invalid Input!")

print("------------------------------------------------------")
print("\n")
print("Final Result : ")
if physics and psub1>=45:
    if chemistry and psub2>=45:
        if bee and psub3>=45:
            if eg and psub4>=45:
                if maths>=35:
                    if ce>=35:
                        print("Pass")

else:
    print("Fail")