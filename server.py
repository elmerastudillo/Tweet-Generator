from flask import Flask
from StochasticSampling import get_word_weight_dict
from StochasticSampling import get_random_word_by_weight_prob
from histogram import histogram
from histogram import text_file_list

app = Flask(__name__)


@app.route('/')
def random_word():
    """Return random word using Flask Server."""
    word_sentence = []
    file_path = "The_Journal_of_Prison_Discipline.txt"
    text_file = text_file_list(file_path)
    word_dictionary = histogram(text_file)
    dictionary = get_word_weight_dict(word_dictionary)
    for _ in range(1, 10):
        random_word = get_random_word_by_weight_prob(dictionary)
        word_sentence.append(random_word)
    sentence_string = ' '.join(word_sentence)
    return sentence_string