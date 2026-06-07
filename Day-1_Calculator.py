#Calculator
a = int(input("enter num1: "))
b = int(input("enter num2: "))
operation = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, 5 to floor division, 6 to find reminder and 7 to find exponent (a^b): "))
if operation==1:
    print(a+b)
if operation==2:
    if a>=b:
        print(a-b)
    else:
        print(b-a)
if operation==3: 
    print(a*b)
if operation==4:
    print(a/b)
if operation==5: 
    print(a//b)
if operation==6:
    print(a%b)
if operation == 7:
    print(a**b)
if operation > 7 or operation < 1:
    print("Choose accurate operation")
