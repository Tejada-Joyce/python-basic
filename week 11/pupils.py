import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


# Inside the main function, write statements to do the following:
# Call the read_compound_list function to read the pupils.csv file into a list named students_list.
# Write a lambda function that will extract the birthdate from a student.
# Write a call to the sorted function that will sort the students_list by birthdate from oldest to youngest.
# Print the students_list by calling the print_list function.

def main():
    students_list = read_compound_list("pupils.csv")
    birthdate = lambda student: student[BIRTHDATE_INDEX]
    given_name = lambda student: student[GIVEN_NAME_INDEX]
    birthdate_no_year = lambda student: student[BIRTHDATE_INDEX][5:]

    # Ordered from Oldest to Youngest
    order_by_age = sorted(students_list, key = birthdate)
    print("Ordered from Oldest to Youngest")
    print_list(order_by_age)

    # Ordered by Given Name
    order_by_given_name = sorted(students_list, key = given_name)
    print("\nOrdered by Given Name")
    print_list(order_by_given_name)

    # Ordered by Birth Month and Day
    order_by_birthdate_no_year = sorted(students_list, key = birthdate_no_year)
    print("\nOrdered by Birth Month and Day")
    print_list(order_by_birthdate_no_year)


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


# Function named print_list that takes a list as a parameter and prints each element of the list on a separate line. In other words, this print_list function should include a for each loop that prints each element on a separate line.
def print_list(list):
    for element in list:
        print(element)

if __name__ == "__main__":
    main()