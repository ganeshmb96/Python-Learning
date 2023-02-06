"""This file deals with encapsulation and abstraction"""

class SoftwareEngieer:

    def __init__(self):
        self._salary = None         #This is a private variable and cannot be seen when instantiation

    #property decorator
    @property
    def salary(self):
        #can use the checks and constraints
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self, value):
        del self._salary
    
    
se = SoftwareEngieer()

se.salary = 65000
# del se.salary
print(se.salary)