"""
Write a Python program that asks the user for two integers:  
1) the number of manufactured items and 
2) the number of items that the user will pack per box. 
Your program must compute and print the number of boxes necessary to hold 
the items. This must be a whole number. Note that the last box may be packed 
with fewer items than the other boxes.
"""
import math

#Prompt user for the number of manufactured items 
items = int(input("Enter the number of items: "))
#Prompt user for the number of items that the user will pack per box
itPerBox = int(input("Enter the number of items per box: "))

boxes = math.ceil(items/itPerBox)

# Print the number of boxes necessary to hold the items.
print(f"For {items} items, packing {itPerBox} items in each box, you will need {boxes} boxes.")