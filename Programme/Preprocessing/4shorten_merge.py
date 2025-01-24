import csv
import sys

input_file = "merged_" + sys.argv[1] + ".csv"
output_file = "shortened_merge_" + sys.argv[1] + ".csv"

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    
    # Länge der ersten Zeile bestimmen
    first_row = next(reader)
    target_length = len(first_row)
    
    # Alle Zeilen kürzen
    shortened_rows = [first_row]  # Erste Zeile bleibt unverändert
    for row in reader:
        shortened_rows.append(row[:target_length])  # Zeilen auf Ziel-Länge kürzen

# Gekürzte Zeilen in eine neue Datei schreiben
with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(shortened_rows)

print("Merge wurde gekürzt.")