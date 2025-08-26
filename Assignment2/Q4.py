year = int(input("Enter the YEAR: "))

if year % 4==0:
    print(f"The given year {year} is a leap year.")
elif year % 100 ==0 and year % 400 ==0:
    print(f"The given year {year} is a leap year.")
else :
    print(f"The given year {year} is a leap year.")
