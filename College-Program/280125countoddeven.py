l1=[]
countodd=0
counteven=0

n=int(input("Enter Elements:"))
i=0
while(i<n):
    y=int(input("Enter Elements"))
    l1.append(y)
    i+=1
l2=tuple(l1)
print(l2)
for x in l2:
    if (x%2==0):
        counteven+=1
    else:
        countodd+=1
print("Even:",counteven)
print("Odd:",countodd)

