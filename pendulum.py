"""
The time in seconds that a pendulum takes to swing
back and forth once is given by this formula:
             ____
            / n
    t = 2π / ----
          √  9.81

where t is the time in seconds,
π is PI the ratio of the circumference divided by
    the diameter of a circle (use math.pi), and
n is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
import math

#Prompt a user to enter the length of a pendulum in meters
length = float(input("Please enter the length of a pendulum (meters):"))

#Calculate time
time = 2*math.pi*math.sqrt(length/9.81)

#Print the time in seconds 
# print(f"Time (seconds): {round(time, 2)}")
print(f"Time (seconds): {time:.2f}")

