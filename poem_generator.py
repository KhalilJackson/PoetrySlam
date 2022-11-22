"""
Written by Khalil Jackson
11/22/2022

This file contains the functions used to generate the poem. parts_of_speech() 
takes in the inputted string from the main function and breaks down the text 
into lists of the parts of speech. Middle man takes those lists and chooses 
which one to incorporate into the poem. Then, poem_maker() formats the lists to
create the poem, which is represented as a list.
"""

import spacy

def parts_of_speech(inputted_string):
    """
    Takes in the inputted text as a single string, and those words are 
    categorized by their parts of speech using spacy. The nouns, adjectives, 
    and verbs are kept and placed into respective lists to be passed down to 
    the middle_man function. Makes sure a word is added to a list once.
    
    Returns a noun list, an adjective list, and a verb list.
    
    Args:
        noun_list: list of nouns from the inputted text
        adjective_list: list of adjectives from the inputted text
        verb_list: list of adjectives from the inputted text
    """

    nlp = spacy.load("en_core_web_sm")

    # Connect the parameter with the code
    doc = nlp(inputted_string)

    noun_list = []
    adjective_list = []
    verb_list = []

    for token in doc:
        
        # If the word is a noun, add to noun_list
        if token.pos_ == "NOUN":
            if str(token) not in noun_list:
                noun_list.append(str(token))

        # If word is an adjective, add to adjective_list
        if token.pos_ == "ADJ":
            if str(token) not in adjective_list:
                adjective_list.append(str(token))

        # If word is a verb, add to verb_list
        if token.pos_ == "VERB":
            if str(token) not in verb_list:
                verb_list.append(str(token))

    # Returns all the nouns, adjective, and verbs from the text
    return noun_list, adjective_list, verb_list

def middle_man(noun_list, adjective_list, verb_list):
    """
    Takes in noun_list, adjective_list, verb_list from parts_of_speech, and it 
    wittles down the lists to only include the necessary number of nouns, 
    adjectvies, and verbs. If there are not enough of a part of speech, those 
    missing words are filled with a period. The function also selects for all 
    available 'ing' verbs to be added to the a new_verb_list in an attempt to 
    increase its evaluation score.

    Returns a noun list, an adjective list, and a verb list.

    Args:
        noun_list: list of nouns from the inputted text
        adjective_list: list of adjectives from the inputted text
        verb_list: list of adjectives from the inputted text
    """

    noun_list = noun_list
    adjective_list = adjective_list
    original_verb_list = verb_list
    
    new_verb_list = []

    # Makes sure there are at least six nouns, a period for noun
    if len(noun_list) < 6:
        while len(noun_list) < 6:
            noun_list.append(".")

    # Makes sure there are no more than six nouns
    if len(noun_list) > 6:
        while len(noun_list) > 6:
            noun_list.pop()

    # Makes sure there are at least four adjectives, a period for adjective
    if len(adjective_list) < 4:
        while len(adjective_list) < 4:
            adjective_list.append(".")

    # Makes sure there are no more than 4 adjectives
    if len(adjective_list) > 4:
        while len(adjective_list) > 4:
            adjective_list.pop()

    # Placed the 'ing' verbs from orinigal_verb_list in new_verb_list
    for verb in verb_list:
        if verb[-3:] == "ing" or verb[-2:] == "in":
            new_verb_list.append(verb)

    # Makes sure there are at least six verbs in new_verb_list
    if len(new_verb_list) < 6:

        # Add verbs from original list to new list until we reach 6
        while len(new_verb_list) < 6 and len(original_verb_list) > 0:

            # Ensures no repeated verbs between the two lists
            if original_verb_list.pop() not in new_verb_list:
                new_verb_list.append(original_verb_list.pop())
        
        # If there are no more verbs to add, substitute with a period
        while len(new_verb_list) < 6 and len(original_verb_list) == 0:
            new_verb_list.append(".")

    # Makes sure there are no more than six verbs
    if len(new_verb_list) > 6:
        while len(new_verb_list) > 6:
            new_verb_list.pop()

    # Returns POS lists containing the poem's words
    return noun_list, adjective_list, new_verb_list

def poem_maker(noun_list, adjective_list, verb_list):
    """
    Takes in noun_list, adjective_list, and verb_list from middle_man to create 
    a list representation of the diamante poem.

    Returns list representation of the poem.

    Args:
        noun_list: list of nouns from the inputted text
        adjective_list: list of adjectives from the inputted text
        verb_list: list of adjectives from the inputted text
    """

    noun_list = noun_list
    adjective_list = adjective_list
    verb_list = verb_list

    diamante_list = []

    # Appends diamante list in diamante poem order
    diamante_list.append(noun_list[0])
    diamante_list.append(adjective_list[0:2])
    diamante_list.append(verb_list[0:3])
    diamante_list.append(noun_list[1:5])
    diamante_list.append(verb_list[3:])
    diamante_list.append(adjective_list[2:])
    diamante_list.append(noun_list[-1])

    # Returns the poem represented as a string
    return diamante_list