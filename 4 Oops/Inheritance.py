#inheritance  is reusing code

# class Dog:
#     def walk(self):
#         print("Wak")
        
# class cat:
#      def walk(self):
#         print("Wak")   #we have to put repeated one

# //////////////TO AVIOD ABOVE , using inheritance ///////////////////

class Mammal:
    def walk(self):
        print("Walk")
        
        
class Dog(Mammal):   #it inherit from parent class
    def bark(self):
        print("bark")                                                  #Incase,class have to smthng , so pass do nothing but no error aslo
                                                                        # d.walk()  it the print statement at last
class cat(Mammal):                                             
    def meow(self):
        print("meow")

d=Dog()
c= cat()



d.bark()
c.meow()