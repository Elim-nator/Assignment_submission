subj1 = int(input("Enter the first marks: "))
subj2 = int(input("Enter the second marks: "))
subj3 = int(input("Enter the third marks: "))

avg= (subj1+subj2+subj3)/3

print("Grade system")

if avg>=90 and avg<=100:
    print("avg>=90 and avg<=100 Therefore\ngrade A")
elif avg>=80 and avg<=90:
    print("avg>=80 and avg<=90 Therefore\ngrade B")
elif avg>=70 and avg<=80:
    print("avg>=70 and avg<=80 Therefore\ngrade C")
elif avg>=60 and avg<=70:
    print("avg>=60 and avg<=70 Therefore\ngrade D")
else :
    print("avg>=0 and avg<=60 Therefore\ngrade F")