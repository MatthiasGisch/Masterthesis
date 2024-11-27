import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/BASF 27.11.2024/644-2.csv')
df2 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/BASF 27.11.2024/644-8.csv')
df3 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/BASF 27.11.2024/645-1.csv')
df4 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/BASF 27.11.2024/645-2.csv')

measurements = df['Measurement']
time = df['Time']
measurements2 = df2['Measurement']
time2 = df2['Time']
measurements3 = df3['Measurement']
time3 = df3['Time']
measurements4 = df4['Measurement']
time4 = df4['Time']

# Create a line plot
plt.plot(time, measurements, color = 'blue', label = '644-2')
plt.plot(time4, measurements4, color = 'yellow', label = '645-2')
plt.plot(time3, measurements3, color = 'green', label = '645-1')
plt.plot(time2, measurements2, color = 'red', label = '644-8')
plt.grid(True)

plt.ylabel('Messwert')
plt.xlabel('Zeit')
plt.legend()

# Show the plot
plt.show()