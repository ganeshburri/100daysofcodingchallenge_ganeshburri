def division():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try:
        result = int(num1) / int(num2)
        print("The result is", result)
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except ValueError:
        print("You must enter a number!")
choice = input("Do you want to divide two numbers? (yes/no): ")
while choice == "yes":
    division()
    choice = input("Do you want to divide two numbers? (yes/no): ")
print("exiting...")