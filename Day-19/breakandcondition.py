print("Table Printing")
for i in range(10):
    if(i==10):
        break
    print("9 X",i+1,"=",9*(i+1))
for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5X",i,"=",5*1)
print("True False Statement:")
i=0
while True:
    print(i)
    i=i+1
    if(i%10==0):
        break
