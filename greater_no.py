num_1=int(input("Enter the number"))
num_2=int(input("Enter the number"))
num_3=int(input("Enter the number"))
if num_1>=num_2 and num_1>=num_3:
    print("Largest number",num_1)
elif num_2>=num_1 and num_2>=num_3:
    print("Largest number",num_2)
elif num_3>=num_1 and num_3>=num_2:
    print("Largest number",num_3)
else:
    print("It is Edual")

    