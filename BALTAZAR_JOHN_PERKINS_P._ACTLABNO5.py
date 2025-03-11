while True:
    age = int(input("Enter your age (or type -1 to exit): "))
    
    if age == -1:
        print("Goodbye!")
        break
    elif age >= 65:
        print("SENIOR!")
    elif age == 64:
        print("ADULT!")
    elif age >= 20:
        print("ADULT")
    elif age == 19:
        print("TEEN!")
    elif age >= 13:
        print("TEEN!")
    elif age == 12:
        print("CHILD!")
    elif age >= 0:
        print("CHILD!")
    else:
        print("You haven't been born yet!")