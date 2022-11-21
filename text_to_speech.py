"""
Contains the method used to turn the poem and its evaluated score into an mp3 file.

"""



# from gtts import gTTS
# import os

# # define variables
# s = "escape with plane"
# file = "file.m4a"

# # initialize tts, create mp3 and play
# tts = gTTS(s, 'en')
# tts.save(file)
# os.system("mpg123 " + file)

text = ["sitting", "runin", "batting", "comin"]

for word in text:
    if word[-3:] == "ing" or word[-2:] == "in":
        print("Got an ing inging here!")