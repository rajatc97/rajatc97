nch=int(input("Enter the number of class held : "))
nca=int(input("Enter the number of class attended : "))
attend=(nca/float(nch))*100
print("Attendance is : ", attend)
if attend>=75:
    print("You are allowed in exam")
else:
    print("Sorry you are not allowed in exam")
