"""

"""

import spacy

def list_joiner(word_list):

    word_list = word_list

    #turn first half of list into a string
    for section in word_list:
        if type(section) == str:
            diamante_string = diamante_string + section + " "
        # if type(section) == list and len(section) == 4:
        #     first_half = first_half + " ".join(section[0:2]) + " "
        #     second_half = second_half + " ".join(section[2:]) + " "
        else:
            diamante_string = diamante_string + " ".join(section) + " "




def spacy_similarities():
    """
    Takes in diamante_list, diamante_string from poem_maker.

    Gives a similarity score rangind from 0-1.
    """

    diamante_list = ['blacker', ['hard', 'careful'], ['comin', 'go', 'do'], ['truth', 'family', '。', 'group'], ['get', '。', 'depart'], ['watchin', 'beautiful'], 'ceiling']
    diamante_string = "blacker hard careful comin go do truth family 。 group get 。 depart watchin beautiful ceiling"

    first_half = diamante_list[0:3] + diamante_list[3][0:2]
    second_half = diamante_list[3][2:] + diamante_list[4:]

    print(list_joiner(first_half))



    # nlp = spacy.load("en_core_web_md")  # make sure to use larger package!
    # doc1 = nlp("I like salty fries and hamburgers.")
    # doc2 = nlp("Fast food tastes very good.")

    # # Similarity of two documents
    # print(doc1, "<->", doc2, doc1.similarity(doc2))

    # # Similarity of tokens and spans
    # french_fries = nlp("Uta Hagen")
    # burgers = nlp("Uta Hagen")
    # print(french_fries, "<->", burgers, french_fries.similarity(burgers))


# def wordnet_similarities():


def main():

    spacy_similarities()

if __name__ == "__main__":
    main()