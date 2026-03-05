# Voice Recognition Biometric System (Python 3.11)

Bu loyiha biometrik tizimlar fani uchun ishlab chiqilgan.

---

## 🛠 Texnologiyalar

- Python 3.11
- librosa
- numpy
- scikit-learn
- sounddevice
- scipy

---

## ⚙️ O'rnatish

Virtual environment yaratish:

```shell
python -m venv venv
.\venv\Scripts\activate
```

Paketlarni o'rnatish:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📷 1. Dataset yig'ish

```shell
python ./src/dataset_collector.py
```

Har bir foydalanuvchi uchun alohida papka yaratiladi:

dataset/ ali/ vali/

---

## 🧠 2. Training

```shell
python ./src/train_model.py
```

Natijalar:

- models/speaker_model.pkl

---

## 🎯 Tekshirish

```shell
python main.py
```
