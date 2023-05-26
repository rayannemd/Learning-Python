operator = input("Insira um operador (+ - * /): ")
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number:")

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result == num1 / num2
    print(round(result, 3))
else :
    print(f"{operator} nao e um operador valido")
