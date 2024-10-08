#Python String
#Create a str and assign a value to it

sim_str = str("hello World")
print(sim_str) #output: hello world

#Check if "faith" in sim_str
print('faith' in sim_str)  #output: False

#check if 'hello' in sim_str
print('hello' in str) #output: True

#String concatenation
other_str = "and welcome today's post :)"
sim_str +=other_str  #sim_str = sim_str+other_str

'''
Do you notice double quotes instead of singel quotes?
I did that because the string has an aprosphe
'''

print(sim_str) #output: Hellow world and welcome to today's post :)


#Get the length of the string

print("length of the string = ", len(sim_str))  #output: 43

#string slice ([start:stop:step])
#get the first word by string slice
greet = sim_str[0:5] 
print(greet) #output: "hello"

#convert string to list 

new_str_list = sim_str.split(" ")
print(new_str_list)
#output["hello", "world", "and", "welcome", "to", "today's", "post"]

#get first world from sim_str

first_word = new_str_list[0]
print(first_word ) #output: 'hello'

#question: How do you print a string and a number or any variable?
#Answer user f-string

"""
If we try to print(first_word + 5), we will get an error as teh + there is
a binary operator(addition) an dnot concatenation operator so you use f"string
"""

print(f"Favourite number: {5}") #output: Favourite number:5
print(f"Greet {first_word}")  #output: Hello

#string methods
#Note: All string methods return new values. They do not change the original string.
#1. upper()

print(sim_str.upper()) #output: HELLO

#2.lower()
print(sim_str.lower()) #output: 'hello'

#3. count()
print(sim_str.count('l')) #outupt: 2

#4. index()
space_index = sim_str.index(" ")
print(space_index)  #output: 5

#5. replace()
print(sim_str.replace("world", "everyone"))
