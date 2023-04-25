a=int(input("enter a year:"))
if a%4==0 and a%100 !=0:
    print("it is a leap year")
elif a%4==0 and a%100==0 and a%400!=0:
    print("it is not leap year")
elif a%4==0 and a%100==0 and a%400==0:
    print("it is an leap year")
else:
    print("it is not a leap  year")

