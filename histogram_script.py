"""Histogram project."""


def text_file_list(file_path):
    """Grabs the .txt file and parses it into a list of words."""
    word_list = []
    with open(file_path) as f:
        # Converting .txt file in list of string and stripping \n from the end
        word_list = [word for line in f for word in line.split(" ")]
        word_clean_list = list(map(str.strip, word_list))
        f.close
        return word_clean_list


def histogram(word_list):
    """Loops through list and return a histogram with word count."""
    histogram_dict = {}
    for i in word_list:
        if i in histogram_dict:
            histogram_dict[i] += 1
        else:
            histogram_dict[i] = 1
    return histogram_dict


def histogram_tuples(words):
    """Make histogram of tuples"""
    hgram = []
    for word in words:
        index = find(word, hgram)
        if index is None:
            hgram.append((word, 1))
        elif index is not None:
            count = hgram[index][1]
            new_pair = [word, count + 1]
            hgram[index] = new_pair
    return hgram

def find(item,histogram):
   for index, pair in enumerate(histogram):
    if pair[0] == item:
        print("The index is " + index)
        return index
    return None

def list_of_words(length):
    dict_words = '/usr/share/dict/words'
    words_str  = open(dict_words, 'r').read()
    all_words  = words_str.split("\n")
    return all_words[0:length]

def count(word,histogram):
    index = find(word, histogram)
    if index:
        word_count_pair = histogram[index]
        print(word_count_pair)
        return word_count_pair[1]
    else:
        return 0

def unique_words(dictionary):
    """Return all unique words in Histogram."""
    unique_words_list = []
    for word, value in dictionary.items:
        if value == 1:
            unique_words_list.append(word)
    return len(unique_words_list)


def frequency(word, histogram):
    """Input a word and histogram and return count of word."""
    if histogram[word]:
        print(histogram[word])
    else:
        print("Word doesn't exist")


if __name__ == '__main__':
    # path = "The_Journal_of_Prison_Discipline.txt"
    # txt_list = text_file_list(path)
    # word_dictionary = histogram(txt_list)
    # unique_word_list = unique_words(word_dictionary)
    word_list = list_of_words(20)
    word_list.append('a')
    word_list.append('a')
    word_list.append('a')
    word_list.append('a')
    # print(word_list)
    tuple_hist = histogram_tuples(word_list)
    count_of_word = count('a', tuple_hist)
    print(count_of_word)

    
