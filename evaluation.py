"""
Written by Khalil Jackson
11/22/2022

This file contains the functions used to evaluate the diamante poem and to make
strings from it list representation. list_joiner() makes the string from the 
list. spacy_similarities calculates a similarity score of the first and second 
half of the poem. conventional_similarity() creates a score out of 16 of how 
well the poem fits the conventions of a diamante poem.
"""

import spacy

def list_joiner(diamante_list):
    """
    Takes a diamante list from and iterates through it to create a string 
    representation. If an item in the list it a string, add it directly to the 
    string; if it is a list, then join and add a space. Designed to be used for
    the half lists from spacy_similarities and also to gather the entire string
    representation when the main function passes it into file_creator.

    Returns the string representation of either poem halves or its entirety.

    Args:
        diamante_half = half of the diamante poem from diamante_list
    """

    diamante_list = diamante_list
    diamante_string = ''

    # Turn the list of strings and lists into a string
    for section in diamante_list:
        if type(section) == str:
            diamante_string = diamante_string + section + " "
        else:
            diamante_string = diamante_string + " ".join(section) + " "

    # Returns string representation of the poem list
    return(diamante_string)

def spacy_similarities(diamante_list):
    """
    Takes in diamante_list from poem_maker() and calculates the similarity 
    between the first and second half of the diamante poem. Breaks the list 
    into two half lists, uses list_joiner() function to create strings of the 
    halves, then uses spacy similarity function to get a score between 0-1 of 
    the similarity of the two halves. Score ranges between 0-1, inclusive.

    Returns the similarity score.

    Args: 
        diamante_list = list representation of the poem
    """

    diamante_list = diamante_list
    
    # Creates lists for the first and second halves of the poem
    first_half = diamante_list[0:3] + diamante_list[3][0:2]
    second_half = diamante_list[3][2:] + diamante_list[4:]

    # Turns those lists into strings
    first_half_string = list_joiner(first_half)
    second_half_string = list_joiner(second_half)

    # Uses nlp to prepare strings for a similarity score
    nlp = spacy.load("en_core_web_md")
    first_part = nlp(first_half_string)
    second_part = nlp(second_half_string)

    # Returns the similarity score
    return(first_part.similarity(second_part))

def conventional_similarity(diamante_list):
    """
    Takes in the diamante list. Scores the poem as a fraction of 16 by seeing 
    how many empty words there are in the poem (empty words represented as 
    "."). Sees how many "." It also counts against a verb that does not end in 
    "ing" or "in".

    Returns conventional similarity score.

    Args:
        dimante_list = list representation of the poem
    """

    diamante_list = diamante_list

    counter = 0

    # Iterates through diamante_list to count number of "."
    for part in diamante_list:

        # Looks for period in the string elemnts of the list
        if type(part) == str:
            if part == "。" or part == ". ":
                counter = counter + 1

        # Looks for periods in the list elements of the list
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

    # Makes the score a fraction of 16
    score = counter / 16

    # Returns conventional score
    return(score)