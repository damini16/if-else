year=int(input("Enter the Year"))
if year%4==0 and year%100==0:
    print("Leap year")

elif year%100!=0:
    print("Its not Leap year")

elif year%400:
    print("Leap year")

else:
    print("It not leap year")