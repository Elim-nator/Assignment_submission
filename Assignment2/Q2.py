num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


def findmax(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"Num1 {num1} is maximum")
    elif num2>num1 and num2>num3:
        print(f"Num2 {num2} is maximum")
    else :
        print(f"Num3 {num3} is the maximum")

findmax(num1,num2,num3)