import math

# ==========================
# Calculator Functions
# ==========================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b


def floor_division(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a // b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(a)


# ==========================
# Main Program
# ==========================

while True:

    print("\n====================================")
    print("      PYTHON CALCULATOR")
    print("====================================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Power")
    print("8. Square Root")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    try:

        if choice == "8":

            number = float(input("Enter number: "))

            print("Result =", square_root(number))

        elif choice == "9":

            print("Thank you for using the calculator.")
            break

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Answer =", add(num1, num2))

            elif choice == "2":
                print("Answer =", subtract(num1, num2))

            elif choice == "3":
                print("Answer =", multiply(num1, num2))

            elif choice == "4":
                print("Answer =", divide(num1, num2))

            elif choice == "5":
                print("Answer =", modulus(num1, num2))

            elif choice == "6":
                print("Answer =", floor_division(num1, num2))

            elif choice == "7":
                print("Answer =", power(num1, num2))

        else:
            print("Invalid menu choice.")

    except ValueError:
        print("Please enter valid numbers.")