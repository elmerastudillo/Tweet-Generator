from random import random

# Getting input from user and then splitting by space
words = input("Enter words: ").split(" ")
random.shuffle(words)
print(' '.join(words))
#
# rand_index = random.randint(0, len(words) - 1)
# wordsRandom = random.shuffle(words)
# print(wordsRandom)
