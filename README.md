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

A diamante poem is one where the words share a relation to one another, and the
most efficient way to ensure that words share a relation--given the tools I 
have currently--is to use imput from a song, or poem, or book since those tend 
to have words of related meaning. The idea behind this generator is that there 
exists a diamante poem for each input that fits the mold to varying degrees; 
the goal of this system is to find that diamante poem and determine how closely
it aligns to the conventional diamante poem. 

Some "ing" verbs are shortened to "in," so we try to improve the accuracy of 
evaluation by counting words that end in either "in" or "ing" as verbs. This 
helps a lot, especially in case of song lyrics, but there is an issue where 
some verbs that end in "in" are not beign verd, such as "explain."


 
[Talk to text]
[Saving poems to be read later]