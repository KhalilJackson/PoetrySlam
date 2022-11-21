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

A poem is evaluated by two metrics. The first is how closely it follows the 
actual diamante poem structure. There are a total of 16 words across seven 
rows. Each poem will receive a score out of 16 to determine if each words fits 
its position. The second is a combined similarity score using nltk.wordnet and 
spaCy.

[Talk to text]
[Saving poems to be read later]
"""

import random
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
    Takes in the inputted text as a single string, and those words are 
    categorized by their parts of speech using spacy. The nouns, adjectives, 
    and verbs are kept and placed into respective lists to be passed down to 
    the middle_man function. 
    
    Returns noun_list, adjective_list, and verb_list.
    
    Args:
        noun_list: list of nouns from the inputted text
        adjective_list: list of adjectives from the inputted text
        verb_list: list of adjectives from the inputted text
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
    Takes in noun_list, adjective_list, verb_list from parts_of_speech, and it 
    wittles down the lists to only include the necessary number of nouns, 
    adjectvies, and verbs. If there are not enough of a part of speech, those 
    missing words are filled with a period. The function also selects for all 
    available 'ing' verbs to be added to the a new_verb_list in an attemp to 
    increase its evaluation score.

    Returns a noun_list, adjective_list, and new_verb_list.

    Args:
        noun_list: list of nouns from the inputted text
        adjective_list: list of adjectives from the inputted text
        verb_list: list of adjectives from the inputted text
    """

    noun_list = noun_list
    adjective_list = adjective_list
    original_verb_list = verb_list

    new_verb_list = []

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

    #placed the 'ing' verbs from orinigal_verb_list in new_verb_list
    for verb in verb_list:
        if verb[-3:] == "ing" or verb[-2:] == "in":
            new_verb_list.append(verb)

    #makes sure there are at least six verbs in new_verb_list
    if len(new_verb_list) < 6:
        while len(new_verb_list) < 6 and len(original_verb_list) > 0:
            new_verb_list.append(original_verb_list.pop())
        
        #if there are no more verbs to add, substitute with a period
        while len(new_verb_list) < 6 and len(original_verb_list) == 0:
            new_verb_list.append(".")

    #makes sure there are no more than six verbs
    if len(new_verb_list) > 6:
        while len(new_verb_list) > 6:
            new_verb_list.pop()

    # print("HERE IS THE NOUN LIST")
    # print(noun_list)
    # print("HERE IS THE ADJECTIVE LIST")
    # print(adjective_list)
    # print("HERE IS THE NEW VERB LIST")
    # print(new_verb_list)
    return noun_list, adjective_list, new_verb_list

def poem_maker(noun_list, adjective_list, verb_list):
    """
    Takes in noun_list, adjective_list, and verb_list from middle_man to create 
    a list representation of the diamante porem and a strign representation of 
    the diamante poem.

    Returns diamante_list and diamante_string.

    Args:
        noun_list: list of nouns from the inputted text
        adjective_list: list of adjectives from the inputted text
        verb_list: list of adjectives from the inputted text
    """

    # noun_list = ['blacker', 'truth', 'family', 'way', 'group', 'ceiling']
    # adjective_list = ['hard', 'careful', 'watchin', 'beautiful']
    # verb_list = ['comin', 'go', 'do', 'get', 'sing', 'depart']

    noun_list = noun_list
    adjective_list = adjective_list
    verb_list = verb_list

    diamante_list = []
    diamante_string = ""

    #appends diamante list in diamante poem order
    diamante_list.append(noun_list[0])
    diamante_list.append(adjective_list[0:2])
    diamante_list.append(verb_list[0:3])
    diamante_list.append(noun_list[1:5])
    diamante_list.append(verb_list[3:])
    diamante_list.append(adjective_list[2:])
    diamante_list.append(noun_list[-1])

    print("here is the diamante list")
    print(diamante_list)

    #iterates through list to format a string of the poem
    for section in diamante_list:
        if type(section) == str:
            diamante_string = diamante_string + section + " "
        else:
            diamante_string = diamante_string + " ".join(section) + " "


    print("here is the diamante string")
    print(diamante_string)

    return diamante_list, diamante_string




def main():

    # take user input to get the .txt file
    
    # plain_text = ""

    # with open("legit_nas.txt", "r") as f:
    #     for line in f:
   
    #         plain_text = plain_text + line
    #         # line.lower
    #         # line.replace(",", "")
    #         # line.replace("(", "")
    #         # line.replace(")", "")

    #     # print(line, end="")
    #     plain_text.lower
    #     plain_text.replace(",", "")
    #     plain_text.replace("(", "")
    #     plain_text.replace(")", "")
       
    #     print(plain_text)

    #     # text = f.read()
    #     # print(text)
    

    # noun_list, adjective_list, verb_list = parts_of_speech()
    # middle_man(noun_list, adjective_list, verb_list)

    poem_maker()



if __name__ == "__main__":
    main()

