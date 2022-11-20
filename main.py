"""
Written by Khalil Jackson

This project is designed to creates a Diamante Poem generator. A diamante poem 
is one that is diamond shaped because it takes two nouns, synonyms or antonyms,
and follows the order of 1-3 for the first noun and 3-1 for the second 
(one noun, two adjectives, and three 'ing' verbs). Between both sets of three 
'ing' verbs is four nouns that relate to both nouns.

The generator takes in a .txt file and uses spacy to groups words together 
by their parts of speech. Then, we select the necessary number of 
nouns, adjectives, and verbs from those lists to creare a diamante poem.

A poem is evaluated by how closely it follows the actual diamante poem 
structure. There are a total of 16 words across seven rows. Each poem will 
receive a score out of 16 to determine if each words fits its position.

[Talk to text]
[Saving poems to be read later]
"""

import spacy
import os



# passage = "We comin' (back) blacker than Black Panther 2 Nobody this thorough, that's the truth Never go against the family, that's something you don't do Don't get Eddie Kane'd tryin' to sing your way back in the group (Nah) Stars in the ceiling, God's Son in the building, rep that 7-1-8 It's hard to depart from that feeling, careful selling weight The DA be watchin' you dealing Get yourself straight Before they find that paraphernalia For those who claim a hundred million on taxes, beautiful actresses Street dudes who turned activist, who used to move packages Know Nas still here to remove the wall that our back against Legitimize all your hustles before the gavel hit"

# print("LOWERCASE VERSION")
# print(passage.lower)
# passage.replace(",", "")
# passage.replace("(", "")
# passage.replace(")", "")

#print(passage)

#Need to figure out how to input text from input file
#Need to remove commas and parentheses

def parts_of_speech():
    """
    Takes in text as a single string.

    Returning three values and put them into 


    Breaks down string into parts of speech.
    Makes lists for nouns, verbs, and adjectives.
    """

    nlp = spacy.load("en_core_web_sm")

    #connect the parameter with the code
    doc = nlp("We comin' blacker than Black Panther 2 Nobody this thorough, that's the truth Never go against the family, that's something you don't do Don't get Eddie Kane'd tryin' to sing your way back in the group (Nah) Stars in the ceiling, God's Son in the building, rep that 7-1-8 It's hard to depart from that feeling, careful selling weight The DA be watchin' you dealing Get yourself straight Before they find that paraphernalia For those who claim a hundred million on taxes, beautiful actresses Street dudes who turned activist, who used to move packages Know Nas still here to remove the wall that our back against Legitimize all your hustles before the gavel hit")

    noun_list = []
    adjective_list = []
    verb_list = []

    for token in doc:
        
        #if the word is a noun, add to noun_list
        if token.pos_ == "NOUN":
            noun_list.append(str(token))

        #if word is an adjective, add to adjective_list
        if token.pos_ == "ADJ":
            adjective_list.append(str(token))

        #if word is a verb, add to verb_list
        if token.pos_ == "VERB":
            verb_list.append(str(token))

    return noun_list, adjective_list, verb_list

def middle_man(noun_list, adjective_list, verb_list):
    """
    takes in noun_list, adjective_list, verb_list from parts_of_speech.
    
    Figure out what to do if there are not enough POS.
    """

    noun_list = noun_list
    adjective_list = adjective_list
    verb_list = verb_list

    #makes sure there are at least six nouns, a period for noun
    if len(noun_list) < 6:
        while len(noun_list) < 6:
            noun_list.append(".")

    #makes sure there are no more than six nouns
    if len(noun_list) > 6:
        while len(noun_list) > 6:
            noun_list.pop()

    #makes sure there are at least four adjectives, a period for adjective
    if len(adjective_list) < 4:
        while len(adjective_list) < 4:
            adjective_list.append(".")

    #makes sure there are no more than 4 adjectives
    if len(adjective_list) > 4:
        while len(adjective_list) > 4:
            adjective_list.pop()

    #makes sure there are at least six verbs, a period for a verb
    if len(verb_list) < 6:
        while len(verb_list) < 6:
            verb_list.append(".")

    #makes sure there are no more than six verbs
    if len(verb_list) > 6:
        while len(verb_list) > 6:
            verb_list.pop()

    return noun_list, adjective_list, verb_list

def poem_maker():
    """
    Takes in noun_list, adjective_list, verb_list from middle_man

    """

    noun_list = ['blacker', 'truth', 'family', 'way', 'group', 'ceiling']
    adjective_list = ['hard', 'careful', 'watchin', 'beautiful']
    verb_list = ['comin', 'go', 'do', 'get', 'sing', 'depart']






def main():

    noun_list, adjective_list, verb_list = parts_of_speech()
    middle_man(noun_list, adjective_list, verb_list)



if __name__ == "__main__":
    main()

