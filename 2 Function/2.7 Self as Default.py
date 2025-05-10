#Self as default argument

class Car:
    def __init__(self, brand, model):   # <- constructor with parameters
        self.brand = brand              # <- store brand in the object
        self.model = model              # <- store model in the object

    def display(self):                  # <- method inside the class
        return self.brand, self.model      # dot pachi ko parameter

car1 = Car("Toyota", "Corolla")         # <- creating an object
print(car1.display())                   # <- calling a method
                                           
                                           
                                           
                                            # __init__ or display() are method
                                            # dot pachi ko parameter
                                            # car1 is object
# ///////////////////
# Term	      Where it's defined     	     Example
# Function	 Defined outside a class   	  def greet():
# Method	 Defined inside a class	      def display(self):