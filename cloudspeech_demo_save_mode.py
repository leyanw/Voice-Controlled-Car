#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
#Importing Files for Voice Response
#import logging
#import sys
#import aiy.assistant.auth_helpers
#import aiy.voicehat
#from google.assistant.library import Assistant
#from google.assistant.library.event import EventType
#
#logging.basicConfig(
#    level=logging.INFO,
#    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
#)
import commands
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat


#Importing Files for Serial Comm
import time

path = []
"""recognizer = aiy.cloudspeech.get_recognizer()
wordsave = aiy.cloudspeech.get_recognizer()
recognizer.expect_phrase('turn off the light')
recognizer.expect_phrase('turn on the light')
recognizer.expect_phrase('blink')
recognizer.expect_phrase('straight')
recognizer.expect_phrase('back')
recognizer.expect_phrase('right')
recognizer.expect_phrase('left')
recognizer.expect_phrase('northeast')
recognizer.expect_phrase('northwest')
recognizer.expect_phrase('southwest')
recognizer.expect_phrase('southeast')
recognizer.expect_phrase('save')
recognizer.expect_phrase('done')
recognizer.expect_phrase('path')
    #recognizer.expect_phrase('rotate left')
recognizer.expect_phrase('rotate')
recognizer.expect_phrase('return')
wordsave.expect_phrase('Car')


button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()
aiy.audio.get_recorder().start()"""
recognizer = aiy.cloudspeech.get_recognizer()
wordsave = aiy.cloudspeech.get_recognizer()	

def main():
    #recognizer = aiy.cloudspeech.get_recognizer()
    #wordsave = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn off the light')
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('blink')
    recognizer.expect_phrase('straight')
    recognizer.expect_phrase('back')
    recognizer.expect_phrase('right')
    recognizer.expect_phrase('left')
#northeast
    recognizer.expect_phrase('one')
#northwest
    recognizer.expect_phrase('two')
#southwest
    recognizer.expect_phrase('three')
#southeast
    recognizer.expect_phrase('four')
    recognizer.expect_phrase('save')
    recognizer.expect_phrase('finish')
    recognizer.expect_phrase('path')
    #recognizer.expect_phrase('rotate left')
    recognizer.expect_phrase('rotate')
    recognizer.expect_phrase('return')
    recognizer.expect_phrase('stop')
    wordsave.expect_phrase('Car')


    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()
    #print('Press the button and speak')
    #button.wait_for_press()

    print('Listening...')
    text1 = wordsave.recognize()
    if not text1:
        print('No Hotword')
    else:
        aiy.audio.say('Hello Team')
        print("Hello Team")
        led.set_state(aiy.voicehat.LED.ON)
        while True:
            text = recognizer.recognize()
            if not text:
                print('Sorry, I did not hear you.')
            else:
                print('You said "', text, '"')
                aiy.audio.say('Ok')
                if 'save' in text:
                    save()
                    #aiy.audio.say('Begin Saving Path')
                elif 'turn on the light' in text:
                    led.set_state(aiy.voicehat.LED.ON)
                elif 'turn off the light' in text:
                    led.set_state(aiy.voicehat.LED.OFF)
                elif 'blink' in text:
                    led.set_state(aiy.voicehat.LED.BLINK)
                elif 'straight' in text:
                    print ("Straight Detected")
                    commands.straight()
                elif 'back' in text:
                    print ("Back Detected")
                    commands.back()
                elif 'right' in text:
                    commands.right()
                elif 'left' in text:
                    commands.left()
                elif 'one' in text:
                    commands.top_Right()
                elif 'two' in text:
                    commands.top_Left()
                elif 'three' in text:
                    commands.bottom_Right()
                elif 'four' in text:
                    commands.bottom_Left()
                elif 'rotate' in text:
                    commands.rightcircle()
                elif 'stop' in text:
                    commands.stop()
                elif 'path' in text:
                    path.reverse()
                    length = len(path)
                    print(*path, sep = ",")
                    for i in range (0, length):
                        if path[i] == 'straight':
                            commands.straight()
                            time.sleep(2)
                            commands.stop()
                            print ('straight')
                        elif path[i] == 'back':
                            commands.back()
                            time.sleep(2)
                            commands.stop()
                            print ('back')
                        elif path[i] == 'right':
                            commands.right()
                            time.sleep(2)
                            commands.stop()
                            print ('right')
                        elif path[i] == 'left':
                            commands.left()
                            time.sleep(2)
                            commands.stop()
                            print ('left')
                        elif path[i] == 'top_Right':
                            commands.top_Right()
                            time.sleep(2)
                            commands.stop()
                            print ('top_Right')
                        elif path[i] == 'top_Left':
                            commands.top_Left()
                            time.sleep(2)
                            commands.stop()
                            print ('top_Left')
                        elif path[i] == 'bottom_Right':
                            commands.bottom_Right()
                            time.sleep(2)
                            commands.stop()
                            print ('bottom_Right')
                        elif path[i] == 'bottom_Left':
                            commands.bottom_Left()
                            time.sleep(2)
                            commands.stop()
                            print ('bottom_Left')
                elif 'return' in text:
                        path.reverse()
                        print(*path, sep = ",") 
                        length = len(path)
                        for i in range (0, length):
                                if path[i] == 'straight':
                                        commands.back()
                                        time.sleep(2)
                                        commands.stop()
                                elif path[i] == 'back':
                                        commands.straight()
                                        time.sleep(2)
                                        commands.stop()
                                elif path[i] == 'right':
                                        commands.left()
                                        time.sleep(2)
                                        commands.stop()
                                elif path[i] == 'left':
                                        commands.right()
                                        time.sleep(2)
                                        commands.stop()
                                elif path[i] == 'top_Right':
                                        commands.bottom_Left()
                                        time.sleep(2)
                                        commands.stop()
                                elif path[i] == 'top_Left':
                                        commands.bottom_Right()
                                        time.sleep(2)
                                        commands.stop()
                                elif path[i] == 'bottom_Right':
                                        commands.top_Left()
                                        time.sleep(2)
                                        commands.stop()
                                elif path[i] == 'bottom_Left':
                                        commands.top_Right()
                                        time.sleep(2)
                                        commands.stop()
                elif 'goodbye' in text:
                    aiy.audio.say('Goodbye Team Marvic')
                    led.set_state(aiy.voicehat.LED.OFF)
                    break

def save():
    path.clear()
    aiy.audio.say('save mode')
    while True:
            text = recognizer.recognize()
            if 'straight' in text:
                    commands.straight()
                    time.sleep(2)
                    commands.stop()
                    path.append('straight')
                    print ("Straight saved")
            elif 'back' in text:
                    commands.back()
                    time.sleep(2)
                    commands.stop()
                    path.append('back')
                    print ("Back saved")
            elif 'right' in text:
                    commands.right()
                    time.sleep(2)
                    commands.stop()
                    path.append('right')
                    print ("right saved")
            elif 'left' in text:
                    commands.left()
                    time.sleep(2)
                    commands.stop()
                    path.append('left')
                    print ("left saved")
            elif 'one' in text:
                    commands.top_Right()
                    time.sleep(2)
                    commands.stop()
                    path.append('top_Right')
                    print ("top_Right")
            elif 'two' in text:
                    commands.top_Left()
                    time.sleep(2)
                    commands.stop()
                    path.append('top_Left')
                    print ("top_Left")
            elif 'three' in text:
                    commands.bottom_Right()
                    time.sleep(2)
                    commands.stop()
                    path.append('bottom_Right')
                    print ("bottom_Right")
            elif 'four' in text:
                    commands.bottom_Left()
                    time.sleep(2)
                    commands.stop()
                    path.append('bottom_Left')
                    print ("bottom_Left")
            elif 'rotate' in text:
                    commands.rightcircle()
                    time.sleep(1)
                    commands.stop()
                    path.append('rightcircle')
                    print ("rightcircle")
            elif 'finish' in text:
                    print(*path, sep = ",")
                    aiy.audio.say('save mode exited')
                    break
			
if __name__ == '__main__':
    main()



