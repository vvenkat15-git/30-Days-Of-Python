#Variables in Python

first_name  = "venkat"
last_name   = "vanukuru"
country     = "India"
City        = "Hyderabad"
age         = 25
is_married  = False
skills      = ["Python", "Restapi","Fast-api","Django"]
person_info = {
        'firstname':"venkat",
        'lastname': "vanukuru",
        "city"   : "hyderabad"
}

#Printing the values stored in the variables

print("First Name:", first_name)
print("First name length: ", len(first_name))
print("Last Name:", last_name)
print("Last name length: ", len(last_name))
print("Country", country)
print("Age:",age)
print("Married:", is_married)
print("skills:", skills)
print("person Information:", person_info)

#Decalring multiple variables in one line

first_name, last_name, country, age, is_married = 'venkat', 'vanukuru', 'Inida','Hyderabad','25','Fasle'

print(first_name,last_name, country, age, is_married)
