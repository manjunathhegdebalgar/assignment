""" Program to count number of words in a text file """
import re

file_name = input("Enter file name: ")
word_count = 0
with open(file_name, "r") as f:
    for line in f:
        list_of_words = re.findall(
            r"[\w']+", line
        )  # using regular expression to fetch the words
        word_count = word_count + len(list_of_words)
print("Total number of words in the given file is ", word_count)
