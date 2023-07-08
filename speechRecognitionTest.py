import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listeing started ... ')
        audio = r.listen(source, 10, 10)
        print('listening stopped ... ')

    # Sphinx recognition

    try:
        print('sphinx output : '+r.recognize_sphinx(audio))

    except sr.UnknownValueError:
        print('Sphnix unable to detect the audio')

    except Exception as e:
        print('Exception on sphinx: ', e)

    
    # Google Speech Recognition

    try:
        print('Google Recognition Output: '+ r.recognize_google(audio))

    except sr.UnknownValueError:
        print('google unable to detect the audio')

    except Exception as e:
        print('Exception on google: ', e)


    # Whisper Recognition

    try:
        print('Whisper Recognition Output: ' + r.recognize_whisper(audio))

    except sr.UnknownValueError:
        print('Whisper unable to detect the audio')

    except Exception as e:
        print('Exception on whisper: ', e)


for _ in range(5):
    listen()