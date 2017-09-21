"""Stochastic-Sampling."""
from histogram import histogram
from histogram import text_file_list
import random


file_path = "The_Journal_of_Prison_Discipline.txt"
text_file = text_file_list(file_path)
word_dictionary = histogram(text_file)


def get_random_word(dictionary):
    """Returning a random word from a dictionary."""
    rand_index = random.randint(0, len(dictionary) - 1)
    key_list = list(dictionary)
    random_w = key_list[rand_index]
    return random_w


def get_word_weight_dict(dictionary):
    """Calculating prob weight of each word & returning a dict[word:weight]."""
    word_weight_dictionary = {}
    total_values = sum(dictionary.values())
    # Grab every value from dictionary python
    for (word, value) in dictionary.items():
        # print("{} : {} ".format(word, value))
        # Getting the weight of each value
        # times a word appears divided by total words
        total = float(value / total_values)
        # print(total)
        word_weight_dictionary[word] = total
    return word_weight_dictionary


def get_random_word_by_weight_prob(dictionary):
    """Returning a random word calculated by using relative probability."""
    # print(dictionary)
    # total_weight = sum(dictionary.values())
    # uniform() takes parameters , wherein you can submit the range of the random number
    random_int = random.random()
    cumulative_probability = 0.0
    for (word, word_weight) in dictionary.items():
        # computing the increasing cumulative probability
        cumulative_probability += word_weight
        # until the cumulative_probability becomes greater than the random_int
        if random_int < cumulative_probability:
            break
    return word


if __name__ == '__main__':
    import sys

    # print(get_random(word_dictionary))
    # print(get_probabilty_by_weight(word_dictionary))
    weight = get_word_weight_dict(word_dictionary)
    print(get_random_word_by_weight_prob(weight))
