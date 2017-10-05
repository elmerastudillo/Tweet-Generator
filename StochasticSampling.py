"""Stochastic-Sampling."""
from histogram import histogram
from histogram import text_file_list
import random


def get_random_word(dictionary):
    """Returning a random word from a dictionary."""
    rand_index = random.randint(0, len(dictionary) - 1)
    key_list = list(dictionary)
    random_word = key_list[rand_index]
    return random_word


def get_word_weight_dict(dictionary):
    """Calculating prob weight of each word & returning a dict[word:weight]."""
    word_weight_dictionary = {}
    total_values = sum(dictionary.values())
    for (word, value) in dictionary.items():
        # times a word appears divided by total words
        total = float(value / total_values)
        word_weight_dictionary[word] = total
    return word_weight_dictionary


def get_random_word_by_weight_prob(dictionary):
    """Returning a random word calculated by using relative probability."""
    random_float = random.random()
    cumulative_probability = 0.0
    for (word, word_weight) in dictionary.items():
        # computing the increasing cumulative probability
        cumulative_probability += word_weight
        # until the cumulative_probability becomes greater than the random_int
        if random_float < cumulative_probability:
            break
    return word


if __name__ == '__main__':

    file_path = "The_Journal_of_Prison_Discipline.txt"
    text_file = text_file_list(file_path)
    word_dictionary = histogram(text_file)
    dictionary = get_word_weight_dict(word_dictionary)
    for _ in range(1, 10):
        print(get_random_word_by_weight_prob(dictionary))
