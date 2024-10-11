#Decorators

'''Python Decorators are a powerful and flexiable tools that are mainly used to add extra functionality to 
   functions and methods without modifying source content.
   Decoratos wrap a function, adding additional functionality before after the execution.'''

#How does the Python Decorators Work.?

'''A Decorator is higher-order function that takes another function as an argument and returns a new function.
   The new function usually contains the original function with some added behavior.'''

#Basic Structure of a Decorator

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before the original function.")
        return original_function
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()
'-----------------------------------------------------------------------------------'
#Decorator:

''' A Decorator is a design pattren that modifies a function or class without altering its code.
    Think of it as wrapping a fucntion with additional functionaly
'''

#Basic Example
def my_decorator(func):
    def wrapper():
        print("before funciton")
        func()
        print("After Funciton")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

'''Step of by step
    How decorators wrap functions
    1. Define a decorator that accepts a fucntion
    2. wrap it an another function to add behavior
    3. Apply it using @decrator_name
    '''
#before and after: Applying a Decorator to a  function

#Before decorator
def say_hello():
    print("hello")

#After applying decorator
@my_decorator
def say_hello():
    print("hello!")


#Real World Applications of Decorators:
'''
    1. Logging: Track function execution
    2. Authetication: verify permissions
    3. caching:     Optimize repeated operations'''

#logging decorator
def logfunction_call(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logfunction_call
def process_data():
    print("Processing data....")


 #Generators: Efficient iteration mode simple

''' A generator produces values one at a time, simplifying iteration and saving memory-perfect
    for handling large datasets or infiite sequences.
    '''

#Simple generator Example:Counting up to a Number

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

#Generators: Efficient iteration mode simple
'''
define with yield insted of return
generates values lazily as needed
ideal for memory efficiency'''


#practical Generator use cases

'''
    Large datasets: process one item at a time
    infine sequences: count without limits
    lazy evalutions: computer only when necessary.'''

#Generator for large files:processing one line at a time

#example
def countup_n(n):
    count = 1
    while count <= n:
        yield count
        count += 1


#Decorators and generators streamline our code and boost efficiency.


   
