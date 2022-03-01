q=int(input("Enter Quantity : "))
price=q*100
if price>=1000:
    d=price*0.1
else:
    d=0
total=price-d
print(total)