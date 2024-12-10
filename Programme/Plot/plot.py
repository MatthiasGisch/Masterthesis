import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/Kunststoffgranulate 10.12.24/350_400/Nersalen.csv')
df2 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/Kunststoffgranulate 10.12.24/350_400/Papierspritzguss.csv')
df3 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/Kunststoffgranulate 10.12.24/350_400/Styrolution.csv')
df4 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/Kunststoffgranulate 10.12.24/350_400/TPU-Kork.csv')

measurements = df['Measurement']
time = df['Time']
measurements2 = df2['Measurement']
time2 = df2['Time']
measurements3 = df3['Measurement']
time3 = df3['Time']
measurements4 = df4['Measurement']
time4 = df4['Time']

# Create a line plot
plt.plot(time, measurements, color = 'blue', label = 'Nersalen')
plt.plot(time, measurements2, color = 'yellow', label = 'Papierspritzguss')
plt.plot(time, measurements3, color = 'green', label = 'Styrolution')
plt.plot(time, measurements4, color = 'red', label = 'TPU-Kork')
plt.grid(True)

plt.ylabel('Messwert')
plt.xlabel('Zeit')
plt.legend()

# Show the plot
plt.show()