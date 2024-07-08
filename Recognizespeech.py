import speech_recognition as sr
from VoiceOutput import Voice_out
from Transfomersgpt import generate_response

recognizer = sr.Recognizer()

def record_audio(i):
    with sr.Microphone() as source:
        if i == 0:
            Voice_out("Listening")
        else:
            print('Listening...')
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        gpt = generate_response(text)
        Voice_out(gpt)
        print(gpt)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Sorry, there was an error processing your request."