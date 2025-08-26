'''Q12. Write a Program to reverse the letters present in the given String. Do 
not use strrev() function'''

s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)
