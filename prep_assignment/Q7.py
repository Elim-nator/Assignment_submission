#Q7. Write a java program to accept a number from user using command line argument and display its table.

n = int(input("Enter a number: "))
print("Table of", n)
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
