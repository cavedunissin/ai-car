#!/usr/bin/env python3

import speech_recognition as sr
import forecastio
from gtts import gTTS
import pygame,time

api_key = "9f3c6523191bf26504d35d55a3f7ecb6"
#api_key = 'Enter your api key'
lat = 25.0391667
lng =  121.525
lang = 'zh-TW'
file_name = 'weather.mp3'

forecast = forecastio.load_forecast(api_key, lat, lng)
r = sr.Recognizer()

def speak(text):
    print(text)
    tts = gTTS(text, lang)
    tts.save(file_name)
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play(loops=0)
    
    while pygame.mixer.music.get_busy() == True:
        time.sleep(0.5)
    


while True:
    with sr.Microphone() as source:
        print("Please wait .")
        r.adjust_for_ambient_noise(source,duration=1)
        print("Say something!")
        audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio, language = lang)
        print(cmd)

        if cmd == '你好':
            speak('你好啊，我是樹莓派機器人，你可以問我有關天氣的問題喔!')
        elif cmd == '氣溫預報':
            by_hour = forecast.hourly()
            for data in by_hour.data:
                speak('在' + str(data.time) + '氣溫是' +  str(data.temperature) + '度西')
        else:
            speak("對不起，我不懂你在說什麼")
            
    except sr.UnknownValueError:
        print("Google cloud not understand")
        
    except sr.RequestError as e:
        print("No response from google service:{0}".format(e))
