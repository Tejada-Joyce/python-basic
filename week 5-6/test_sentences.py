from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, create_sentence
import pytest
import random

"""
Note: it's better to increase the range in the cases I'm using
several "random" options so that it is more accurate.

"""

# Determiners Lists
single_determiners = ["the", "one"]
plural_determiners = ["some", "many"]
# Nouns Lists
single_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
# Preposition List
prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
# Verbs Lists
past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
# Tenses List
tenses_list = ['past', 'present', 'future']


def test_get_determiner():
    # Test the get_determiner function.

    # This loop will repeat the statements inside it 8 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(8):
        grammatical_number = random.randint(1,2) 
        word = get_determiner(grammatical_number)

        # Verify that the word returned from get_determiner is
        # one of the words in the corresponding determiners list.
        # 1. Test the single determiners.
        if(grammatical_number==1):
            assert word in single_determiners
        # 2. Test the plural determiners.
        else:
            assert word in plural_determiners

def test_get_noun():
    # Test the get_noun function.

    # This loop will repeat the statements inside it 8 times.
    for _ in range(8):
        grammatical_number = random.randint(1,2) 
        word = get_noun(grammatical_number)

        # Verify that the word returned from get_noun is
        # one of the words in the corresponding nouns list.
        # 1. Test the single nouns.
        if(grammatical_number==1):
            assert word in single_nouns
        # 2. Test the plural nouns.
        else:
            assert word in plural_nouns

def test_get_preposition():
    # Test the get_preposition function.
    
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_preposition()

        # Verify that the word returned from get_preposition is
        # one of the words in the prepositions list.
        assert word in prepositions

def test_get_prepositional_phrase():
    # Test the get_prepositional_phrase function.
    
    # This loop will repeat the statements inside it 8 times.
    for _ in range(8):
        quantity = random.randint(1,2)
        phrase = get_prepositional_phrase(quantity)
        word_list = phrase.split(" ")

        # Verify that the phrase returned from get_prepositional_phrase
        # contains 3 words in it and each word matches the correct 
        # preposition, determiner, and noun.
        assert len(word_list) == 3
        assert word_list[0] in prepositions
        if(quantity==1):
            assert word_list[1] in single_determiners
            assert word_list[2] in single_nouns
        else:
            assert word_list[1] in plural_determiners
            assert word_list[2] in plural_nouns
        
def test_get_verb():
    # Test the get_verb function.

    # This loop will repeat the statements inside it 8 times.
    for _ in range(8):
        tense = random.choice(tenses_list)
        grammatical_number = random.randint(1,2)
        word = get_verb(grammatical_number, tense)

        # Verify that the word returned from get_verb is
        # one of the words in the corresponding word list.
        # 1. Test the past tense.
        if(tense == "past"):
            assert word in past_verbs        
        # 2. Test the present tense.
        elif(tense == "present"):
            if(grammatical_number==1):
               assert word in present_singular_verbs
            else:
               assert word in present_plural_verbs
        # 3. Test the future words.
        elif(tense == "future"): 
            assert word in future_verbs

def test_create_sentence():
    # Test the create_sentence function.

    # This loop will repeat the statements inside it 8 times.
    for _ in range(8):
        grammatical_number = random.randint(1,2)
        random_bool = bool(random.getrandbits(1))
        tense = random.choice(tenses_list)
        sentence = create_sentence(grammatical_number, tense , random_bool)
        sentence_list = sentence.split(" ")

        # Verify that the sentence returned from create_sentence
        # contains 3/4(future) words without a prepositional phrase
        # and 6/7(future) words with a prepositional_phrase.
        if (tense == "future"):
            if(random_bool):
                assert len(sentence_list) == 7
            else:
                assert len(sentence_list) == 4
        else:
            if(random_bool):
                assert len(sentence_list) == 6
            else:
                assert len(sentence_list) == 3


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])