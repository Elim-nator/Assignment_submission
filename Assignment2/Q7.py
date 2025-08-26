quantity = int(input("Enter the quantity you are purchasing :"))
price =quantity*5

if quantity<30:
    print(f"Your total price is :{price}")
elif quantity<30:
    print(f"Your total price is :{price-(price*0.10)}")
elif quantity<50:
    print(f"Your total price is :{price-(price*0.15)}")
