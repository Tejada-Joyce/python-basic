import random
    
def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)
    randomwords = ['join', 'love', 'smile']
    append_random_words(randomwords, 3)
    print(randomwords)

def append_random_numbers(numbers_list, quantity = 1):
    """
    To append a pseudo random number to a list
    Parameters: 
        a list named numbers_list 
        an integer named quantity that indicates how 
        many numbers we append(default value of 1)
    Return:
        none
    """
    for _ in range(quantity):        
        # Computes quantity pseudo random numbers by calling the random.uniform function.
        random_number = random.uniform(1, 100)
        # Rounds the quantity pseudo random numbers to one digit after the decimal.
        random_number = round(random_number, 1)
        # Appends the quantity pseudo random numbers onto the end of the numbers_list.
        numbers_list.append(random_number)

def append_random_words(words_list, quantity = 1):
    """
    To append a random word to a list
    Parameters: 
        a list named words_list  
        an integer named quantity that indicates how 
        many words we append(default value of 1)
    """
    nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    for _ in range(quantity):        
        # Computes random words by calling the random.choice function.
        random_word = random.choice(nouns)
        # Appends the random word onto the end of the words_list.
        words_list.append(random_word)

if __name__ == "__main__":
    main()