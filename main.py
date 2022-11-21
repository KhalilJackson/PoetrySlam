"""
Written by Khalil Jackson


Resources considered:

"""

import fileinput
from poem_generator import *
from evaluation import *


def get_file_string():
    """
    
    """
    
    try:
        file = input("What .txt file would you like to use? Add .txt to the name.")

        f = open(file,"r+")
        
    except(FileNotFoundError, IOError):
        print("Error. Either file does not exist in this folder or the name was inputted incorrectly")
        get_file_string()

    else:
        
        inputted_string = ""

        for line in f:
            for letter in line:
                if letter == "," or letter == "(" or letter == ")" or \
                    letter == "." or letter == "?":
                    pass
                if letter == "\n" or letter == "'":
                    inputted_string = inputted_string + " "
                else:
                    inputted_string = inputted_string + letter.lower()

        # print(inputted_string)
        return(inputted_string)




        
    #do what you want if there is an error with the file opening


    # try:
        
    #     file = input("What .txt file would you like to use? Add .txt to the name.")
        
    
    # except(FileNotFoundError, IOError):

    #     # Prints out exception before calling the function again
    #     print("Error. Either file does not exist in this folder or the name was inputted incorrectly")
    #     get_file_string()
       

    # else:
    #     inputted_string = ""

    #     for line in fileinput.input(files = file):
    #         for letter in line:
    #             if letter == "," or letter == "(" or letter == ")" or \
    #                 letter == "." or letter == "?":
    #                 pass
    #             if letter == "\n" or letter == "'":
    #                 inputted_string = inputted_string + " "
    #             else:
    #                 inputted_string = inputted_string + letter.lower()
        
    #     return(inputted_string)

def main():
    """
    
    """

    # inputted_string = get_file_string()

    print(get_file_string())

    # noun_list, adjective_list, verb_list = parts_of_speech(inputted_string)
    # noun_list, adjective_list, verb_list = middle_man(noun_list, adjective_list, verb_list)
   
    # # List of the diamante poem
    # diamante_list = poem_maker(noun_list, adjective_list, verb_list)

    # # Getting spacy similarity score and conventional similarity score
    # spacy_similarities(diamante_list)
    # conventional_similarity(diamante_list)



    # Find a way to input .txt files by asking for user to input
    # Read input while stripping the ",", ".", "'", "(", ")", etc.
    # Make is so that an indidivual string is inputted

    #write the poem to .txt 
    #one function take in string text and reads it
    #one reas in poem and calls the other one to read it


if __name__ == "__main__":
    main()