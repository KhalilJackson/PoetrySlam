"""
Written by Khalil Jackson

Contains the method used to turn the poem and its evaluated score into an mp3 file.

Resources considered:
"""

from gtts import gTTS
import os



def main():
    # define variables
    s = "escape with plane"
    file = "file.mp3"

    # initialize tts, create mp3 and play
    tts = gTTS(s, 'en')
    tts.save(file)
    os.system("mpg123 " + file)


if __name__ == "__main__":
    main()
