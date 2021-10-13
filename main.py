x = int(input("Enter value #1: "))
y = int(input("Enter value #2: "))

operation = input("Choose arithmetic operation (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Invalid operation!")