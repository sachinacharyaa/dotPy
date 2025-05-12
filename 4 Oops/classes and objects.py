# A class in Python is a user-defined template for creating objects.

# define a class
# class Dog:
#     sound = "bark"  # class attribute
    
# #Creating object
# animal = Dog()        #creating an object of that class
#                       # animal is the object 
# print(animal.sound)




#Creating class with  __init__()
# It automatically initializes object attributes when an object is created.
class Dog:
    species = "Canine"     # Class attribute

    def __init__(self, name, age):
       self.name = name   # Instance attribute
       self.age = age     # Instance attribute
       

animal = Dog("Jhonny ", 2)    #Creating object with  __init__()
print(animal.species) 
print(animal.name)
print(animal.age)

# Modify instance variables
animal.name = "jhonal"
print(animal.name)