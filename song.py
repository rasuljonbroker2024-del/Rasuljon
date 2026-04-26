# song.py

# Code for children's song TTS

def synthesize_song(song_text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(song_text)
    engine.runAndWait()

if __name__ == '__main__':
    song = "Twinkle, twinkle, little star, How I wonder what you are!"
    synthesize_song(song)