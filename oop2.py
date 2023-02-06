#How to use functions in classes and why to use them

#declaration of global function
list_emp1 = ["Max", 20, "Junior", 5000]

def code(se):
    print("This is the name of the person writing the code {}".format(se[0]))

#calling the function 
# code(list_emp1)

#Class creation
class SoftwareEngineer():
    
    #Class Attribute is an attriute that is tied to the class and 
    #not to an object of the class
    alias = "Keyboard Magician"

    #Class Function
    @staticmethod
    def entry_salary(age):
        ret_val = 0
        if age < 25:
            ret_val = 7000
        if age >= 25 and age<=30:
            ret_val = 10000
        return ret_val

    def __init__(self, name , age, level, salary):
        """Init is the class constructor and is used 
        for initializing all the variables of the class"""

        #Instance Attributes
        self.name  = name
        self.age = age
        self.level = level
        self.salary = salary

        # print(name , age, level, salary)
    #instance method
    def code(self):
        print("This is the name of the person writing the code {}".format(self.name))

    def code_in_language(self, language):
        print("{} writing in language {}".format(self.name, language))

    #built in methods called as DUNDER METHODS
    def __str__(self):
        """This method is executed whenever our object is converted 
            into a string
        """
        information = f"name  = {self.name} , age = {self.age}, salary = {self.salary}"
        return information

    #dunder method 2
    def __eq__(self, other):
        """This method gets two parametrs by default and compares
        their values"""
        return self.name == other.name and self.age == other.age

#Object /Instance Creation
se2 = SoftwareEngineer("Max", 20, "Junior", 5000)
se3 = SoftwareEngineer("Ganesh", 25, "Senior", 10000)
se4 = SoftwareEngineer("Ganesh", 25, "Senior", 10000)

#You can also print the object values as well
print(se2.name, se2.age)

#Using the intance function from the class
se2.code()
se2.code_in_language("Python")


#Printing out the object information
print("This is the default contents of the Class")
print(se2)      #The str method is called when we run this command and return value

#testing out the __eq__ method
print(se2 == se3)   #This will print out "False" because the memory address is different

print(se3 == se4)

#Calling the class function 
print(SoftwareEngineer.entry_salary(25))

#Testing to see how the static method responds to the object definition
print(se2.entry_salary(21))