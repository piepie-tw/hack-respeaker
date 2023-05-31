#!/usr/bin/python3

import time
from gtts import gTTS
from pygame import mixer
import tempfile
import sys

def speak(sentence, lang, loops=1):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        #print(sentence)
        #print(lang)
        tts = gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(loops)

if __name__ == "__main__":
    sentence = sys.argv[1]
    lang = sys.argv[2]
    speak(sentence, lang)
    time.sleep(int(len(sentence)/2 ))

