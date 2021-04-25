#if number less than 200 and even number is Ringo and greter than 200 and odd then print bingo
#takes input from user
number=int(input("Enter the number"))
#put the conditions
if number<200 and number%2==0:
    print("Ringo")
elif number >200 and number%2!=0:
    print("Bingo")
else:
    print("Invalid inputs")