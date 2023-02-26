from translate import Translator
thisdict = {
  "Hindi": "hi",
  "Kannada": "kn",
  "Tamil": "ta",
  "Telugu": "te",
  "Urdu":	"ur",
  "Malayalam":"ml",
  "Punjabi":"pa"
}
content=input('Enter content: ')
lang=input("Enter language: ")
translator= Translator(to_lang=thisdict[lang])
translation = translator.translate(content)
print(translation)

from gtts import gTTS #Import Google Text to Speech
from IPython.display import Audio #Import Audio method from IPython's Display Class
tts = gTTS(translation) #Provide the string to convert to speech
tts.save('1.wav') #save the string converted to speech as a .wav file
sound_file = '1.wav'
Audio(sound_file, autoplay=True) 

n=int(input('Enter number of times to repeat every sentence: '))
from gtts import gTTS #Import Google Text to Speech
from IPython.display import Audio #Import Audio method from IPython's Display Class
tts = gTTS(content) #Provide the string to convert to speech
tts.save('2.wav') #save the string converted to speech as a .wav file
sound_file1 = '2.wav'
Audio(sound_file1, autoplay=True) 
