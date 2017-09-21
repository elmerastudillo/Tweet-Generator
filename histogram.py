"""Histogram project."""
path = "/Users/elmerastudillo/Desktop/MakeSchool_Computer_Science2/Tweet-Generator/The_Journal_of_Prison_Discipline.txt"


def text_file_list(file_path):
    """Grabs the .txt file and parses it into a list of words."""
    word_list = []
    with open(file_path) as f:
        # Converting .txt file in list of string and stripping \n from the end
        word_list = [word for line in f for word in line.split(" ")]
        f.close
        return word_list


word_list = text_file_list(path)


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


unique_w = histogram(word_list)
print(unique_w)


# Function to return all unique words in Histogram
def unique_words(dict):
    """Return all unique words in Histogram."""
    return len(dict)


unique_words(unique_w)


def frequency(word, histogram):
    """Input a word and histogram and return count of word."""
    if histogram[word]:
        print(histogram[word])
    else:
        print("Word doesn't exist")


# frequency("up", unique_w)
