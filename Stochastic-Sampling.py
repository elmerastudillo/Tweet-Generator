"""Stochastic-Sampling"""
from histogram import histogram
from histogram import text_file_list
import random


file_path = "/Users/elmerastudillo/Desktop/MakeSchool_Computer_Science2/Tweet-Generator/The_Journal_of_Prison_Discipline.txt"
text_file = text_file_list(file_path)
word_dictionary = histogram(text_file)


def get_random(dictionary):
    """Getting a random word from a dictionary."""
    rand_index = random.randint(0, len(dictionary) - 1)
    key_list = list(dictionary)
    random_w = key_list[rand_index]
    # print(random_word)
    # Total_words
    return random_w


def get_random_with_weight(dictionary):
    """Randomly picking items with given weights"""
    total_values = sum(dictionary.values())
    # Grab every value from dictionary python
    for (word, value) in dictionary.items():
        print("{} : {} ".format(word, value))
        total = value / total_values
        # Getting the weight of each value
        # (dict value divided by total sum of dict values)
        print(total)





    # word_at_index = dict.values()[rand_index]
    # print(word_at_index)
    # word = list(collection.keys())[list(collection.values())]
    # print(word


random_word(word_dictionary)
