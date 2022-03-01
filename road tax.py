cp=int(input("enter the cost price :"))
if cp<100000:
    print("the road tax is : ",15/100*cp)
elif cp<=100000 and cp>50000:
    print("the road tax is : ",10/100*cp)
else :
    print("the road tax is : ",5/100*cp)
