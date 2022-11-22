"""
Written by Khalil Jackson


Resources considered:

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
        file = input("What .txt file would you like to use? Add .txt to the " +
        "name.")

        f = open(file,"r")
        
    except(FileNotFoundError, IOError):
        print("Error. Either file does not exist in this folder or the name " +
        "was inputted incorrectly")
        get_file_string()

    else:
        
        inputted_string = ""

        for line in f:
            for letter in line:
                if letter == "," or letter == "(" or letter == ")" or \
                    letter == "." or letter == "?" or letter == "!":
                    continue
                if letter == "\n" or letter == "'":
                    inputted_string = inputted_string + " "
                else:
                    inputted_string = inputted_string + letter.lower()

        return(inputted_string)


def main():


    inputted_string = get_file_string()

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
    file_name = file_creator(diamante_string, similarity_score, conventional_score)
    file_reader(file_name)

    # Read input while stripping the ",", ".", "'", "(", ")", etc.
    # There are sometimes where verbs end in "in" that aren't "ing" verbs


if __name__ == "__main__":
    main()