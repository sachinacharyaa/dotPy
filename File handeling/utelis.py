#with class, doing module of largest no

def find_max(numbers):
    max_number = numbers[0]

    for number in numbers:
         if number > max_number:
            max_number = number
    return max_number


numbers = [ 1 ,4, 5 ,3]
print(find_max(numbers))









# Without class and etc
# numbers = [ 1 ,4, 5 ,3]
# max_numbers = numbers([0])

# for number in numbers:
#    if number > max_number:
#     max_number = number

# print(max_number)