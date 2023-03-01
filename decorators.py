"""
    This file is a tutorial on the workings and implementation of decorators in Python

    Definintion - The decorator is a function that gives Python the ability to change its own behaviour 
                  wihtout modifying its own code. The basic premise of a decorator is that it accepts a function 
                  as a parameter and returns a function.
"""

#The code below consists of a execution time evaluator that can be added to other 
#functions as a wrapper to determine how decorators work in Python

import time

def timer(func):        #You can pass functions as parameters to other functions
    def wrapper():
        t1 = time.time()
        """Understand how the below code works and what exactly are we passing a reference or the result of the function ? 
                        (My guess result of the function)"""
        res = func()    
        t2 = time.time()
        print(f"{func.__name__} executed in {str(t2 - t1)} seconds")
        return res
    return wrapper

#defining the function that will use the wrapper
def deprecated_test_decorator():
    time.sleep(2)
    print("Execute test decorator")

#calling the test function
test = timer(deprecated_test_decorator)    #setting up a reference and specifying the function to pass as parameter
print(test)                     #Running this line returns the pointer to location of the function
test()                          #This is then running the wrapper function on the specified function

"""The above 3 lines are not the best way to use decorators .
    The below way is how to effectively use them.

    Using the @timer to decorate a function is the same as stating that
    'test = timer(FUNCTION_NAME)'
"""

@timer
def correct_test_decorator():
    time.sleep(2)
    print("Executing the test decorator")

#Just calling the test decroator like a regular function
correct_test_decorator()

######################################################################

"""Below code blocks are snippets explaining further into the concepts of decorators"""

#Function to specify the author of the file
def specify_author(func):
    def wrapper(name):
        title = f"The author of this file is {func(name)}"
        return title
    return wrapper

#function to add things to the title of the file
def add_things(func):
    def wrapper(file_title):
        title = "The name of the file is " 
        new_title = title + func(file_title) +' !!!'
        return new_title
    return wrapper

@specify_author
def get_author(name):
    return name

@add_things
def get_title(file_title):
    return file_title

print(get_author('Simon Cowell'))
print(get_title('decorators'))

#Function to pass multiple arguements or varying number of arguments
def add_many_authors(func):
    def wrapper(*args, **kwargs):
        title = f"The author/s of this file is/are {func(*args, **kwargs)}"
        return title
    return wrapper

@add_many_authors
def get_mult_authors(n1, n2):
    return n1 + ','+ n2

print(get_mult_authors('anderj', 'karpathy'))