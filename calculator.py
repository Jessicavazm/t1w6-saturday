# Calculator using IF, ELSE statements

# Get user inputs for numbers and preferred operation

num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, * or /): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:    
        result = "Error, division by Zero"
else:
    result = "Invalid operation, try again"        

print(f"The result is {result}")
