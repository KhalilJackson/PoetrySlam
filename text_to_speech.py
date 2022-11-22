"""
Written by Khalil Jackson
11/22/2022

Contains the methods used to turn the diamante poem into a .txt file and read 
it out loud. file_creator() creates the file with the poem and scores 
represented as a single string; this was done because the readline function 
would have trouble reading the entire poem and scored formatted with newlines; 
the function also returns the filename because file_reader is called using it 
by the main; this prevents the chance there is an error inputting the local 
file. file_reader() reads the contents of the .txt files.

"""

from evaluation import *
from poem_generator import *
import os

def file_creator(diamante_string, similarity_score, conventional_score):
    """
    Takes in diamante_string, similarity_score, and conventional_score to 
    create a file containing a single string with the poem and its scores. 
    Names the poem after its first and last noun before formatting the string 
    and writitng it to a new file.

    Returns the name of the file.

    Args:
        diamante_string = string representation of the poem
        similarity_score = similarity score of poem halves
        conventional_score = similarity score of poem to its conventions
    """

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

    # Returns the file name
    return(file_name)

def file_reader(file_name):
    """
    Takes in the file name then opens the file to be read.

    Args:
        file_name = name of the file including ".txt"
    """

    file_name = file_name

    # Opens file and gathers the string to by read
    f = open(file_name,"r")
    string = f.readline()
    
    # Reads the string
    os.system("say " + string)