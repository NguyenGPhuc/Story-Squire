import pyttsx3

voice_engine = pyttsx3.init()

# Text to speech setting
""" RATE"""
rate = voice_engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
voice_engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = voice_engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
voice_engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = voice_engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
voice_engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


# uses text to speech libary to read the reponse
def speech_response(gpt_response):
    voice_engine.say(gpt_response)
    voice_engine.runAndWait()