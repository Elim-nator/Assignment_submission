'''Q5. Write a program to check the input characters for uppercase, 
lowercase, number of digits and other characters. Display appropriate 
message.'''

s = input("Enter text: ")
upper = 0
lower = 0
digits = 0
others = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
    elif '0' <= ch <= '9':
        digits += 1
    else:
        others += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Others:", others)
