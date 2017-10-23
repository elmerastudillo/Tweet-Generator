from histograms import Dictogram
import random
from cleanup import clean_file
from collections import deque
import re


def markov_chain(data):
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

def nth_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data)-order):
        # Creatjng the window
        window = tuple(data[i: i+order])
        # If windiw is already in the markov model
        if window in markov_model:
            # Update the value
            markov_model[window].update([data[i+order]])
        else:
            # Add the value
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

# Provided by Jeff Chiu
def generate_random_sentence_n(length, markov_model):
    # Length denotes the max amount of chars
    # connect to twitter API
    current_window = get_start_token(markov_model)
    sentence = [current_window[0]]
    tweet = ''

    valid_tweet_flag = True
    sentence_count = 0
    while valid_tweet_flag:
        # We will generate random sentences until we decide we can not any more
        current_dictogram = markov_model[current_window]
        random_weighted_word = current_dictogram.return_weighted_random_word()

        current_window_deque = deque(current_window)
        current_window_deque.popleft()
        current_window_deque.append(random_weighted_word)
        current_window = tuple(current_window_deque)
        sentence.append(current_window[0])
        # print ('my current word inside windows: ' + str(current_window[1]))
        # print ('my current window: ' + str(current_window))
        if current_window[1] == 'end' or current_window[1] == '[end]':
            sentence_string = ' '.join(sentence)
            sentence_string = re.sub('end', '. ', sentence_string, flags=re.IGNORECASE)
            sentence_string = sentence_string.capitalize()
            new_tweet_len = len(sentence_string) + len(tweet)

            if sentence_count == 0 and new_tweet_len < length:
                # We should add this sentence to the tweet and move on to
                # make another
                tweet += sentence_string
                sentence_string = ' '.join(sentence)
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count == 0 and new_tweet_len >= length:
                # forget the sentence and generate a new one :P
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            elif sentence_count > 0 and new_tweet_len < length:
                # More than one sentence. and length is still less max
                # Get another new sentence
                tweet += sentence_string
                sentence_string = ' '.join(sentence)
                sentence_count += 1
                current_window = generate_random_start(markov_model)
                sentence = [current_window[0]]
            else:
                # Return this good good tweet
                return tweet


if __name__ == '__main__':
    clean_text_list = clean_file('corpus.txt')
    # print(clean_text_list)
    # print(markov_chain(clean_text_list))
    # markov_chain = markov_chain(clean_text_list)
    # # higher_order_markov_chain = nth_order_markov_model(2, clean_text_list)
    # print(markov_chain)
    # sentence = generate_sentence(10, markov_chain)
    # # sentence = generate_sentence_with_higher_order(10, higher_order_markov_chain)
    # print(sentence)
