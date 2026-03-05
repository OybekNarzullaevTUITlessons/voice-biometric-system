import os
import sounddevice as sd
from scipy.io.wavfile import write
import time

def collect_dataset(person_name, samples=5, seconds=3):

    fs = 16000
    dataset_path = f"dataset/{person_name}"

    os.makedirs(dataset_path, exist_ok=True)

    print(f"\n{person_name} uchun dataset yig'ilmoqda...")

    for i in range(samples):

        print(f"\n{i+1}-namuna yozishga tayyorlaning...")
        time.sleep(2)

        print("Gapiring...")

        audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()

        filename = f"{dataset_path}/{person_name}_{i+1}.wav"

        write(filename, fs, audio)

        print("Saqlandi:", filename)

    print("\nDataset yig'ish tugadi!")

collect_dataset("Javlon", samples=3)