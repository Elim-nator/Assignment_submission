calls = int(input("Enter the number of calls: "))
bill = 200
bill1 = bill + ((calls-100)*0.60)
bill2 = bill1 +((calls-150)*0.50)
bill3 =  bill2 +((calls-200)*0.40)
if calls<=100:
    print(f"Your bill is now {bill}")
elif calls>100 and calls<=150:
    print(f"Your bill is now {bill1}")
elif calls>150 and calls<=200:
    print(f"Your bill is now {bill2}")
elif calls>200 and calls<=400:
    print(f"Your bill is now {bill3}")
else :
    print("Sorry, your call limit is expired")