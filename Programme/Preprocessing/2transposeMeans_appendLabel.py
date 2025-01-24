import os
import sys
import pandas as pd

# Eingabe- und Ausgabeordner definieren
input_folder = sys.argv[1] + "/calculated_means"
output_folder = sys.argv[1] + "/calculated_means" + "/transposed_labeled"
step_size = int(sys.argv[2])

# Ausgabeordner erstellen, falls er nicht existiert
os.makedirs(output_folder, exist_ok=True)

# Alle CSV-Dateien im Eingabeordner auflisten
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Dateien verarbeiten
for csv_file in csv_files:
    file_prefix = os.path.splitext(csv_file)[0]  # Dateiname ohne Erweiterung
    
    # Eingabedatei einlesen
    file_path = os.path.join(input_folder, csv_file)
    data = pd.read_csv(file_path, skiprows=1, delimiter=';')

    # Zeilenweise Kombination
    rows_combined = []
    for i in range(0, len(data), step_size):
        block = data.iloc[i:i+step_size].values.flatten()  # Block extrahieren und flach machen
        rows_combined.append(block)

    # In DataFrame umwandeln
    new_df = pd.DataFrame(rows_combined)
    new_df.insert(0, 'Prefix', [file_prefix] * len(new_df))

    # Ergebnis speichern
    output_file = os.path.join(output_folder, f"transposed_labeled_means_{file_prefix}.csv")
    new_df.to_csv(output_file, index=False, header=False)