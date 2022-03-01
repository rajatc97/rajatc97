nou=int(input("enter the no of unit :"))
if nou<100:
    print("no unit charge")
elif nou>=100 and nou<200:
    print("no of unit charge",5/100*nou)
elif nou>=200 and nou<400:
    print("no of unit charge",10/100*nou)
else:
    print("no of unit charge",15/100*nou)
