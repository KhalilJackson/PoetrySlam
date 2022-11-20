# PoetrySlam
This project aims to develop a diamante poem generation and evaluation system. 
A diamante poem is one that is diamond shaped because it takes two nouns, 
synonyms or antonyms, and follows the order of 1-3 for the first noun and 3-1 
for the second (one noun, two adjectives, and three 'ing' verbs). Between both 
sets of three 'ing' verbs is four nouns that relate to both nouns.

The generator takes in a .txt file and uses spacy to groups words together 
by their parts of speech. Then, we randomly select the necessary number of 
nouns, adjectives, and verbs for a diamante poem.

A poem is evaluated by how closely it follows the actual diamante poem 
structure. There are a total of 16 words across seven rows. Each poem will 
receive a score out of 16 to determine if each words fits its position.
 
[Talk to text]
[Saving poems to be read later]