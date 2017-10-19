from histograms import Dictogram
import pwd
import random
from cleanup import clean_file
# from collection import deque

# Used Dictorgram class to access my histogram
#1 Used dictionary as data structure to create the markov chain
#2 For every word in the cleaned file - go through and update a historgram for the value
#3 Generate those tokens inside each historgram. 
#4 create the histogram for every single word
#5 set uzp and the if else statement and acces sets those words to the Dictogram inside our list
#6 Converting Markov to class object
class Markov:
    def __init__(self,iterable):
        """Initalize with an empty dictionary of word nodes"""
        self.nodes = {}
        self.update(iterable)

    # def update(self.iterable):
    #     pass

    # def generate_sentence(self):
    #     pass

    def update_node(self,word,next_word):
        if word in self.nodes:
            self.nodes[word].update([next_word])
        else:
            self.nodes[word] = Dictogram(next_word)

    def get_next(self, current_word):
        dictogram = self.nodes.get(current_word, None)
        if dictogram is None:
            return '[END]'
        return dictogram.get_random_word

    def generate_sentence(self):
        word = list(words.append(self.get_next('[Start]')))


def markov_model(data):
    """markov model for 1st order"""
    #Dictionary that stores windows as the key in the key-value pair and then the value 
    #for each key is a dictogram
    markov_chain = dict()
    # Looping through the ammount of indexs in the list
    for index in range(0, len(data) - 1):
        # If index word of list exists in dictionary then update the current index
        # Store a histogram of words for each window
        if data[index] in markov_chain:
            markov_chain[data[index]].update([data[index + 1]])
        else:
            markov_chain[data[index]] = Dictogram([data[index + 1]])
    return markov_chain

# Nth Order Markon Model Structure
def nth_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data)-order):
        #Creating the windowe
        window = tuple(data[i: i+order])
        # Adding to dictionary
        if window in markov_model:
            #Append to existing Dictogram 
            markov_model[window].update([data[i+order]])
        else:
            markov_model[window] = Dictogram([data[i+order]])
    return markov_model

# Walk our model
def generate_random_start(model):

    # Generate a "valid" starting word. 
    # A valid starting word are words that start a sentene
    if 'END' in model:
        end_word = 'END'
        while end_word == 'END':
            end_word = model['END'].return_weighted_random_word()
        return end_word
    return random.choice(list(model.keys()))
    pass

# Getting a random word as the start of the sentence
def get_start_token(markov):
    # return random.choice(list(markov_model.keys()))
    first_word = random.choice(list(markov.keys()))
    return first_word

# Generating sentence using first order markov_model
def generate_sentence(length, markov_model):
    # length parameter is length of the sentence
    # Create first word
    current_word = generate_random_start(markov_model)
    # Save first word to sentence list
    sentence = [current_word]
    # Loop through the length of sentence provided
    for i in range(0, length):
        # Getting current dictogram and starting from the current word(first word)
        current_dictogram = markov_model[current_word]
        # Getting random word from dictogram starting from the place of the current word
        random_word = current_dictogram.return_weighted_random_word()
        # Setting current word variable to the random word
        current_word = random_word
        # Append the new current word until the sentence length is formed
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence

# Generating sentence using nth order markov_model
def generate_sentence_with_nth_order(length, higher_order_markov_model):
    # length parameter is length of the sentence
    # Create first word
    current_word = generate_random_start(higher_order_markov_model)
    # Save first word to sentence list
    sentence = [current_word]
    # Loop through the length of sentence provided
    for i in range(0, length):
        # Getting current dictogram and starting from the current word(first word)
        current_dictogram = higher_order_markov_model[current_word]
        # Getting random word from dictogram starting from the place of the current word
        random_word = current_dictogram.return_weighted_random_word()
        # Setting current word variable to the random word
        current_word = random_word
        # Append the new current word until the sentence length is formed
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence


if __name__ == '__main__':
    clean_text_list = clean_file('corpus.txt')
    # print(clean_text_list)
    # print(markov_chain(clean_text_list))
    markov_chain = markov_model(clean_text_list)
    # higher_order_markov_chain = nth_order_markov_model(2, clean_text_list)
    print(markov_chain)
    sentence = generate_sentence(10, markov_chain)
    # sentence = generate_sentence_with_higher_order(10, higher_order_markov_chain)
    print(sentence)

