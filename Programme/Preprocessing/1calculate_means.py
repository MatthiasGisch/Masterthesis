import os
import sys
import pandas as pd

# Ordner mit den CSV-Dateien
input_folder = sys.argv[1]  # Ersetze mit deinem Eingabeordner
output_folder = sys.argv[1] + "/calculated_means"  # Neuer Ordner für die Ergebnisse

# Sicherstellen, dass der Ausgabeordner existiert
os.makedirs(output_folder, exist_ok=True)

# Alle CSV-Dateien im Eingabeordner auflisten
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

for csv_file in csv_files:
    # Datei einlesen
    file_path = os.path.join(input_folder, csv_file)
    data = pd.read_csv(file_path, delimiter=';')
    
    # Mittelwerte für bestimmte Spalten berechnen
    mean_columns = data.columns[4:-1]  # Spalten 4 bis zur vorletzten Spalte auswählen
    data['Mean'] = data[mean_columns].mean(axis=1)
    
    # Ergebnis zusammensetzen
    first_twelve_columns = data.iloc[:, :12]
    remaining_columns = data.iloc[:, 12:]
    result = remaining_columns
    result['Mean'] = data['Mean']  # Berechneten Mittelwert hinzufügen
    
    # Neue Datei im Ausgabeordner speichern
    output_file = os.path.join(output_folder, f"calculated_means_{csv_file}")
    result.to_csv(output_file, index=False, sep=';')