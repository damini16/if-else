salary=int(input("Enter the salary of employee"))
year=int(input("Enter the working year of employee"))
if year>=5:
    count=salary*10/100
    bounus=salary+count
    print("The employee work more than 5 year so employee is  eligible for bonus")
    print("Basic Salary:",salary ,"\nSalary with Bonus:",bounus )
else:
    print("The employee not work more than 5 year so the employee not eligible for bonus.")