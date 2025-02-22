appleprice=210
budget=200
if(appleprice>=budget):
    print("Alex Add 10Kg Apple To the cart")
else:
    print("Alexa,do not add Apples To the cart")


num=int(input())
if(num<0):
    print("Number to negative")
elif(num>1 and num<=10):
    print("Number is between 1-10")
elif(num>10 and num<=20):
    print("Number is between 11-20")
else:
    print("NUmber is greater than 20")
