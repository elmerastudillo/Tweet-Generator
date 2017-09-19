
def histogram():
    histogram_dict = {}
    word_file = []
    path = "/Users/elmerastudillo/Desktop/MakeSchool_Computer_Science2/Tweet-Generator/The_Journal_of_Prison_Discipline.txt"
    with open(path) as f:
        # Converting .txt file in list of string and stripping \n from the end
        word_file = [word for line in f for word in line.split(" ")]
    # print(word_file)
    # for word in list
    # if word doesnt exist  add it to the dictionary
    # else raise the count by 1 if word does exist
    for i in word_file:
        if i in histogram_dict:
            # print(i)
            histogram_dict[i] += 1
        else:
            histogram_dict[i] = 1
    path.close()
    return histogram_dict

# Setting histogram return value to unique_w
unique_w = histogram()


# Function to return all unique words in Histogram
def unique_words(dict):
    unique_w = 0
    for i in dict:
        unique_w += 1
    # print(unique_w)

unique_words(unique_w)

# Input a word and histogram and return how many times the word appears in the histogram
def frequency(word, histogram):
    if histogram[word]:
        print(histogram[word])
    else:
        print("Word doesn't exist")

frequency("up", unique_w)
