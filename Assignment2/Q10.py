p =float(input("Enter the value of p (Principal amount) :"))
r =float(input("Enter the value of r(Rate of interest) :"))

n =float(input("Enter the value of n(No of times interest compounds in year) :"))
t =float(input("Enter the value of t(Time in years) :"))

def compoundfun(p,r,n,t):

    ci = p * ((1 + (r/n)) ** (n * t))   
    print(f"Your compound interest is {ci}")


compoundfun(p,r,n,t)