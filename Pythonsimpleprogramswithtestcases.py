#1. python program to reverse of given string 
def reverse_string(string):
    return string[::-1]
string = input("enter your string here = ")
print("reverse of given string = ",reverse_string(string))


#pytestcases:
import pytest
def test_simple_string():
    assert reverse_string("hello") == "olleh"
def test_palindrome():
    assert reverse_string("racecar") == "racecar"
def check_with_empty_string():
    assert reverse_string("") == ""
def checkwithsingel_char():
    assert reverse_string("a") =="a"
def checkstringwithspace():
    assert reverse_string("hello world") == "dlrow olleh"
def checkwithnumbers():
    assert reverse_string("12345") == "54321"

'--------------------'

#2. Check given string is palindrome or not


def palindrome(string):
    return string == string[::-1]
string = input("enter your string here = ")
if string == string[::-1]:
    print(f"given string is {string} palindrome")
else:
    print(f"given string is {string} is not a palindrome")


#testcases:

import pytest

def test_palindrome_with_even_length():
    assert palindrome("abba") == True

def test_palindrome_with_odd_length():
    assert palindrome("racecar") == True

def test_palindrome_with_non_palindrome():
    assert palindrome("hello") == False

def test_palindrome_with_mixed_case():
    assert palindrome("Able was I ere I saw Elba") == False  # Note: Original function is case-sensitive

def test_palindrome_with_special_characters():
    assert palindrome("A man, a plan, a canal, Panama") == False  # Original function doesn't handle punctuation

def test_palindrome_with_empty_string():
    assert palindrome("") == True

def test_palindrome_with_single_character():
    assert palindrome("a") == True

def test_palindrome_with_spaces():
    assert palindrome("   ") == True  # Only spaces are considered a palindrome


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
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)
number = int(input("Enter your number here: "))
print(factorial(number))

#testcases
import pytest

def test_factorial_of_zero():
    assert factorial(0) == 1

def test_factorial_of_one():
    assert factorial(1) == 1

def test_factorial_of_two():
    assert factorial(2) == 2

def test_factorial_of_three():
    assert factorial(3) == 6

def test_factorial_of_four():
    assert factorial(4) == 24

def test_factorial_of_five():
    assert factorial(5) == 120

def test_factorial_of_large_number():
    assert factorial(10) == 3628800  # 10! = 3628800

def test_factorial_of_negative_number():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial(-1)

'_____________________________________________________'

# 6. Fibonacci series 

def fibonacci(n):
    if n < 0:
        raise ValueError("Number of terms must be non-negative.")
    return n if  n<10 else fibonacci(n-1)+fibonacci(n-2)
series = [fibonacci(i) for i in range(20)] 
print(series) 

#test cases

import pytest

def test_fibonacci_series_zero_terms():
    assert fibonacci(0) == []

def test_fibonacci_series_one_term():
    assert fibonacci(1) == [0]

def test_fibonacci_series_two_terms():
    assert fibonacci(2) == [0, 1]

def test_fibonacci_series_three_terms():
    assert fibonacci(3) == [0, 1, 1]

def test_fibonacci_series_four_terms():
    assert fibonacci(4) == [0, 1, 1, 2]

def test_fibonacci_series_five_terms():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_series_ten_terms():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_series_negative_terms():
    with pytest.raises(ValueError, match="Number of terms must be non-negative."):
        fibonacci(-5)

'_______________________________________________________'

# 7. sum of its digits

def sum_of_digits(n):
    if n < 0:
        raise ValueError("Number of terms must be non-negative.")
    return n if n <10 else n%10 +sum_of_digits(n//10)
digits = int(input("enter your number to check the digits:"))
print(sum_of_digits(digits))


#testcases

import pytest

def test_sum_of_digits_single_digit():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5
    assert sum_of_digits(9) == 9

def test_sum_of_digits_two_digits():
    assert sum_of_digits(10) == 1
    assert sum_of_digits(23) == 5
    assert sum_of_digits(99) == 18

def test_sum_of_digits_three_digits():
    assert sum_of_digits(100) == 1
    assert sum_of_digits(456) == 15
    assert sum_of_digits(999) == 27

def test_sum_of_digits_large_number():
    assert sum_of_digits(123456789) == 45

def test_sum_of_digits_negative_number():
    with pytest.raises(ValueError, match="Input must be a non-negative integer."):
        sum_of_digits(-1)

'________________________________________________________'

# 8. Check the given number is prime or not

def is_prime(n):
    if n < 0:
        raise ValueError("Number of terms must be non-negative.")
    return n>1 and all(n%i for i in range(2,n))
number = input("enter number to check prime or not")
print(is_prime(number))

#test cases

import pytest

def test_is_prime_with_negative_number():
    with pytest.raises(ValueError, match="Number must be non-negative."):
        is_prime(-1)

def test_is_prime_with_zero():
    assert is_prime(0) == False

def test_is_prime_with_one():
    assert is_prime(1) == False

def test_is_prime_with_two():
    assert is_prime(2) == True

def test_is_prime_with_three():
    assert is_prime(3) == True

def test_is_prime_with_four():
    assert is_prime(4) == False

def test_is_prime_with_five():
    assert is_prime(5) == True

def test_is_prime_with_six():
    assert is_prime(6) == False

def test_is_prime_with_large_prime():
    assert is_prime(29) == True

def test_is_prime_with_large_non_prime():
    assert is_prime(100) == False

def test_is_prime_with_large_prime_edge_case():
    assert is_prime(97) == True

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
