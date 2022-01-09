import speech_recognition as sr

listener = sr.Recognizer()
def hearing():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()



    except:
        command=int(2)
        pass
    return command
