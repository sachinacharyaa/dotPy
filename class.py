# Program to convert centimeters to feet and inches

# Take input from user
cm = float(input("Enter length in centimeters: "))

# Conversion factors
CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12

# Calculate total inches
total_inches = cm / CM_PER_INCH

# Calculate feet and remaining inches
feet = int(total_inches // INCHES_PER_FOOT)
inches = total_inches % INCHES_PER_FOOT

# Display the result
print(f"{cm} cm is equal to {feet} feet and {inches:.2f} inches.")