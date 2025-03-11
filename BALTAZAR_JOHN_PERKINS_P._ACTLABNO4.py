while True:
    score = int(input("Enter your score : "))
    
    if score <= -1:
    	print("Error retype your score!")
    elif score > 100:
        print("Invalid score!")
    elif score == 0:
    	print("Invalid score!")
    elif score == 100 :
        print("You got [A] EXELENT!")
    elif score >= 90:
        print("You got [A] EXELENT!")
    elif score == 89 :
        print("You got [B] WELL DONE")
    elif score >= 80:
        print("You got [B] WELL DONE!")
    elif score == 79:
        print("You got [C] CONGRATS!")
    elif score >= 70:
        print("You got [C] CONGRATS!")
    elif score == 69:
        print("You got [D] NEED IMPROVEMENT!")
    elif score >= 60:
    	print("You got [D] NEED IMPROVEMENT!")
    elif score <= 59:
    	print("You got [F] FAIL")
    else:
        print("Error retype your score!")