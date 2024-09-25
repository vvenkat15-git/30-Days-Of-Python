'''The solid principles are five design principles for writing maintable and
   and scalabel object oriented code. They help in developing software that is
   easy to understand, flexiable and less prone to bugs.'''

#S....SINGLE RESPONSIBILITY PRINCIPLE

'A class should have only one reson to change, that means it should have only one job or respobsibility'
#Explanation:
'Each class should be focused on one aspect of functionality, making it easier to maintain to modify'

#Example::::

#Violation of SRP: Handling both user data and notification

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def notification(self, message):
        print(f"sending '{message}' to {self.email}")

#Adheting to SRP:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class NotificationService:
    def notification(self, message):
        print(f"sending '{message}' to {self.email}")
    
user = User("Alice", "alice@example.com")
NotificationService.send_email(user.email, "welcome to out platfrom")

#Here, the User class only handles user-related data and notificationService handles notification

'___________________________________________________________________________________________________________________'


# 2. OPEN/CLOSED PRINCIPLE

"DEFNITION"
'Classes should be open for Extention but Closed for Modification'
"EXPLANATION"
'we should be able to add new functionality wihtout altering the existing code'

#EXAMPLE:

#VIOLATION OF OCP: Adding new functionality requires modifying the class

class Discount:
    def apply_discount(self, total, discount_type):
        if discount_type == "fixed":
            return total - 10
        elif discount_type == "percentage":
            return total * 0.9


#ADHERING to OCP: Extending functionality by subclassing or using strategy pattren

from abc import ABC, abstractclassmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass

class FixedDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total - 10
    
class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total * 0.9
    

def calculate_price(total, discount_strategy: DiscountStrategy):
    return discount_strategy.apply_discount(total)

total_price = 100

discount = FixedDiscount()

print(calculate_price(total_price, discount))

#In this case, I extend the DiscountStrategy class to add new discount strategies witout modyfing the existing code

'_____________________________________________________________________________________________________________________'

# 3. LISKOV SUBSTITUTION PRINCIPLE
"DEFINITION"
'subtypes must be substitutable for their base types without altering the correctness of the program'
"EXPLANATION"
'Derived classes should be able to repalce their base class without affecting the program behaviour'


#EXAMPLE:
#Violation of LSP:

class Bird:
    def fly(self):
        print("flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")


#Adhering to LSP
class Bird(ABC):
    @abstractclassmethod
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("flying")

class Penguin(Bird):
    def move(self):
        print("Swimming")

def move_bird(bird: Bird):
    bird.move()

    
sparrow = Sparrow()
penguin = Penguin()
move_bird(sparrow) #output: Flying
move_bird(penguin) #output: Swimming

'The Base class Bird has a general move() method, and subclasses implement this method in a way appropriate to them.'

'________________________________________________________________________________________________________________________'


# 4. INTERFACE SEGREGATION PRINCIPLE:
"DEFINTION"
'No client should be foriced to depend on methods it does not use.'
"EXPLANATION:"
'A class should not implement interfaces it doesnot need split large interfaces into smaller, more specific ones.'

#Example:
#Violation of ISP

class Worker:
    def work(self):
        pass
    def eat(self):
        pass
class Robot(Worker):
    def work(self):
        print("Robot Working")

    def eat(self):
        raise NotImplementedError("Robot doesnt eat")
    
#Adhering to ISP

class Workable(ABC)
    def work(self):
        pass

class Estable(ABC):
    def eat(self):
        pass


class Human(Workable, Estable):
    def work(self):
        print("human working")

    def eat(self):
        print("human eating")

class Robot(Workable):
    def work(self):
        print("robot working")

worker = Robot()
worker.work()

#outut: Robot Working
'_________________________________________________________________________________________________________'

# 5. Dependency Inversion
"DEFINITION"
' High level modules should not depend on low-level modules both shlould be depend on abstractions'
"EXPLANAION"
'Depend on abstractions(interfaces rather than concrete implementations.)'

#Example:

class SQLDatabase:
    def connect(self):
        print("connecting to sql database")
    
class App:
    def __init__(self):
        self.database = SQLDatabase()

    def run(self):
        self.database.connect()

#Adhering to DIP:

class Database(ABC):
    def connect(self):
        pass


class SQLDatabase(Database):
    def connect(self):
        print("connecting to the sql database")
    
class NoSQLDatabase(Database):
    def connect(self):
        print("Connecting to NOSQL Database")

class APP:
    def __init__(self, database: Database):
        self.database = database

    def run(self):
        self.database.connect()

sql_db = SQLDatabase()
app = App(sql_db)
app.run()
#output: Connecting to SQl Database