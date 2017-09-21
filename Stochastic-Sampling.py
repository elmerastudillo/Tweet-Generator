from histogram import histogram
import random

word_dictionary = histogram()


def random_word(dict):
    rand_index = random.randint(0, len(dict) - 1)
    print(rand_index)
    # Cats our dictionary
    print(len(dict))
    word_at_index = dict.values()[rand_index]
    print(word_at_index)
    # word = list(collection.keys())[list(collection.values())]
    # print(word)


random_word(word_dictionary)
