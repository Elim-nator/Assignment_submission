#Q1. Write a program to input n numbers on command line argument and calculate maximum of them.

n = int(input("How many numbers? "))
if n <= 0:
    print("No numbers entered.")
else:
    first = float(input("Enter number 1: "))
    max_val = first
    for i in range(2, n + 1):
        x = float(input(f"Enter number {i}: "))
        if x > max_val:
            max_val = x
    print("Maximum is:", max_val)
