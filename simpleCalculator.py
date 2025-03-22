# Get user input for two numbers and operations to be performed on them.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Chose which operation to perform between addition(+), subtraction(-), multiplication(*) or division(/): ")

# Perform the operation based on user input
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:  # Check to prevent division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")