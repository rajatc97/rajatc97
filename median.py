v1=input()
v2=input()
v3=input()

a1=[v1,v2,v3]
a1.remove(max(a1))
a1.remove(min(a1))

print(a1[0])