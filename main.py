def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    choice = input("Enter operation: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '+':
        print("Result:", add(a, b))
    elif choice == '-':
        print("Result:", subtract(a, b))
    elif choice == '*':
        print("Result:", multiply(a, b))
    elif choice == '/':
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()
