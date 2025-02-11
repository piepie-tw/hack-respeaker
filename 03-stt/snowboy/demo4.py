import snowboydecoder
import sys
import signal
import speech_recognition as sr
import RPi.GPIO as GPIO
import os

"""
This demo file shows you how to use the new_message_callback to interact with
the recorded audio after a keyword is spoken. It uses the speech recognition
library in order to convert the recorded audio into text.

Information on installing the speech recognition library can be found at:
https://pypi.python.org/pypi/SpeechRecognition/
"""


interrupted = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def audioRecorderCallback(fname):
    print("converting audio to text")
    r = sr.Recognizer()
    r.pause_threshold = 1
    r.phrase_threshold = 0.3
    r.non_speaking_duration = 0.5
    r.dynamic_energy_threshold = False

    with sr.AudioFile(fname) as source:
        audio = r.record(source)  # read the entire audio file
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        #print(r.recognize_google(audio))
        print(r.recognize_google(audio, language="zh-TW"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    finally:
        GPIO.output(25, GPIO.LOW)
        os.remove(fname)



def detectedCallback():
    snowboydecoder.play_audio_file()
    GPIO.output(25, GPIO.HIGH)
    sys.stdout.write("Say something>>> ")
    sys.stdout.flush()

def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    GPIO.cleanup()


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print("Listening... Press Ctrl+C to exit")

# main loop
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()




