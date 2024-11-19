import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Zeitreihendaten
data = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/PU Schaum BASF 18.11.2024 Durchgang 2/645-2.csv')
df = pd.DataFrame(data, columns=["Measurement"])

df["AirQuality"] = (df["Measurement"] > 10000).astype(int)  # Gute Luft = 1, Schlechte Luft = 0

# Features und Ziel
X = df["Measurement"]
y = df["AirQuality"]  # Für Klassifikation

# Aufteilen in Training und Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# SVM-Modell erstellen
svm = SVC(kernel="rbf", C=1.0, gamma="scale")

# Modell trainieren
svm.fit(X_train, y_train)

# Vorhersagen
y_pred = svm.predict(X_test)

# Modellbewertung
accuracy = accuracy_score(y_test, y_pred)
print(f"Genauigkeit: {accuracy}")

# Vergleich der tatsächlichen Werte und Vorhersagen
plt.scatter(range(len(y_test)), y_test, label="Tatsächliche Werte", color="blue")
plt.scatter(range(len(y_pred)), y_pred, label="Vorhergesagte Werte", color="red")
plt.legend()
plt.title("SVM Regression: Tatsächlich vs Vorhersage")
plt.show()