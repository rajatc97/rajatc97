s1=int(input())
s2=int(input())
s3=int(input())
if s1==s2 and s1==s3:
    print("Equilatral")
elif s1!=s2 and s1!=s3 and s2!=s3:
    print("Scalane")
else:
    print("Isoceles")