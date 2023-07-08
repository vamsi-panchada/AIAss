import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        audio = r.listen(source=source)

        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        
        except Exception as e:
            print('Exception found E : ', e)
            return e
        

if __name__ == '__main__':
    while True:
        r = listen()
        print(r)