'''Q9. Accept an integer number and when the program is executed print the 
binary, octal and hexadecimal equivalent of the given number.
Sample Output:
terminal> java Test
Enter Number : 20
Given Number :20
Binary equivalent :10100
Octal equivalent :24
Hexadecimal equivalent :14'''

'''Hint: Use bitwise operators for binary conversion. Octal/Hexadecimal 
conversion to be done by repetitive division using recursion.'''

def to_binary_bitwise(n):
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        last_bit = n & 1
        bits = str(last_bit) + bits
        n = n >> 1
    return bits

def to_octal_recursive(n):
    if n < 8:
        return str(n)
    return to_octal_recursive(n // 8) + str(n % 8)

def to_hex_recursive(n):
    hexchars = "0123456789ABCDEF"
    if n < 16:
        return hexchars[n]
    return to_hex_recursive(n // 16) + hexchars[n % 16]

num = int(input("Enter Number: "))
print("Given Number:", num)
print("Binary equivalent:", to_binary_bitwise(num))
print("Octal equivalent:", to_octal_recursive(num))
print("Hexadecimal equivalent:", to_hex_recursive(num))
