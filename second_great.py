#Find the second gretest number 
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
num3=int(input("Enter the number"))
if num1>=num2 and num1>=num3:
    if num2>=num3:
        print(num2)
    else:
        print(num3)
elif num2>=num1 and num2>=num3:
    if num1>=num3:
        print(num1)
    else:
        print(num3)
elif num1>=num2:
    print(num1)
else:
    print(num2)
