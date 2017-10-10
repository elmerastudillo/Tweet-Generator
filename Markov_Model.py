from histograms import Dictogram
import pwd


def markov_chain(data):

    markov_model = dict()

    for i in range(0, len(data) - 1):
        if data[i] in markov_model:
            markov_model[data[i]].update(data + 1)
        else:
            markov_model[Dictogram(data[i + 1])]
    return markov_model


if __name__ == '__main__':
    text_file = open('The_Journal_of_Prison_Discipline.txt')
    text_file_dict = Dictogram(text_file)
    # text_list = [word.rstrip('/n') for word in text_file_dict]
    markov_chain(text_file_dict)
