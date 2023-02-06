"""This lesson will be on the topic of inheritance"""

class Employee:
    #This is the parent class
    #All other classes that want to inhert can call it in their declaration
    #this class can be inherited from extended and overrided 
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"name = {self.name}, age={self.age}, salary={self.salary}"

    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee):
    #This class will inherit from the Employee class and declares it
    #This class can have it its own varibles like Junior/ Senior SW
    def __init__(self, name, age, level, salary):
        super().__init__(name , age, salary)    #Calling the init function of the parent class
        self.level = level
    
    def work(self):
        #Overriding the function present in the Parent class
        print(f"{self.name} is coding...")

class Designer(Employee):
    
    def __init__(self, name, age, salary, num_designs):
        super().__init__(name, age, salary)
        self.num_designs = num_designs
    
    def work(self):
        print(f"{self.name} is drawing...")

    def designs_worked_on(self):
        #This fuction has overrided the Parent class 
        print(f"the designer {self.name} has worked on {self.num_designs} so far")



se = SoftwareEngineer("Ganesh", 25,"Senior" ,65000)
print(se)
print(se.name, se.age)
se.work()


d = Designer("Geoff", 27, 10000, 10)
print(d)
print(d.name, d.age)
d.work()
d.designs_worked_on()


#POLYMORPHISM
"""Polymorphism means a function being used in different forms
    from the example above the work() function has achieved different forms from overriding
    So we can use this to achieve polymorphism by creating respective instances
"""

employees = [SoftwareEngineer("Ganesh", 25,"Senior" ,65000),
            SoftwareEngineer("Alex", 31,"Senior" ,75000),
            Designer("Yuriy", 28,"Senior" ,65000)]

def employee_motivation(EmployeesList):
    for employee in EmployeesList:
        employee.work()

print("\nHere are the employee motivation criteria")
employee_motivation(employees)            