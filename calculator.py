


num1 = float(input("enter the 1st number: "))

operador = input("Enter an operator (+ - * /):")

num2 = float(input("enter the 2st number: "))

print(f"{num1} {operador} {num2}")

if operador == "+":
    result = num1 + num2
    print(round(result,3))
elif operador == "-":
    result = num1 - num2
    print(round(result,3))
elif operador == "*":
    result = num1 * num2
    print(round(result,3))
elif operador == "/":
    result = num1/num2
    print(round(result,3))
else:
    print(f"{operador} is not valid operator")    

     
