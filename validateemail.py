#validate emial:
#lenght of the email
#@should be inemail
#.should be in email
#firstletter should be in alphabet
#end with .com or .in or 
#based on these conditons need to write a code


#using regular expersssions

import re

def validate_email(email):
    #basic regex for validating an email address
    pattren = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(in|com|org)$'
    return re.match(pattren, email) is not None

#example
email = "example@example.com"
if validate_email(email):
    print(f"{email} is valid email address")
else:
    print(f"{email}is not a valid")


'_____________________________________________________________'

import re

def validate_email(email):
    # Regular expression pattern for validating specific TLDs (.in, .com, .org)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(in|com|org)$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
emails = ["example@example.com", "user@domain.in", "test@website.org", "invalid@domain.net"]

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
