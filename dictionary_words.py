import random
text_file = open("/usr/share/dict/words")
# content = text_file.readlines()
# print(content)

# looping through each word and stripping the \n in filename by using rstrip()
# Pseudocode
# content =  words array
# shuffle through content and return words by number user entered
content = [word.rstrip('\n') for word in text_file]
# print(content)
number = int(input("Enter number:"))
# content_range = range(int(number))
# content_range[number] for i in content

# loop the number of times the user inputs by using the range function
for _ in range(number):
    print(random.choice(content))



text_file.close()
