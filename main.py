import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('Listening...')

        # Recognition using SPHINX

        try:
            

        # Google Recognition
        # try:
        #     print('Listening ...')

        #     audio = r.listen(source, 10, 3)
        #     query = r.recognize_google(audio, language="en-in")
        #     print(f"User said: {query}")
        #     return query
        
        # except Exception as e:
        #     print('Exception found E : ', e)
        #     return e
        

if __name__ == '__main__':
    while True:
        r = listen()
        print(r)