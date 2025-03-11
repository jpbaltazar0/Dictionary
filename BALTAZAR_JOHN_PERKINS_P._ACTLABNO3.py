def check_number(num):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

check_number(4) 
check_number(7) 
check_number(-2) 
check_number(-5) 
check_number(0) 

while True:
	num = int(input("Enter your number: "))
	
	if num % 2 == 0:
		print(f"{num} is an even number")
	else:
		print(f"{num} is an odd number")