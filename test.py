# -*- coding:utf-8 -*-
# win10 python 3.9.6 64-bit vivacuba1990
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
        print(e)

def beginning():
    now = strftime("%H:%M")    
    say_message('сейчас '+ now)
    say_message('задай время')
    
def do_tris_command(message):
    message = message.lower()   
    vivacuba = message
    now = datetime.datetime.now()
    if 'выход' in message:
        exit()

    if  len(vivacuba) == 4:
        vivacuba = '0' + vivacuba

    if len(vivacuba) <= 4 or len(vivacuba) >= 6:
        say_message('похоже неправильно задал время, начнём сначала')
        return beginning()

    say_message('добавить описание при включении будильника?')
    message = listen_command()

    if 'да' in message or 'давай' in message or 'ну давай' in message or 'добавь' in message:
        say_message('диктуй')
        zapis = listen_command()
        file = open('zap.txt', 'w', encoding='utf-8')
        file.write(zapis)
        file.close()
        say_message('я записала, ' + zapis + ' время установлено на ' + vivacuba )
        
    if 'нет' in message or 'не надо' in message or 'не стоит' in message:
        say_message('хорошо, время установлено на ' + vivacuba)

    

    while True:
        now = datetime.datetime.now()
        now = strftime("%H:%M")
        time.sleep(10)
        if  now == vivacuba:
            winsound.Beep(2500,1500)
            if os.path.exists('zap.txt'):
                f = open('zap.txt', 'r', encoding='utf-8')
                f_all = f.read()
                say_message(f_all)
                f.close()
                os.remove('zap.txt')
                now = strftime("%H:%M")    
                say_message('текущее время '+ now) 
            exit()

def say_message(message):
    
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
    str(time.time())+"_"+str(random.randint(0, 100))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Маруся: "+message)

if __name__ == '__main__':
    beginning()
        
while True:
    command = listen_command()
    do_tris_command(command) 

    
    
       
        

   
