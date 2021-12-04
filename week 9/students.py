import csv
from os import replace

"""
1. Opens the students.csv file for reading, skips the first 
    line of text in the file because it contains only headings, 
    and reads the other lines of the file into a dictionary. 
    The program must store the student I-Numbers as keys and 
    the student names as values in the dictionary.
2. Gets an I-Number from the user, uses the I-Number to find the 
    corresponding student name in the dictionary, and prints the name.
3. If a user enters an I-Number that doesn't exist in the dictionary, 
    your program must print the message, "No such student" (without the quotes).
"""


def main():
    ""
    INUMBER_INDEX = 0
    NAME_INDEX = 1
    students = read_dict("students.csv", INUMBER_INDEX)
    
    i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    i_number = remove_dashes(i_number)
    length = len(i_number)

    # Help from solution to learn of the isdigit method
    if not i_number.isdigit():
        print("Invalid I-Number")
    else:
        if (length < 9):
            print("Invalid I-Number: too few digits")
        elif (length > 9):
            print("Invalid I-Number: too many digits")
        else:
            if i_number in students:
                print(students[i_number][NAME_INDEX])
            else:
                print("No such student")

def read_dict(filename, key_column_index):
    
    dictionary = {}

    with open(filename) as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            key =  row[key_column_index]
            dictionary[key] = row

    return dictionary

def remove_dashes(i_number):
    new_i_number = i_number.replace("-","")
    return new_i_number

# Call main to start this program.
if __name__ == "__main__":
    main()
