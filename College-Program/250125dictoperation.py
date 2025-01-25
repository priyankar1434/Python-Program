d1={}
x=int(input("How Many Dict Objects:"))
i=0
while(i<x):
    d2=int(input("Enter Key:"))
    d3=input("Enter Data:")
    d1[d2]=d3
    i+=1
print(type(d1))
s=d1.keys()
for p in s:
    print("Keys are:",p)
o=d1.values()
for q in o:
    print("Data Values are:",q)
l=d1.items()
for r in l:
    print("Items are:",r)


