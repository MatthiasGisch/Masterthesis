import os
import sys

# Ordnerpfad definieren
data_path = sys.argv[1]

# Überprüfen, ob der Ordner existiert
if not os.path.exists(data_path):
    print(f"Der Ordner '{data_path}' existiert nicht.")
    sys.exit(1)

# Alle CSV-Dateien im Ordner auflisten
csv_files = [f for f in os.listdir(data_path) if f.endswith('.csv')]

if not csv_files:
    print(f"Keine CSV-Dateien im Ordner '{data_path}' gefunden.")
    sys.exit(1)

# Bedingung für den Dateinamen
condition = sys.argv[2]

# Neue Datei zum Speichern definieren
output_file = "merged_" + sys.argv[2] +  ".csv"

# CSV-Dateien zeilenweise verarbeiten
header_written = False  # Um den Header nur einmal zu schreiben
with open(output_file, 'w', encoding='utf-8') as outfile:
    for csv_file in csv_files:
        # Überprüfen, ob die Datei die Bedingung erfüllt
        if condition in csv_file:
            file_path = os.path.join(data_path, csv_file)
            
            # Überprüfen, ob die Datei existiert (sicherheitsbedingt)
            if not os.path.isfile(file_path):
                print(f"Datei '{file_path}' konnte nicht gefunden werden.")
                continue

            print(f"Verarbeite Datei: {file_path}")

            # Aktuelle Datei einlesen
            with open(file_path, 'r', encoding='utf-8') as infile:
                # Header prüfen und schreiben
                if not header_written:
                    header = infile.readline()  # Erste Zeile als Header
                    outfile.write(header)
                    header_written = True
                else:
                    infile.readline()  # Header überspringen
                
                # Restliche Zeilen schreiben
                for line in infile:
                    outfile.write(line)

print(f"Zusammenführung abgeschlossen. Ergebnis gespeichert in '{output_file}'.")