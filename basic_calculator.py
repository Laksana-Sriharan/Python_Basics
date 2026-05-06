number1 = input("Enter your first number: ")
number2 = input("Enter your second number: ")

#Input gained from the user will be treated as string, so change typecast them
result1 = float(number1) + float(number2)
print("The sum is: ", result1)

result2 = float(number1) - float(number2)
print("The difference is: ", result2)

result3 = float(number1) * float(number2)
print("The product is: ", result3)

result4 = float(number1) / float(number2)
print("The division is: ", result4)
