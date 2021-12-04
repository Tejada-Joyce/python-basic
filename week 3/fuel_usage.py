"""
Write a Python program that asks the user for three numbers:
- A starting odometer value in miles
- An ending odometer value in miles
- An amount of fuel in gallons

Your program must calculate and print fuel efficiency in both
miles per gallon and liters per 100 kilometers. Your program must 
have three functions named as follows:
- main
- miles_per_gallon
- lp100k_from_mpg

All user input and printing must be in the main function. In other 
words, the miles_per_gallon and lp100k_from_mpg functions must not 
call the the input or print functions.
"""

def main():
    print("Please, enter the following values:")
    # Get an odometer value in U.S. miles from the user.
    first_reading = float(input("- The first odometer reading (in miles): "))

    # Get another odometer value in U.S. miles from the user.
    second_reading = float(input("- The second odometer reading (in miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    fuel = float(input("- The amount of fuel used (in gallons): "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(first_reading, second_reading, fuel)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    mpg = round(mpg, 1)
    # Round the liters per 100 km to two digits after the decimal.
    lp100k = round(lp100k, 2)

    # Display the results for the user to see.
    print(
    f'''{mpg} miles per gallon \n'''
    f'''{lp100k} liters per 100 kilometers''')


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg = abs(end_miles - start_miles)/ amount_gallons
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215/mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()