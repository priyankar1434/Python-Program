x=int(input("Enter the value of x:"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case 9:
        print("_")
    case _:
        print("default")
