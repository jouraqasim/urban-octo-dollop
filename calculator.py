num1 =int(input("Enter the value1:"))
opr = (input("Enter the operator.."))
num2 =int(input("Enter the value2:"))

if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
    
else:
    print("Syntax Error") 
