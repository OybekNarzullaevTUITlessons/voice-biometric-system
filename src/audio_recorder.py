import sounddevice as sd
from scipy.io.wavfile import write

def record_voice(filename="recordings/test_voice.wav", seconds=3):
    fs = 16000

    print("Gapiring...")

    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write(filename, fs, audio)

    print("Ovoz yozildi:", filename)