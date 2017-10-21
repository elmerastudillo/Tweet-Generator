from flask import Flask
# from StochasticSampling import get_word_weight_dict
# from StochasticSampling import get_random_word_by_weight_prob
# from histogram import histogram
# from histogram import text_file_list
from markov_model import markov_chain
from markov_model import generate_sentence
from cleanup import clean_file



app = Flask(__name__)


@app.route('/sentence')
def markov():
    clean_text_list = clean_file('corpus.txt')
    markov_word = markov_chain(clean_text_list)
    # higher_order_markov_chain = nth_order_markov_model(2, clean_text_list)
    sentence = generate_sentence(10, markov_words)
    print(sentence)
    return sentence

if __name__ == "__main__":
    app.run(debug = True)

# def random_word():
#     """Return random word using Flask Server."""
#     word_sentence = []
#     file_path = "The_Journal_of_Prison_Discipline.txt"
#     text_file = text_file_list(file_path)
#     word_dictionary = histogram(text_file)
#     dictionary = get_word_weight_dict(word_dictionary)
#     for _ in range(1, 10):
#         random_word = get_random_word_by_weight_prob(dictionary)
#         word_sentence.append(random_word)
#     sentence_string = ' '.join(word_sentence)
#     return sentence_string
