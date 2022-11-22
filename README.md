# PoetrySlam

Goal: This project aims to develop a diamante poem generation and evaluation 
system. A diamante poem is one that is diamond shaped because it takes two 
nouns, synonyms or antonyms, and follows the order of 1-3 for the first noun 
and 3-1 for the second (one noun, two adjectives, and three 'ing' verbs). 
Between both sets of three 'ing' verbs is four nouns that relate to both nouns.

Title and setup: This poem generator is named A Diamond in the Rough. 
The setup needed to run the system is that you have .txt files of string in the
same folder as the code then it is ran; you input the name of the file 
including the .txt.

Code Description: The generator takes in a .txt file and uses spacy to group 
words together by their parts of speech. Then, we select the necessary number 
of nouns, adjectives, and verbs from those lists to creare a diamante poem.

A poem is evaluated by two metrics. The first is how similar the fist half of 
the poem is to the second half, which is done using the spaCy similarity 
function. The second is how closely the entire poem follows diamante poem 
conventions; there are a total of 16 words across seven rows; each poem will 
receive a score out of 16 to determine if each words fits its position.

The poem is then formatted into a single string with its two evaluation scores 
placed at the end so it can be written to a .txt file. Then, the file is read.

Challenges: This project challenged me in a number of ways. First, I had to 
completely break down how I wanted to approach this project before I even began
writing a line of code. Dealing with semantic differences and how the system 
would manipulate text and format it required a level of detail I am not used 
to, especially for such an open ended assignment. Thsi was the first time I 
tried working with wordnet, which I initially played around with until I 
learned to use spaCy and eventually decided to use it. It was also the first 
time I have ever written to a file to be read using tts. It was also a 
challenge because I my experience in python relative to other languages is 
less, and I did things and thought about problems in a way I had not done 
before even in another language.

Issues to address: 1. Words are not randomly selected our of the available 
nouns, adjectives, and verbs. The intention to input poems, songs, or passages 
allows the system to take advantage of the inherent relation between the words.
2. Some "ing" verbs are shortened to "in," so we try to improve the accuracy of
evaluation by counting words that end in either "in" or "ing" as verbs. This 
helps a lot, especially in case of song lyrics, but there is an issue where 
some verbs that end in "in" are not beign verd, such as "explain."



By the Code Day deadline, please submit a link to your GitHub repo containing your code and documentation. 


Three scholarly papers in computer science that inspired your approach, and how.  You can research scholarly papers to include by using Google Scholar Links to an external site..
