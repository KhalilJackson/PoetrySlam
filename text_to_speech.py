"""
Written by Khalil Jackson

Contains the methods used to turn the diamante poem into a .txt file then read 
it out loud.

Resources considered:
"""

from evaluation import *
from poem_generator import *
from gtts import gTTS
import os


def file_creator(diamante_string, similarity_score, conventional_score):
    """
    Takes in diamante_string, similarity_score, and conventional_score.
    
    """
    # diamante_string = "spacy similarity score for diamante poem"
    # similarity_score = 0.4356
    # conventional_score = 7/16

    diamante_string = diamante_string
    similarity_score = similarity_score
    conventional_score = conventional_score

    # Gathers the first and last noun from the string
    first_noun = diamante_string.split(" ", 1)[0]
    last_noun = diamante_string.split(" ", -1)[-1]

    # Combines first and last noun to create the file name
    file_name = "from_" + first_noun + "_to_" + last_noun + ".txt"

    file_string = ""

    # Formats a single string containing poem and scores 
    file_string = "The diamanté poem is as follows. " + diamante_string + \
        ". This poem has a similarity score of " + str(similarity_score) + \
            " and a conventional score of " + str(conventional_score) + "."

    # Creates and writes to a file using the formatted strings
    file = open(file_name, "w")
    file.write(file_string)
    file.close()

    return(file_name)


def file_reader(file_name):

    file_name = file_name

    # Opens file and gathers the string to by read
    f = open(file_name,"r")
    string = f.readline()
    
    # Reads the string
    os.system("say " + string)

# def main():

#     # file_creator()
#     file_reader()

# if __name__ == "__main__":
#     main()


