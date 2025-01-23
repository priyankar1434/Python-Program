s1=set()
x=int(input("How many elements in 1st Object: "))
i=0
while(i<x):
    s1.add(int(input("Enter Your Elements: ")))
    i+=1
print(s1)
s2=set()
y=int(input("How many elements in 2nd Object: "))
i=0
while(i<y):
    s2.add(int(input("Enter Your Elements:")))
    i+=1
print(s2)
s3=s2.union(s1)
s4=s2.intersection(s1)
s5=s3-s4
print("Non Uniqe Elements are: ",s5)


