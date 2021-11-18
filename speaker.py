def trans(strs):
    from googletrans import Translator
    translator=Translator()
    sentence=strs
    translatedsen=translator.translate(sentence,src='en',dest='bn')
    print(translatedsen.text)




def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)





texts=str(trans('how are you'))
speak(texts)
from gtts import gTTS
import playsound
import os

tts = gTTS(text=texts, lang='bn')
tts.save('good.mp3')
os.system('mpg321 good.mp3')
playsound.playsound('good.mp3', True)
