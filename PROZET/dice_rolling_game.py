
import random

while True:
 user = input("Roll the dice?(y/n): ").lower()

 if user == 'y':
   
   first = random.randint(1,6)
   second = random.randint(1,6)
   
   print(f'( { first} , {second})')
   
 elif user == 'n':
   print("Thanks for playing")
   break
   
 else :
   print("Invalid choice!")















# import random 



# while True:                       #sim  adding Loop
#  user = input("Roll the dice? (Y/N): ").lower()

#  if user == "y":
    
#   class dice:
#      def roll(self):
        
#         first = random.randint(1,6)
#         second = random.randint(1,6)
        
#         return first,second
    
    
#   d = dice()
#   print(d.roll())
  
 
#  elif user == "n":
#     print("Thanks for playing")
#     break                         #yeha break garni ho vani jabtak N aauna chaleko chalai
#  else:
#     print("Invalid chouice")
#                                #yeha break halni ho vani jabtak y or n bahek aru naayesamma chaleko chalai
