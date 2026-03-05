import os
import pickle
from sklearn.svm import SVC
from feature_extraction import extract_features

X = []
y = []

dataset_path = "dataset"

for person in os.listdir(dataset_path):

    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    for file in os.listdir(person_path):

        file_path = os.path.join(person_path, file)

        features = extract_features(file_path)

        X.append(features)
        y.append(person)

model = SVC(probability=True)

model.fit(X, y)

# models papkasini yaratish
os.makedirs("models", exist_ok=True)

with open("models/speaker_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saqlandi: models/speaker_model.pkl")