#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
from gpiozero import Button
from signal import pause
import speech_recognition as sr
import requests

import sys
try:
    reload         # Python 2
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:  # Python 3
    from importlib import reload

btn = Button(23)  # the button is wired to GPIO pin 17


def stt():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio, language="zh-TW")
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))


def passKeyword(keyword):
    r = requests.post("http://140.113.73.212:5000/deliver_keyword",
                      data={'keyword': keyword})
    return r.status_code


if __name__ == '__main__':
    btn.when_pressed = lambda: keyword=stt()
    btn.when_released = lambda: passKeyword(keyword)
    pause()

    # keyword=stt()
