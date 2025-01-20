s1=str(input("Enter Your String : "))
s2=s1.lower()
print(s2)
print("Enter The Operation Do You Want To Perform")
print("1.Select For Vowels Operation")
print("2.Select For Upper and Lower Case Operation")
x=int(input("Enter Your Number For Operation Perform : "))
if x==1:
    if(('a' in s2) or ('e' in s2) or ('i' in s2) or ('o' in s2) or ('u' in s2)):
        print("Vowels Present")
    else:
        print("not Contain")
elif x==2:
    print(s2.upper())
    print(s2.lower())
else:
    print("Invalid Option")
