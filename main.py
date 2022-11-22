"""
Written by Khalil Jackson
11/22/2022

This file contains the main function and helper funciton that calls the rest of
the functions to run the poetry generator. The main function initially calls 
get_file_string() to get a single string containing the inputted text then uses
poem_generator.py to cull through the text and formate the poem before it is 
written to a file and spoken in text_to_speech.py.
"""

from text_to_speech import *
from poem_generator import *
from evaluation import *

def get_file_string():
    """
    Asks the user to input the name of the .txt file containing strings that 
    will be used to generate the diamante poem. Uses try and exxcept to deal 
    with file errors and input/output errors. Then, it iterates through the 
    text to strip special characters and place all lines into a singule string.

    Returns the string of inputted text striped of special characters.

    Args:
        none
    """
    
    try:

        # Gets user input to open the desired local .txt file
        file = input("What .txt file would you like to use? Add .txt to the " +
        "name.")

        f = open(file,"r")
        
    except(FileNotFoundError, IOError):

        # If there is an error, print message and call function again
        print("Error. Either file does not exist in this folder or the name " +
        "was inputted incorrectly")
        get_file_string()

    else:
        
        inputted_string = ""

        # Iterates through file, strips characters, add to single string
        for line in f:
            for letter in line:
                if letter == "," or letter == "(" or letter == ")" or \
                    letter == "." or letter == "?" or letter == "!":
                    continue
                if letter == "\n" or letter == "'":
                    inputted_string = inputted_string + " "
                else:
                    inputted_string = inputted_string + letter.lower()

        # Returns the string stipped of special characters
        return(inputted_string)

def main():

    # Gets a single string from inputted test
    inputted_string = get_file_string()

    # Breaks down string to parts of speech then list for the poem
    noun_list, adjective_list, verb_list = parts_of_speech(inputted_string)
    noun_list, adjective_list, verb_list = middle_man(noun_list, \
        adjective_list, verb_list)
   
    # List of the diamante poem
    diamante_list = poem_maker(noun_list, adjective_list, verb_list)

    # Gets the string of the diamante poem
    diamante_string = list_joiner(diamante_list)

    # Getting spacy similarity score and conventional similarity score
    similarity_score = spacy_similarities(diamante_list)
    conventional_score = conventional_similarity(diamante_list)

    # File_creator needs diamante_string, similarity_score, conventional_score
    file_name = file_creator(diamante_string, similarity_score, \
        conventional_score)
    file_reader(file_name)

if __name__ == "__main__":
    main()