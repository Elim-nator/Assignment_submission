'''Q10. Read at most 10 names of students and store them into an array of 
char nameOfStudents[10][50]. Sort the array and display them back. Hint: 
Use qsort() method.'''


count = int(input("How many names (max 10)? "))
if count > 10:
    count = 10
names = []
for i in range(count):
    names.append(input(f"Enter name {i+1}: "))

n = len(names)
i = 0
while i < n:
    j = 0
    while j < n - 1 - i:
        if names[j].lower() > names[j+1].lower():
            temp = names[j]
            names[j] = names[j+1]
            names[j+1] = temp
        j += 1
    i += 1

print("Sorted names:")
for nm in names:
    print(nm)
