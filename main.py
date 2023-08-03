import os
import time
import pyaudio
import playsound
import speech_recognition
from gtts import gTTS
import openai
import speech_recognition as sr
import uuid

api_key = "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"

lang = 'en'

openai.api_key = api_key

while True:
    def get_adio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)

                if "Friday" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                      messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save(file_name)
                    playsound.playsound(file_name, block=False)

            except Exception:
                print("Exception")

        return said

    # if "stop" in guy:
    #     break

    get_adio()



