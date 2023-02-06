#List is not the best structure to store data 

#Class is the best option

#Class creation
class SoftwareEngineer:
    
    #Class Attribute is an attriute that is tied to the class and 
    #not to an object of the class
    alias = "Keyboard Magician"

    def __init__(self, name , age, level, salary):
        """Init is the class constructor and is used 
        for initializing all the variables of the class"""

        #Instance Attributes
        self.name  = name,
        self.age = age,
        self.level = level,
        self.salary = salary

        # print(name , age, level, salary)




#Object Creation in the form of instance
list_emp1 = ["Max", 20, "Junior", 5000]
se1 = SoftwareEngineer(*list_emp1)

se2 = SoftwareEngineer("Max", 20, "Junior", 5000)

#You can also print the object values as well
print(se2.name, se2.age)

#Works if there is a class attribute
print(SoftwareEngineer.alias)

#Recap
#Learnt how to create a class
#Class and Instance Attributes
#How to visualize object values 
#instance attibutes defined by __init__(self)