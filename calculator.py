#Simple Calculator 
#choose number 1-4 from user
choose=int(input("Select the choice"))
num_1=int(input("Enter the  first number"))
num_2=int(input("Enter the second number"))
if choose==1:
    sum=num_1+num_2
    print("Addition of number is",sum)
elif choose==2:
    sub=num_1-num_2
    print("Substraction of number is",sub)
elif choose==3:
    mul=num_1*num_2
    print("Multipilaction of nunber is", mul)
elif choose==4:
    div=num_1/num_2
    print("Dividsion of number is",div)
else:
    print("Wrong input")