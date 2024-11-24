import json
import random
from random import randrange, seed
import threading
import time
from gtts import gTTS
import pygame
import os

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
voiceLines = data['voiceLines']

language = ["en", "de", "el", "es", "fr", "fi"]

def randomizeVoiceLines():
    randomizedVoiceLines = voiceLines.copy()
    random.shuffle(randomizedVoiceLines)
    chosenVoiceLine = randomizedVoiceLines[0]

    usedLanguage = language[randrange(0, len(language))]

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    voiceLine = gTTS(text=chosenVoiceLine, lang="fi", slow=False)

    print(randomizedVoiceLines[0])
    print(usedLanguage)
    # File path
    voiceLineFile = "voiceLine.mp3"
    # Saving the converted audio in a mp3 file
    voiceLine.save("voiceLine.mp3")
    # Initialize the mixer module
    pygame.mixer.init()

    print("Playing voiceline audio...")
    # Load the mp3 file
    pygame.mixer.music.load("voiceLine.mp3")
    # Play the loaded mp3 file
    pygame.mixer.music.play()
    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    # Stop music before removing the files
    pygame.mixer.music.stop()
    # Explicitly quitting the mixer to release the files
    pygame.mixer.quit()
    # Short delay to allow for resource cleanup
    time.sleep(0.1)

    print("Audio playback completed.")

    # Now remove the audio files after playback
    if os.path.exists(voiceLineFile):
        os.remove(voiceLineFile)
    if os.path.exists(voiceLineFile):
        os.remove(voiceLineFile)

while True:
    seed(time.time())
    randomizeVoiceLines()
    # Random interval between 5 and 30 minutes (300-1800 seconds)
    random_interval = random.randint(300, 1800)
    #random_interval = random.randint(30, 300)
    print(f"Next call in {random_interval / 60:.2f} minutes / {random_interval} seconds")
    time.sleep(random_interval)