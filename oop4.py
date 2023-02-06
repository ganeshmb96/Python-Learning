"""This file deals with encapsulation and abstraction"""

class SoftwareEngieer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None         #This is a private variable and cannot be seen when instantiation
        self._num_bug_solved = 0    #not completely private variable or protected variable

    #This function is run only internally
    def code(self):
        self._num_bug_solved += 1

    #getter function
    def get_salary(self):
        return self._salary
    
    #Setter function 
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)
    
    def _calculate_salary(self, base_value):
        if self._num_bug_solved < 10:
            return base_value 
        elif self._num_bug_solved > 10 and self._num_bug_solved < 100:
            return base_value * 2
        else:
            return base_value * 3


se = SoftwareEngieer("Ganesh", 25)
print(se.name, se.age)

for i in range(70):
    se.code()

se.set_salary(65000)
print(se.get_salary())