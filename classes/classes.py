# A simple attempt to model a dog.

class Dog:
    def __init__(self, name, age):
        self.name = name    # attribute
        self.age = age      # attribute
    
    def sit(self):          # method
        print(f"{self.name} is now sitting.")

    def roll_over(self):    # method
        print(f"{self.name} rolled over!")
    
puppy = Dog("puppy", 27)    # create an instance/object of the Dog class
puppy.sit()                 # call the sit method using the puppy instance
puppy.roll_over()           # call the roll_over method using the puppy instance

willie = Dog("willie", 6)   # create another instance/object of the Dog class
print(f"{willie.name} is {willie.age} years old.")  # access attributes of the willie instance

# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: restaurant_name and cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that announces that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("The Food Place", "Italian")
print(restaurant.restaurant_name)  # print the restaurant_name attribute
print(restaurant.cuisine_type)     # print the cuisine_type attribute
restaurant.describe_restaurant()    # call the describe_restaurant method
restaurant.open_restaurant()       # call the open_restaurant method

# Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
restaurant1 = Restaurant("Burger King", "American")
restaurant2 = Restaurant("Sushi Bar", "Japanese")
restaurant3 = Restaurant("Pizza Palace", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
    
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}, Age: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")

william = User("William", "Smith", "william@example.com", 30)
william.describe_user()
william.greet_user()

jane = User("Jane", "Doe", "jane@example.com", 25)
jane.describe_user()
jane.greet_user()