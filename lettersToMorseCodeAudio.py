import winsound
import time
import numpy as np

import sounddevice as sd
import sys
from PyQt5.QtWidgets import *


class MorseApp(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Morse Code Generator") # window title

        mainLayout = QHBoxLayout() # boxed layout

        leftLayout = QVBoxLayout()

        self.inputBox = QLineEdit() # added input box thingy attribute
        self.inputBox.setMinimumHeight(200)
        self.inputBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        leftLayout.addWidget(self.inputBox, stretch=3) # adding to display

        self.convertButton = QPushButton("Convert") # adding button attribute
        self.convertButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        leftLayout.addWidget(self.convertButton, stretch=1) # adding widget
        self.convertButton.clicked.connect(self.morseProgramBabyyy)

        self.playButton = QPushButton("Play")   
        self.playButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        leftLayout.addWidget(self.playButton, stretch=1)
        
        self.playButton.clicked.connect(self.play)

        rightLayout = QVBoxLayout()

        self.outputBox = QTextEdit() # added output box attribute
        self.outputBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        rightLayout.addWidget(self.outputBox, stretch=5) # adding to display

        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        self.setLayout(mainLayout) # shows layout

    def morseProgramBabyyy(self):
     
     # base code for converting english to morse code bleeps & text
 
     string = self.inputBox.text()

     pablo = [s for s in string]

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
     MORSECODEPABLO = ""

     for c in pablo:
      if c.isalnum():
        MORSECODEPABLO += MORSE_CODE [c]
        MORSECODEPABLO += "   "
      elif c.isspace():
        MORSECODEPABLO += "       "
     global duration

     duration = {".":200,
         "-":600}
     
     global frequency1
     frequency1 = 250

     self.outputBox.setText(MORSECODEPABLO)
     QApplication.processEvents() # so it doesnt delay printing morse code in output box over bleeping
     
    def play(self):
      
      sampleRate = 44100
      silence = np.zeros(int(sampleRate * 0.2), dtype=np.float32)

      for i in MORSECODEPABLO:

       if i in duration.keys():

        winsound.Beep(frequency1, duration[i])
        time.sleep(0.2)

       elif i == " ":  # letter/word gap
        sd.play(silence, sampleRate)
        sd.wait()

# running the app
  
app = QApplication(sys.argv)
window = MorseApp() # window is object of MorseApp class

window.show() # displays window on screen
sys.exit(app.exec_()) # starts application event loop, ensures program exits cleanly when window is closed