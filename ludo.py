#wap to find two random no from 1 to 6

import random

class Dice:
 def roll(self):             #self is compulsory - it is clear and call the method
     
     first = random.randint(1,6)
     second = random.randint(1,6)
     return first, second
 
 
d = Dice()
print(d.roll())
 
     