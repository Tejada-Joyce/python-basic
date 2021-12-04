"""
The size of a car tire in the United States is represented with three numbers like this:
205/60R15. The first number is the width of the tire in millimeters. The second
number is the aspect ratio. The third number is the diameter in inches of the wheel
that the tire fits. The volume of space inside a tire can be approximated with this
formula:

         π w² a (w a + 2,540 d) 
    v =  ----------------------
            10,000,000,000

where v is the volume in liters,
π is the constant PI which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Write a program that reads from the keyboard the three numbers 
for a tire and computes and outputs the volume of space inside that tire.
"""
import math
from datetime import datetime

#Prompt a user to enter the width, ratio, diameter of a tire
print("Please, enter the following values:")
width = int(input("- The width of the tire in mm (ex 205): "))
ratio = int(input("- The aspect ratio of the tire (ex 60): "))
diameter = int(input("- The diameter of the wheel in inches (ex 15): "))

#Calculate time
volume = math.pi*(width**2)*ratio*(width*ratio+ 2540*diameter)/10**10

#Print the time in seconds 
print(f"The approximate volume is {volume:.2f} liters.")

"""
Append to the end of the volumes.txt file one line of text 
that contains the following five values:
        current date
        width of the tire
        aspect ratio of the tire
        diameter of the wheel
        volume of the tire
"""

# Get the current date from the computer's clock.
date = datetime.now()
date = f"{date:%Y-%m-%d}"

# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as dimens_file:

    # Print a car's model and dimensions to the file.
    print(f"{date}, {width}, {ratio}, {diameter}, {volume:.2f}", file=dimens_file)

"""
Find tire prices for four or more tire sizes online. Add a set of if … elif … else 
statements in your program that use the tire width, tire aspect ratio, and wheel 
diameter that the user enters to find a price and then print the price.
"""

# I got the prices from https://www.discounttire.com/
if width == 185 and ratio == 60 and diameter == 15:
    price = 106
elif width == 215 and ratio == 75 and diameter == 15:
    price = 62
elif width == 205 and ratio == 55 and diameter == 16:
    price = 142
elif width == 245 and ratio == 60 and diameter == 18:
    price = 160
elif width == 275 and ratio == 50 and diameter == 22:
    price = 274
else:
    price = 250

print(f"The price of each tire with those dimensions would be ${price}.")


""""
After your program prints the price of the tire to the terminal, your program should ask 
the user if she wants to buy tires with the dimensions that she entered. If the user 
answers "yes", your program should ask for her phone number and store her phone number 
in the volumes.txt file.
"""

answer = input("Would you like to buy tires with these dimensions? ")

if answer.lower()== 'yes':
    phone_number = input("Perfect. Can I have your phone number, please? ")
    # Open a text file named volumes.txt in append mode.
    with open("volumes.txt", "at") as dimens_file:
        print(phone_number, file=dimens_file)
    print("Thank you. We will get those tires ready, then.")
else:
    print("I understand. Thank you for your visit.")

