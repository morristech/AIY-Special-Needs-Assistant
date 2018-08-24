#!/usr/bin/env python3
import sys
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

class assistantSettings:
    def __init__(self):
        settingsArray = []
        try:
            with open('/home/pi/.SpecialNeeds.config','r') as f:
                for line in f:
                    settingsArray.append(line)
        except:
            with open('/home/pi/.SpecialNeeds.config','w') as f:
                f.write('20\n')
                f.write('vacation')
            settingsArray.append('20')
            settingsArray.append('vacation')
        self.__volume = int(settingsArray[0])
        self.__schedule = settingsArray[1]
    
    def setVolume(self, volume):
        self.__volume = volume
    
    def getVolume(self):
        return self.__volume
    
    def setSchedule(self, schedule):
        self.__schedule = schedule
    
    def getSchedule(self):
        return self.__schedule
    

def main():
    settings = assistantSettings()
    volume = settings.getVolume()
    name = sys.argv[1]
    aiy.audio.say(name,volume=volume)
    

if __name__ == '__main__':
    main()