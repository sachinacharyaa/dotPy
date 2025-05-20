import random

comp_choice = random.randint(1,100)

  
while True:
  try:
    user = int(input('Guess the number between 1 and 100: '))
 
    if user == comp_choice:
       print("Congratulation my boy you guessed it right!")
       break
  
    elif user > comp_choice:
      print("Too high, try again!")
  
    else:
       print("Too low, try again!")
 
 
 
  except ValueError:
    print('Invalid Choice')
  

  
  

    


































# import random

# weguess_random = random.randint(1, 100)  #random aauncha we dont know

# while True:
#  try:
#   user = int( input ("Guess a number between 1 and 100: "))
   
#   if user>weguess_random:
#     print("Too high!")
#   elif user<weguess_random:
#     print("To low")
#   else :
#     print("You guessed it, Correct!")

#  except ValueError:
#     print("Please enter a valid number")
#     break
    





































# user = (input ("Enter the number between 1 and 100: "))

# if user.isdigit():
#  print(user)
 
# else:
#     print("please enter valid number")
