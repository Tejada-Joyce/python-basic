"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

#Prompt a user to enter their age
age = int(input("Please enter your age:"))

maxrate = 220 - age

min = 65/100 * maxrate

max = 85/100 * maxrate


#Print the time in seconds 
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {min:.0f} and {max:.0f} beats per minute.")