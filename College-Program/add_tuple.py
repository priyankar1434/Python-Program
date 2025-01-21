l1=[]
x=int(input("How Many Elements: "))
i=0
while(i<x):
    y=int(input("Enter Your Elements"))
    l1.append(y)
    i+=1
print(tuple(l1))

l2=[]
i=0
while(i<x):
    b=int(input("Enter Your Elements:"))
    l2.append(b)
    i+=1
l3=[]
i=0
while(i<x):
    l3.append(l1[i]+l2[i])
    i+=1
print(tuple(l3))

