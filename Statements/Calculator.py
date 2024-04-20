a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
op = input("Enter operator: ")

if op == "+":
    print (a+b)
elif op == "-":
    print (a-b)
elif op == "*":
    print (a*b)
elif op == "/":
    print (a/b)
elif op == "%":
    print (a%b)
elif op == "**":
    print (a**b)
else:
    print("Invalid input")