#Q2. Write a program to calculate a Factorial of a number.

n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    print("Factorial of", n, "is", fact)
