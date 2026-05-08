#Calculator

num1 = float(input("Enter your first number: "))
operator = input("Enter your operator: ")
num2 = float(input("Enter your second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if(num2 > 0):
        print(num1 / num2)
    else:
        print("Division cannot be done using zero")
else:
    print("Invalid")

