# calculator.py — Simple CLI Calculator

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Cannot divide by zero!" if b == 0 else a / b

def main():
    print("Simple Calculator")
    while True:
        print("\nChoose operation: +  -  *  /  or 'exit'")
        choice = input("Enter your choice: ")

        if choice.lower() == 'exit':
            print("Exiting Calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

        if choice in operations:
            print(f"Result: {operations[choice](num1, num2)}")
        else:
            print(" Invalid operation! Try again.")

if __name__ == "__main__":
    main()
