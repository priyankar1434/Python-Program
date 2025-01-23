print("--Set Object--")
s1=set()
x=int(input("How Many Elements : "))
i=0
while(i<x):
    s1.add(int(input("Enter Your Elements: ")))
    i+=1
print("Your 1st Set Objects are : ",s1)
s1.remove(int(input("Enter Your Elements Do You Want To Delete: ")))
print("Left Elements are : ",s1)

s2=set()
y=int(input("How Many Elements: "))
i=0
while(i<y):
    s2.add(int(input("Enter Your Elements: ")))
    i+=1
print("Your 2nd Set Objects are : ",s2)
s3=s2.issubset(s1)
print(s3)
    
