sub1=int(input("Enter the marks of subject1"))
sub2=int(input("Enter the marks of subject2"))
sub3=int(input("Enter the marks of subject3"))
sub4=int(input("Enter the marks of subject4"))
sub5=int(input("Enter the marks of subject5"))
total=sub1+sub2+sub3+sub4+sub5/5
per=float(total)*(100/500)
print("Percentage",per)
if per>=60:
    print("Student pass the exam in first class")
elif per>=75:
    print("Student pass the exam with distinction")
else:
    print("Student fail in examination.")