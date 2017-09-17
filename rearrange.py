import random

def scrambleList(lst):
    rand_index = random.randint(0, len(lst) - 1)
    for i in range(len(lst)):
        lst[i], lst[rand_index] = lst[rand_index], lst[i]

# Getting input from user and then splitting by space
words = input("Enter words: ").split(" ")
scrambleList(words)
print(words)
