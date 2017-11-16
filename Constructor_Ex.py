class Employee:

    def __init__(self, name, salary):   #Declaring variables through a constructor.
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee name is:", self.name)
        print("Employees Salary is:", self.salary)


emp = Employee("ABC", 3254324)
emp2 = Employee("DEF", 123456789)
emp.display()
emp2.display()


