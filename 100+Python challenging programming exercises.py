#Question1
#Level1

'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200(both included). 
The numbers obtained should be printed in a commaa-separated sequence on single line.'''

'Hints: Consider use range(#begin, #end)method.'

#Soultion

l = []
for i in range(2000, 3201):
    if (i%7 ==0) and (i%5!=0):
        l.append(str(i))
print(','.join(l))

'---------------------------------------------------------------------------------------------------------------------------------------------'

#Question2
'''Write a program which can compute factorial of given numbers. The results shoyld be printed in comma separated sequence on a single line.
   Suppose the follwing input is supplied to the program:8 then the output should be 40320.
 '''
#Hints
'''In case of input data being supplied to the question, it should be assumed to be a console input'''

#soultion

def factorial(n):
    return 1 if n ==0 else n*factorial(n-1)
number = input("enter your number to check the factorial= ")
print(factorial(number))

#soultion2
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
'------------------------------------------------------------------------------------------------------------------'
#Question3
'''With a Given integral numbe n, write a program to generate a dictionary that contains (i,i*i)
   such that is an integral number between 1 and n(both inclued). and then the program
   should print a dictionay. suppose the following input is supplied to the program:8
   then the output should be: {1:1, 2:4, 3:9, 4:16,5:25,6:36,7:49,8:64}'''
#Hints
'''In case of input data being supplied to the question, it should be assumed to be a 
   a console input. consider use dict()'''

#soultion:

n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)
'-------------------------------------------------------------------------------------------------------------------'

#Question4
'''Write a program which accepts a sequence of comma-separated number from console
   and generate a list and a tuple which contains every number. Suppose the following
   input is supplied to the program: 34,67,55,33,12,98 then, the output should be:
   ['34,'67','55','33','12','98'] ('34','67','55','33','12','98')'''

#Hints:
'''In case of input data being supplied to the question, it should be assumed to be a  console.input.tuple()
   can convert list to tuple'''

#Soultion:

values = int(input("enter values"))
l = values.split(",")
t = tuple(l)
print(l)
print(t)

#output:
'''enter values 44,55,66,77,88,99
['44', '55', '66', '77', '88', '99']
('44', '55', '66', '77', '88', '99')'''
'-------------------------------------------------------------------------------------------------------------'

#Question5
'''Define a clas which has at lest two methods:
   getString: to get a string from console
   input printString: to print in uppercase. Also please include
   simple test funcion to test the class methods'''

#Hints
'Use init method to construct some parameters'

#Soultion
class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
strObj = InputOutString()
strObj.getString()
strObj.printString()
'------------------------------------------------------------------------------------------------------------------'
