# Packages necessary to run
import time
import keyboard
import os
from pygame import mixer
import pyttsx3

# Find and play sound (if in the same folder as this file)
outrosound = os.path.join('outro.mp3')
mixer.init()
mixer.music.load(outrosound)
mixer.music.play()

time.sleep(0.25)
time.sleep(0.5)
keyboard.press_and_release("f11")
os.system("shutdown /s /t 11")
pyttsx3.speak('Ok sir im shutting down your pc in next 10 seconds')
for zaky in range(10):
    print("Shutting down in: " + str(10 - zaky) + " Seconds")
    time.sleep(1)

print("Shutting down now!")
time.sleep(0.5)
