# -*- coding:utf-8 -*-
import os
import datetime
from time import strftime
from gtts import gTTS
import playsound
import speech_recognition as sr
import os
import random
import datetime
from time import strftime
import time
import winsound

                       
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        print("слушаю тебя:")
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="ru-RU").lower()
        print("вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError as e:
        say_message("проверь интернет")
        return "ошибка"

def do_tris_command(message):
    message = message.lower()

    if 'да' in message:
            say_message('диктуй')
            zapis = listen_command()
            file = open('C:/assistent_1/budilnic/zap.txt', 'w', encoding='utf-8')
            file.write(zapis)
            file.close()
            say_message('я записала ' + zapis + ' время установлено на ' + vivacuba )

    elif 'нет' in message:
            say_message('хорошо, время установлено на ' + vivacuba)

def say_message(message):
    
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
    str(time.time())+"_"+str(random.randint(0, 100))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Маруся: "+message)


if __name__ == '__main__':
    
    now = strftime("%H:%M")    
    say_message('сейчас '+ now)
    say_message('задай время')
    
    vivacuba = listen_command()
    now = datetime.datetime.now()
    if now.hour >= 0 and now.hour < 10:
        vivacuba = '0' + vivacuba
    say_message('добавить описание при включении будильника? да или нет?')

    message = listen_command()  # слушает команду
    do_tris_command(message)  # обрабатывает команду

    while True:
        now = datetime.datetime.now()
        now = strftime("%H:%M")
        time.sleep(10)
        if  now == vivacuba:
            winsound.Beep(2500,1500)
            f = open('C:/assistent_1/budilnic/zap.txt', 'r', encoding='utf-8')
            f_all = f.read()
            say_message(f_all)
            f.close()
            now = strftime("%H:%M")    
            say_message('текущее время '+ now) 
            exit()
    
       
        

   