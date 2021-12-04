"""
Your program must ask the user to respond to each of the 
ten statements with D, d, a, or A which mean strongly disagree, 
disagree, agree, and strongly agree. Your program must compute 
the score for each answer and sum and display the person's total 
score. It is a good idea to think about how you will split this 
program into functions before you begin writing the program.
D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
"""

def main():
    print(
    f"""This program is an implementation of the Rosenberg Self-Esteem Scale.\n"""
    """This program will show you ten statements that you could possibly\n"""
    """apply to yourself. Please rate how much you agree with each of the\n"""
    """statements by responding with one of these four letters:\n"""
    """D means you strongly disagree with the statement.\n"""
    """d means you disagree with the statement.\n"""
    """a means you agree with the statement.\n"""
    """A means you strongly agree with the statement.""")

    answer1 = input("1. I feel that I am a person of worth, at least on an equal plane with others.\nEnter D, d, a, or A: ")
    answer2 = input("2. I feel that I have a number of good qualities.\nEnter D, d, a, or A: ")
    answer3 = input("3. All in all, I am inclined to feel that I am a failure.\nEnter D, d, a, or A: ")
    answer4 = input("4. I am able to do things as well as most other people.\nEnter D, d, a, or A: ")
    answer5 = input("5. I feel I do not have much to be proud of.\nEnter D, d, a, or A: ")
    answer6 = input("6. I take a positive attitude toward myself.\nEnter D, d, a, or A: ")
    answer7 = input("7. On the whole, I am satisfied with myself.\nEnter D, d, a, or A: ")
    answer8 = input("8. I wish I could have more respect for myself.\nEnter D, d, a, or A: ")
    answer9 = input("9. I certainly feel useless at times.\nEnter D, d, a, or A: ")
    answer10 = input("10. At times I think I am no good at all.\nEnter D, d, a, or A: ")

    positive_answers = [answer1, answer2, answer4, answer6, answer7]
    negative_answers = [answer3, answer5, answer8, answer9, answer10]

    score_positive = determine_positive(positive_answers)
    score_negative = determine_negative(negative_answers)
    total_score = score_positive + score_negative

    return print(
        f"""Your score is {total_score}.\n"""
        """A score below 15 may indicate problematic low self-esteem."""
    )



def determine_positive(positive_answers):
    """
    Determine score for positive answers
    Parameter: list of of positive answers
    """
    sum = 0
    for i in positive_answers:
        if i == "D":
            sum += 0
        elif i == "d":
            sum += 1
        elif i == "a":
            sum += 2
        elif i == "A":
            sum += 3
        
    return sum

def determine_negative(negative_answers):
    sum = 0
    for i in negative_answers:
        if i == "D":
            sum += 3
        elif i == "d":
            sum += 2
        elif i == "a":
            sum += 1
        elif i == "A":
            sum += 0        
    return sum


if __name__ == "__main__":
    main()