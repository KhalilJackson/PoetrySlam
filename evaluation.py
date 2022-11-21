"""
Written by Khalil Jackson

This file contains the functions used to provide and evaluation for the diamante poem. 


Resources considered:
"""

import spacy

def list_joiner(diamante_list):
    """
    Takes a half of diamante list from spacy_similarities and iterate through 
    it to create one string. If an item in the list it a string, add it 
    directly to the string; if it is a list, then join and add a space.

    Returns the diamante_string.

    Args:
        diamante_half = half of the diamante poem from diamante_list
    """

    diamante_list = diamante_list
    diamante_string = ''

    #turn first half of list into a string
    for section in diamante_list:
        if type(section) == str:
            diamante_string = diamante_string + section + " "
        else:
            diamante_string = diamante_string + " ".join(section) + " "

    return(diamante_string)

def spacy_similarities(diamante_list):
    """
    Takes in diamante_list, diamante_string from poem_maker and calculates the 
    similarity between the first and second half of the diamante poem. Breaks 
    the list into two half lists, uses list_joiner function to create strings 
    of the halves, then uses spacy similarity function to get a score between 
    0-1 of the similarity of the two halves.

    Returns the similarity score.

    Gives a similarity score rangind from 0-1.
    """

    diamante_list = diamante_list
    
    first_half = diamante_list[0:3] + diamante_list[3][0:2]
    second_half = diamante_list[3][2:] + diamante_list[4:]

    first_half_string = list_joiner(first_half)
    second_half_string = list_joiner(second_half)


    nlp = spacy.load("en_core_web_md")
    first_part = nlp(first_half_string)
    second_part = nlp(second_half_string)

    print("Spacy similarity score for diamante poem:")
    print(first_part.similarity(second_part))

    # return(first_part.similarity(second_part))

def conventional_similarity(diamante_list):
    """
    Takes in the diamante list. Scores the poem as a fraction of 16. Sees how 
    many "." there are and how many "ing" verbs there are
    """

    diamante_list = diamante_list

    counter = 0

    # Iterates through diamante_list to count number of "."
    for part in diamante_list:
        if type(part) == str:
            if part == "。" or part == ". ":
                counter = counter + 1

        if type(part) == list:
            for word in part:
                if word == "。" or word == ". ":
                    counter = counter + 1

    # Iterates through the first set of verbs
    for verb in diamante_list[2]:
        if verb[-3:] != "ing" and verb[-2:] != "in":
            counter = counter + 1

    # Iterates through the second set of verbs
    for verb in diamante_list[4]:
        if verb[-3:] != "ing" and verb[-2:] != "in":
            counter = counter + 1

    score = counter / 16

    print("Conventional score for diamante poem:")
    print(score)

    # return(score)