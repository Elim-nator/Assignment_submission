'''Q13. Declare an Array of type char* and initialize it with a few strings (hardcoded). Display the strings which are duplicated in that array. (Hint: use 
strcmp())'''


arr = ["apple", "banana", "apple", "cherry", "banana", "date", "egg", "fig", "fig"]
dups = []

i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr):
        if arr[i] == arr[j]:
            if arr[i] not in dups:
                dups.append(arr[i])
        j += 1
    i += 1

print("Duplicated strings:")
for w in dups:
    print(w)
