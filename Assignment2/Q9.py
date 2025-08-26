#RETURN THE SIMPLE INTEREST


p =int(input("Enter the value of p :"))
r =float(input("Enter the value of r :"))
t =float(input("Enter the value of t :"))

def simplefun(p,r,t):
    si = (p*r*t)/100
    print(f"Your simple interest is {si}")


simplefun(p,r,t)