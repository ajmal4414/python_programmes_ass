# 7.year is leapyear or not

year=int(input("enter a year"))

if (year%400 ==0)and (year%100==0):
    print(year,"is a leapyear")

elif(year%4==0) and (year%100!=0):
    print(year,"is leap year")
else:
    print(year,"is not a leap year")
