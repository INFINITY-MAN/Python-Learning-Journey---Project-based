##Calculator Version 1.0
print("Welcome to the Calculator!")
print("This calculator can perform basic arithmetic operations.")
x=15
while(x!= 90):
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus- Remainder")
    print("6. Exit") 
    choice=input("Enter your choice (1/2/3/4/5) or just text base it like addition: ")
    #print(str(a) + " " + choice + " " + str(b))
    if choice == "1" or choice.lower() == "addition":
        print(str(a) + " " + "+" + " " + str(b) + " = ", end="")
        print("Result: ", a + b)
    elif choice == "2" or choice.lower() == "subtraction":
        print(str(a) + " " + "-" + " " + str(b) + " = ", end="")
        print("Result: ", a - b)
    elif choice == "3" or choice.lower() == "multiplication":
        print(str(a) + " " + "*" + " " + str(b) + " = ", end="")
        print("Result: ", a * b)
    elif choice == "4" or choice.lower() == "division":
        if b != 0:
            print(str(a) + " " + "/" + " " + str(b) + " = ", end="")
            print("Result: ", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == "5" or choice.lower() == "modulus" or choice.lower() == "remainder":
        if b != 0:
            print(str(a) + " " + "%" + " " + str(b) + " = ", end="")
            print("Result: ", a % b)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice.lower() == "exit":
        print("Exiting the calculator. Goodbye!")
        x=90
    