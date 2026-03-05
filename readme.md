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

```bash
python -m venv venv
.\venv\Scripts\activate
```

Paketlarni o'rnatish:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📷 1. Dataset yig'ish

```bash
python ./src/dataset_collector.py
```

Har bir foydalanuvchi uchun alohida papka yaratiladi:

dataset/ ali/ vali/

---

## 🧠 2. Training

```bash
python ./src/train_model.py
```

Natijalar:

- models/speaker_model.pkl

---

## 🎯 Tekshirish

```bash
python main.py
```
