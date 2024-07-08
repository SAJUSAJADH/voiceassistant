from Recognizespeech import recognize_speech, record_audio
from VoiceOutput import Voice_out

if __name__ == "__main__":
    while True:
        i = 0
        audio = record_audio(i)
        text = recognize_speech(audio)
        if "stop" in text or "quit" in text or "exit" in text:
            Voice_out('Good bye')
            print("Stopping...")
            break
        i+=1