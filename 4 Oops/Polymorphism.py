# Polymorphism means "many forms"
# the same function or method can work differently depending on the data type.

# print(len("Hello"))  # String length  , here is len is poly
# print(len([1, 2, 3]))  # List length

# print(max(1, 3, 2))  # Maximum of integers  , here is max is poly
# print(max("a", "z", "m"))  # Maximum in strings


# Polymorphism in Functions

# def add(a,b):
#     return a+b

# print(add(2,5))              # Integer addition
# print(add("hello", "world")) # String concatenation
# print(add([1,3], [4,5]))     # List concatenation





#Polymorphism in OOPs

class dog:
    def speak(self):
        return "bark"
    
class cat:
    def speak(self):
        return "meow"
    
def animal_sound(animal):
    print(animal.speak())
    
    #creating obj
d = dog()
c = cat()

animal_sound(d)       #function bata obj use garera call gariyo 
animal_sound(c)



# # Runtime Polymorphism
# Occurs when the behavior of a method is
# determined at runtime based on the type of the object.

class Animal:
    def sound(self):           
        return "Some generic sound"

class Dog(Animal):           #override
    def sound(self):
        return "Bark"

class Cat(Animal):           #override
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals: 
    print(animal.sound())  # Calls the overridden method
                           #based on the object type  