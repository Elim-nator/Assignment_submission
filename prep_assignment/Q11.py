'''Q11. Create a structure called Employee that includes three fields - a first 
name (type String), a last name (type String) and a monthly salary (double). 
Write functions to initialize the fields, print them and modify the values in 
the given object. Example methods:
 void emp_init(struct emp* e); 
 void set_salary(struct emp *e, double sal);
 void emp_display(struct emp *e);
Write the test code in the main(). Create two emp objects and display each 
object’s yearly salary. Then give each Employee a 10% raise and display 
each Employee’s yearly salary again.'''



class Employee:
    def __init__(self, first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = monthly_salary

    def set_salary(self, sal):
        self.monthly_salary = sal

    def yearly_salary(self):
        return self.monthly_salary * 12

    def emp_display(self):
        print("Employee:", self.first_name, self.last_name)
        print("Monthly Salary:", self.monthly_salary)
        print("Yearly Salary:", self.yearly_salary())

def emp_init():
    fn = input("First name: ")
    ln = input("Last name: ")
    sal = float(input("Monthly salary: "))
    return Employee(fn, ln, sal)

print("Enter Employee 1:")
e1 = emp_init()
print("Enter Employee 2:")
e2 = emp_init()

print("\nBefore raise:")
e1.emp_display()
e2.emp_display()

e1.set_salary(e1.monthly_salary * 1.10)
e2.set_salary(e2.monthly_salary * 1.10)

print("\nAfter 10% raise:")
e1.emp_display()
e2.emp_display()
