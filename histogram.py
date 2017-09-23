"""Histogram project."""


def text_file_list(file_path):
    """Grabs the .txt file and parses it into a list of words."""
    word_list = []
    with open(file_path) as f:
        # Converting .txt file in list of string and stripping \n from the end
        word_list = [word for line in f for word in line.split(" ")]
        word_clean_list = list(map(str.strip, word_list))

        f.close
        # print(word_clean_list)
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

# Setting histogram return value to unique_w


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
    path = "/Users/elmerastudillo/Desktop/MakeSchool_Computer_Science2/Tweet-Generator/The_Journal_of_Prison_Discipline.txt"
    txt_list = text_file_list(path)
    word_dictionary = histogram(txt_list)
    unique_word_list = unique_words(word_dictionary)
    print(unique_word_list)
