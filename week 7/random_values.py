import random
    
def main():
    randfloats = [16.2, 75.1, 52.3]
    print(randfloats)
    append_random_values(randfloats, "float")
    print(randfloats)
    append_random_values(randfloats, "float", 3)
    print(randfloats)
    randomwords = ['join', 'love', 'smile']
    append_random_values(randomwords, "string", 3)
    print(randomwords)
    randint = []
    append_random_values(randint, "int", 6)
    print(randint)

def append_random_values(list, type, quantity = 1 ):
    """
    To append a pseudo random number to a list
    Parameters: 
        a list  
        a type that determines whether it is a string 
        or a float or an int
        an integer named quantity that indicates how 
        many numbers we append(default value of 1)
    Return:
        none
    """
    nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    for _ in range(quantity):  
        if type == "float":      
            # Computes quantity pseudo random numbers by calling the random.uniform function.
            random_float = random.uniform(1, 100)
            # Rounds the quantity pseudo random numbers to one digit after the decimal.
            random_float = round(random_float, 1)
            # Appends the quantity pseudo random numbers onto the end of the numbers_list.
            list.append(random_float)
        elif type == "string":
            # Computes random words by calling the random.choice function.
            random_word = random.choice(nouns)
            # Appends the random words onto the end of the list.
            list.append(random_word)
        elif type == "int":
            # Computes random ints by calling the random.randint function.
            random_int = random.randint(1, 100)
            # Appends the random int onto the end of the list.
            list.append(random_int)


if __name__ == "__main__":
    main()