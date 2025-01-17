L1=[]
x=int(input("Enter 1st List Elements"))
i=1
while(i<=x):
    L1.append (int(input()))
    i+=1
print(L1)


L2=[]
y=int(input("Enter 2nd List Elements"))
i=1
while(i<=y):
    L2.append (int(input()))
    i+=1
print(L2)

L3=sum(L1+L2)
print(L3)
