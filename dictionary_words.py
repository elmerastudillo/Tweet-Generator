import random

# looping through each word and stripping the \n in filename by using rstrip()
# Pseudocode
# shuffle through content and return words by number user entered
# loop the number of times the user inputs by using the range function

def get_object_from_list(lst, index):
    for _ in range(index):
        rand_index = random.randint(0, len(lst) - 1)
        value = content[rand_index]
        # print(value)

text_file = open("/usr/share/dict/words")
content = [word.rstrip('\n') for word in text_file]
number = int(input("Enter number:"))
get_object_from_list(content, number)
text_file.close()
