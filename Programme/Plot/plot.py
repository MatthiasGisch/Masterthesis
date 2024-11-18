import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('Messungen/PU-Schaum BASF 18.11.2024/644-2.csv', sep=';')
df2 = pd.read_csv('Messungen/PU-Schaum BASF 18.11.2024/645-2.csv', sep=';')
df3 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/13.11.2024 Roboterzelle/Testmessung2/WasserEssig.csv')
df4 = pd.read_csv('C:/Users/matth/Desktop/Masterthesis/Messungen/13.11.2024 Roboterzelle/Testmessung2/Papierspritzguss.csv')

measurements = df['Measurement']
time = df['Time']
measurements2 = df2['Measurement']
time2 = df2['Time']
#measurements3 = df3['Measurement']
#time3 = df3['Time']
#measurements4 = df4['Measurement']
#time4 = df4['Time']

# Create a line plot
plt.plot(time, measurements, color = 'blue', label = '644-2')
plt.plot(time, measurements2, color = 'red', label = '645-2')
#plt.plot(time, measurements3, color = 'green', label = 'WasserEssig')
#plt.plot(time, measurements4, color = 'yellow', label = 'Papierspritzguss')
plt.grid(True)

plt.ylabel('Messwert')
plt.xlabel('Zeit')
plt.legend()

# Show the plot
plt.show()