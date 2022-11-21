
from poem_generator import *
from evaluation import *


def main():


    # diamante_list = ['blacker', ['hard', 'careful'], ['comin', 'go', 'do'], ['truth', 'family', '。', 'group'], ['get', '。', 'depart'], ['watchin', 'beautiful'], 'ceiling']

    # spacy_similarities(diamante_list)
    # conventional_similarity(diamante_list)

    # Find a way to input .txt files by asking for user to input
    # Read input while stripping the ",", ".", "'", "(", ")", etc.
    # Make is so that an indidivual string is inputted


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
    

    noun_list, adjective_list, verb_list = parts_of_speech()
    noun_list, adjective_list, verb_list = middle_man(noun_list, adjective_list, verb_list)

    # List of the diamante poem
    diamante_list = poem_maker(noun_list, adjective_list, verb_list)

    spacy_similarities(diamante_list)
    conventional_similarity(diamante_list)




if __name__ == "__main__":
    main()