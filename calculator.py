# CALCULATOR

opertor = input("Enter operator(+,-,*,/): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if opertor == "+":
    print("result:",num1+num2)
elif opertor == "-":
    print("result:",num1-num2)                                                
elif opertor == "*":
    print("result:",num1*num2)
elif opertor == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("result:",num1/num2)
else:  
    print("Invalid operator")