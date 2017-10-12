from histograms import Dictogram
import pwd
from cleanup import clean_file


def markov_chain(data):
    """markov model for 1st ordergi"""
    markov_chain = dict()
    # Looping through the ammount of indexs in the list
    for index in range(0, len(data) - 1):
        # If 
        if data[index] in markov_chain:
            markov_chain[data[index]].update([data[index + 1]])
        else:
            markov_chain[data[index]] = Dictogram([data[index + 1]])
    return markov_chain


if __name__ == '__main__':
    clean_text_list = clean_file('The_Journal_of_Prison_Discipline.txt')
    # print(clean_text_list)
    print(markov_chain(clean_text_list))
