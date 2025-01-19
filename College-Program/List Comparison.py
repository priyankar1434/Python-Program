print("Welcome To List Comparion Program")
#List 1st
l1=[]
x=int(input("How Many Elements in the List 1:"))
i=1
while(i<=x):
    l1.append(input("Enter Elemenst For 1st List"))
    i+=1
print("Your Given List is :",l1)
#List 2nd...
l2=[]
y=int(input("How Many Elements in the List 2:"))
i=1
while(i<=y):
    l2.append(input("Enter Elemenst For 2nd List"))
    i+=1
print("Your Given List is :",l2)

print("Choose Your Operation Do You Perform")
print("1. Checking Greater than and Equal to List")
print("2. Checking Smaller than and Equal to Lsit")
print("3. Checking Equal TO List")
n=int(input("Enter The Number For Performing The Operation"))
i=1
while(i<=n):
    i+=1
    if n==1:
        print(l1>=l2)
        break
    elif n==2:
        print(l1<=l2)
        break
    elif n==3:
        print(l1==l2)
        break
    else:
        print("Try Again")
    
print("Thankyou For using me")
