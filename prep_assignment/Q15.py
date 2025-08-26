'''Q15. Input a string from the user. Count occurrences (case insensitive) of 
each alphabet in the string.
Sample output: 
Input: Welcome to SunBeam.
Output:
A : 1
B : 1
C : 1
E : 3
L : 1
M : 2
N : 1
O : 2
S : 1
T : 1
U : 1
W : 1'''


text = input("Enter text: ")
text = text.upper()

counts = {}
for ch in text:
    if 'A' <= ch <= 'Z':
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

letters = list(counts.keys())
i = 0
while i < len(letters):
    min_idx = i
    j = i + 1
    while j < len(letters):
        if letters[j] < letters[min_idx]:
            min_idx = j
        j += 1
    if min_idx != i:
        letters[i], letters[min_idx] = letters[min_idx], letters[i]
    i += 1

for k in letters:
    print(f"{k} : {counts[k]}")
