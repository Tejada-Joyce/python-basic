"""
Write a Python program that does the following:

Asks the user to enter four values:
- gender
- birthdate in this format: YYYY-MM-DD
- weight in US pounds
- height in US inches
Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
Converts inches to meters (1 in = 2.54/100 cm).
Calculates age, BMI, and BMR.
Prints age, weight in kg, height in cm, BMI, and BMR.
"""

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    print("Please, enter the following information:")
    # Get the user's gender, birthdate, height, and weight.
    gender = input("- Your gender (M or F): ")
    birthdate = input("- Your birthdate (YYYY-MM-DD): ") 
    weight = float(input("- Your weight in US pounds: ") )
    height = float(input("- Your height in US inches: ") )

    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.
    age = compute_age(birthdate)
    weight = kg_from_lb(weight)
    height = m_from_in(height)
    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)


    # Print the results for the user to see.
    print(
    f'''Age (years): {age}\n'''
    f'''Weight (kg): {weight:.2f}\n'''
    f'''Height (m): {height:.1f}\n'''
    f'''Body mass index: {bmi:.1f}\n'''
    f'''Basal metabolic rate (kcal/day): {bmr:.0f}'''
    )

def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = lb * 0.45359237
    return kg


def m_from_in(inch):
    """Convert a length in inches to meters.
    Parameter inch: a length in inches.
    Return: the length in meters.
    """
    m = inch * 2.54 / 100
    return m


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in meters.
    Return: a person's body mass index.
    """
    bmi = weight/height**2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in meters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.upper()=="F":
        bmr = 447.593 + 9.247*weight + 309.8*height - 4.330*age
    else:
        bmr = 88.362 + 13.397*weight + 479.9*height - 5.677*age
    return bmr

# Call the main function so that
# this program will start executing.
main()
