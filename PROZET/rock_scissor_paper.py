import random



emojis = {'r': '🪨', 'p': '📜', 's': '✂'}
choices = ('r','p','s')

while True:
   user = input("Rock, paper or scissor? (r/p/s): ")
   if user not in choices:
      print("Invalid choice!")
      continue
      
      
   comp_choice = random.choice(choices)

   print(f'You chose {emojis[user]}')
   print(f'Computer chose {emojis[comp_choice]}')


   if user == comp_choice:
    print( 'Its a tie , try again')
   
   elif (user == 'r' and comp_choice == 's')or\
      (user == 's' and comp_choice == 'p') or\
      (user == 'p' and comp_choice == 'r'):
         
         print("OMG, You win!")
   else :
      print("You  lose")

   shall_continue = input("Do you want to play again? (y/n): ")


   if shall_continue =='n':
      print("thanks for here")
      break
   
































# import random

# # dic key _>
# # r -> ""
# emojis = {'r':  ' 🪨 ', 's':  '  ✂️', 'p': ' 📜  ' }     #dictonaries
# choices = ("r" , "p", "s")   # tuples are read only

# while True:
#  user = input ("Rock, paper, or Scissors(r/p/s): ").lower().strip()   # lower mean upp AND strip help to reduce space while input
#  if user not in choices:
#   print ("Invalid.")
#   continue                                 #it jumps to while , so dont come error initial
    
#  comp_choice = random.choice(choices)

#  print(f'You     chose {emojis[user]}')
#  print(f'Computer chose {emojis[comp_choice]}')

#  if user == comp_choice:
#     print("Tie ")
#  elif (user == 'r' and comp_choice == 's') or \
#      ( user =='p' and comp_choice == 'r') or \
#      ( user == 's' and comp_choice == 'p'):
         
#     print('You win')
#  else:
#     print('You lose')
    
#  shall_cont = input('continue?(y/n)').lower()
#  if shall_cont == 'n':
#     break                 #n aaysi balla rokeyo , navaye chaleko chalai