#Q3. Write a program to calculate Fibonacci Series up to n numbers

n = int(input("How many Fibonacci numbers? "))
a = 0
b = 1
count = 0
series = []
while count < n:
    series.append(a)
    a, b = b, a + b
    count += 1
print("Fibonacci series:", " ".join(str(v) for v in series))
