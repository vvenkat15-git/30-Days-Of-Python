#1. python program to reverse of given string 

string = input("enter your string here = ")
print("reverse of given string = ", string[::-1])

'--------------------'

#2. Check given string is palindrome or not

string = input("Enter your string here = ")
if string == string[::-1]:
    print(f"given string is {string} palindrome")
else:
    print(f"given string is {string} is not a palindrome")


'---------------------------------------------------------'

# 3. Count the occurances of each charcter in the given string using Collections
from collections import Counter
string = input("enter your string here = ")
occurnaces = Counter(string)
print(occurnaces)

'-----------------------------------------------------------'

# 4. Count the Occurances without using Collections

string = input("enter your number here = ")
occurnaces = {}

for i in string:
    if i in occurnaces:
        occurnaces[i] +=1
    else:
        occurnaces[i] = 1
print(occurnaces)

'-----------------------------------------------------------'

# 5. Factorial of given number

def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)
number = int(input("enter your number here = "))
print(factorial(number))

'_____________________________________________________'

# 6. Fibonacci series 

def fibonacci(n):
    return n if  n<10 else fibonacci(n-1)+fibonacci(n-2)
series = [fibonacci(i) for i in range(20)] 
print(series) 

'_______________________________________________________'

# 7. sum of its digits

def sumogdigits(n):
    return n if n <10 else n%10 +sumogdigits(n//10)
digits = input("enter your number to check the digits")
print(sumogdigits(digits))

'________________________________________________________'

# 8. Check the given number is prime or not

def is_prime(n):
    return n>1 and all(n%i for i in range(2,n))
number = input("enter number to check prime or not")
print(is_prime(number))

'_________________________________________________________'

# 9. Example on try except finally

try:
    a = 10
    b = 20
    result = a/b
    print(result)
except Exception as e:
    print(e)
finally:
    print("I will execute irrespective of exception")

'____________________________________________________________'

# 10. Local variable and global variable
a = 10
def my_func():
    b = 20
    print(a)
    print(b)
my_func() 
print(a)
print(b)
'____________________________________________________________'

# 11. multiple inheritance

class Animal():
    def eat(self):
        print("i can eat")
    def sleep(self):
        print("i can sleep")
class Dog(Animal):
    def bark(self):
        print("i can bark woof   woof")  
dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
'____________________________________________________________'

# 12. Returve data from dummy api

!pip3 install requests

import requests
def getdatafromdummyapi():
    try:
        responce = requests.get("url path")
        data = responce.json()
        print(data)
        return data

    except Exception as e:
        print("error is = ", e)
'______________________________________________________________'

# 13. Pickling and unpickling

import pickle
person = {"name":"Venkat",
          "age":25,
          "gender":"male"}
with open("person.pickle", "wb")as file:
    pickle.dump(person, file)
    print("pickling is completed")

#unpikcling
with open("data.pickle", "rb")as f:
    data = pickle.loads(f)
    print(data)
'______________________________________________________________'

# 14. Fibonacci sereis using generators

def fibonacci():
    a,b = 0, 1
    while True:
        yield a 
        a,b = b, a+b
fib_gen = fibonacci()
for i in range(10):
    print(next(fib_gen))
'_______________________________________________________________'