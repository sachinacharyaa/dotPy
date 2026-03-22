# cm = float(input("Enter length in centimeters: "))

# # Conversion factors
# CM_PER_INCH = 2.54
# INCHES_PER_FOOT = 12

# # Calculate total inches
# total_inches = cm / CM_PER_INCH

# # Calculate feet and remaining inches
# feet = int(total_inches // INCHES_PER_FOOT)
# inches = total_inches % INCHES_PER_FOOT

# # Display the result
# print(f"{cm} cm is equal to {feet} feet and {inches:.2f} inches.")



# first_name = input("enter the first name: ")
# last_name = input("enter the second name: ")
# full_name = first_name + " " + last_name
# print("Joined string" , full_name)



# Write a program to find the roots of a quadratic equation
# given the roots are not imaginary.

# import math

# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))

# if a == 0:
#     print("Not a quadratic equation (a must be non-zero).")
# else:
#     d = b * b - 4 * a * c
#     if d < 0:
#         print("Roots are imaginary; no real roots.")
#     else:
#         r1 = (-b + math.sqrt(d)) / (2 * a)
#         r2 = (-b - math.sqrt(d)) / (2 * a)
#         print("Roots:", r1, "and", r2)



# //Find the largest among three input numbers from user


# a = int(input("Enter a first number:  "))
# b = int(input("Enter a second number:  "))
# c = int(input("Enter a third number:  "))


# if a > b and a>c:
#     print(f"{a} is greatest. ")
    
# elif b> c:
#     print(f"{b} is greatest")
# else:
#     print(f"{c} is greatest ")
    
    
# Calculate the grade according to given condition for the makrs in 5 subject.
# For percentage > above 90, Grade A
# For percentage > above 80, Grade B
# For percentage > above 70, Grade C
# For percentage > above 55, Grade D


# math = int(input('Enter your marks: '))
# science = int(input('Enter your marks: '))
# english = int(input('Enter your marks: '))
# nepali = int(input('Enter your marks: '))
# social = int(input('Enter your marks: '))

# total_marks = (math + science + english + nepali + social)
# result = total_marks /5 


# if math> 40 and science>40 and english>40 and nepali>40 and social>40:
#     print('pass')
#     if result >= 90:
#       print("Grade A ")
#     elif result >= 80:
#       print("Grade B ")
#     elif result>= 70:
#      print("Grade C ")
#     elif result>= 55:
#      print("Grade D ")
#     else:
#      print("Grade F ")
# else:
#     print('Fail ')



# import calendar

# year = int(input("Enter a year: "))
# is_leap = calendar.isleap(year)


# if the year is perfectly divisble by 400 = leap year 

# if is_leap:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# import calendar

# year = int(input("Enter a year: "))


# # if the year is perfectly divisble by 400 = leap year 

# if (year % 400 == 0):
#     print(f"{year} is a leap year.")
# elif  (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is  a leap year.")
# else: 
#     print(f"{year} is not a leap year.")


# unit = int(input('Enter a unit: '))

# if unit<=100:
#  price = 10* unit
# elif unit<=200:
#  price = 1000 + (unit- 100) * 15
    
# elif unit<=300:
#     price = 1000 + 100* 15 + (unit- 200) * 20
# else:
#   price = 1000 + 1500 + 2000 + (unit-300)  * 25
  
# total_price = price + 250
# print('Total payable electricity bill ', total_price)
     
     
     
     

# income = int(input('Enter a income: '))

# if income<=500000:
#  rate = income * 0.01
# elif income<=700000:
#  rate = income * 0.1 
    
# elif income <=1000000:
#     rate = income* 0.2
# elif income>2000000:
#   rate = income * 0.36

# print('tax amount', rate)
     


# write a python program to display odd number from 1 tp 50


# write a program to display even number from the range given by the user
# user = int(input("Enter the range for even number : "))
# for n in range(user):
#     print(n)

# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# ensure start <= end

# start from the first even number in the range



# for n in range(start, end + 1):
#   if start % 2 == 0:
#     print(n)


# write a program to create a table of a number given by the User
# for eg 5 * 1 = 5


# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# write a program to display natural numbers and also find the sum 

# n = int(input("Enter a natural number: "))


# total = 0
# for i in range(1, n + 1):
#     print(i)
#     total += i

# print("Sum =", total)



#factorial of given  number
#5! = 5*4*3*2*1


# n = int(input("Enter a non-negative integer: "))

# fact = 1
# if n<0:
#   print("Factoial of negative number doesnot exist")
# for i in range(1, n+ 1):
#     fact *= i

# print(f"{n}! = {fact}")




# number= int(input("Enter a number: "))

# rev = 0
# print("Original Number", number)

# while(number! = 0):
#  rem = number % 10 # 34, rem = 3
#  rev = rev * 10 + rem  #rev = 4
#  number = number//10

# print("Reversed Number: ", rev)



# number = input("Enter a number: ")
# rev = number[::-1]
# print("Reversed Number: ", rev)



#Fibanacci Series: 0 1 1 


# first_num = 0
# second_num = 1
# n = int(input("Enter no of terms: "))

# while(n! = 0):
#   sum = first_num + second_num
#   print(first_num, end = "")
#   first_num = second_num
#   second_num = sum
#   n = n-1
  

#FIND THE PRIME NUMBER FROM A GIVEN INTERVAL FROM THE USER


# num = int(int("Enter a number: "))

# start = int(input("Enter the starting value: "))
# end = int(input("Enter the ending value: "))


# for i in range(start, end + 1):
#     count = 0
#     for i in range (1, val+ 1): 
#      if i % 1 ==0:
#       count = count + 1
#      if count == 2:
#        print(i)


#find the armstrong number from a given interval from the user

# num = int(input("enter a number: "))

# length = len(str(num))
# orig = num 
# sum = 0

# while(num! = 0):
#      last = num% 10
#      sum = sum + last ** length
#      num = num // 10
# if orig == sum:
#         print(orig)



# start = int(input("ente the starting value s: "))
# endd = int(input("ente the starting value s: "))


# for num in range(start, endd + 1):
#  length = len(str(num))
#  orig = num 
#  sum = 0

#  while(num! = 0):
#      last = num% 10
#      sum = sum + last ** length
#      num = num // 10
#  if orig == sum:
#         print(orig)


# #find the palindrom number from a given interval from the user

# num = int(input("Enter a number: "))

# reverse  = num[:: -1]
# if num == reverse:
#     print(f" {num} is a palindrrom")
# else: 
#     print(f" {num} is a palindrrom")


# random int

import random 
num = random.randint(1,10)


total_guess = 5
attempts = 0

while attempts < total_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess< num:
        print("Too low!, please enter higher number")
    elif guess > num:
        print("High, please enter lower number")
    else: 
        print(f'congrats! You guess it right in {attempts} attempts')
    break
else:
    print(f'Sorry!, you lose, The correct num was {num}')