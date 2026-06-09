import numpy as np
import os

import sounddevice as sd
from PyQt5.QtWidgets import *
from scipy.io.wavfile import write


     # base code for converting english to morse code bleeps & text
 


MORSE_CODE = {
    # Uppercase letters
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    # Lowercase letters (same codes)
    "a": ".-",    "b": "-...",  "c": "-.-.",  "d": "-..",
    "e": ".",     "f": "..-.",  "g": "--.",   "h": "....",
    "i": "..",    "j": ".---",  "k": "-.-",   "l": ".-..",
    "m": "--",    "n": "-.",    "o": "---",   "p": ".--.",
    "q": "--.-",  "r": ".-.",   "s": "...",   "t": "-",
    "u": "..-",   "v": "...-",  "w": ".--",   "x": "-..-",
    "y": "-.--",  "z": "--..",

    # Numbers
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    # Punctuation
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    "\"": ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
}

global MORSECODEPABLO


def convertToMorse(text):
 
 global MORSECODEPABLO
 MORSECODEPABLO = ""

 for c in text:
      if c.isalnum():
        MORSECODEPABLO += MORSE_CODE [c]
        MORSECODEPABLO += "   "
      elif c.isspace():
        MORSECODEPABLO += "       "

 return MORSECODEPABLO
     

def generateWAV(text, filename="static/sound.wav"):
   
   sampleRate = 44100
   dotLength = 0.2
   dashLength = 0.6
   gapLength = 0.2

   freq = 250

   tDot = np.linspace(0,dotLength,int(sampleRate*dotLength), False)
   tDash = np.linspace(0,dashLength, int(sampleRate*dashLength),False)
   tGap = np.zeros(int(sampleRate * gapLength))

   dot_sound = 0.5 * np.sin(2 * np.pi * freq * tDot)
   dash_sound = 0.5 * np.sin(2 * np.pi * freq * tDash)

   audio = np.array([])

   for stuff in text:
      
      if stuff == ".":
         audio = np.concatenate((audio, dot_sound, tGap))
      elif stuff == "-":
         audio = np.concatenate((audio,dash_sound,tGap))
      else:
         audio = np.concatenate((audio,tGap))
   
   filename = os.path.join(os.path.dirname(__file__), "static/sound.wav") # forces file to be saved in correct folder


   write(filename, sampleRate, audio.astype(np.float32))


# running the app
  
