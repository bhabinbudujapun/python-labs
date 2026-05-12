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