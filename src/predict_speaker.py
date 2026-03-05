import pickle
import sounddevice as sd
from scipy.io.wavfile import write
from .feature_extraction import extract_features

MODEL_PATH = "models/speaker_model.pkl"


# modelni yuklash
model = pickle.load(open(MODEL_PATH, "rb"))


def record_voice(filename="recordings/test_voice.wav", seconds=3):

    fs = 16000

    print("Gapiring...")

    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write(filename, fs, audio)

    print("Ovoz saqlandi:", filename)

    return filename


def predict(file):

    features = extract_features(file)

    prediction = model.predict([features])

    return prediction[0]


def recognize_from_mic():

    # ovoz yozish
    file = record_voice()

    # speaker aniqlash
    speaker = predict(file)

    print("\nAniqlangan odam:", speaker)

    return speaker