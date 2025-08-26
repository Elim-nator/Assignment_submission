#Q14 Write a java code to check if string is palindrome.

s = input("Enter a string: ")
left = 0
right = len(s) - 1
pal = True
while left < right:
    if s[left] != s[right]:
        pal = False
        break
    left += 1
    right -= 1

if pal:
    print("Palindrome")
else:
    print("Not Palindrome")
