import csv

avg_measurement_sensor1 = 0

with open("C:/Users/matth/Desktop/Masterthesis/Messungen/13.11.2024 Roboterzelle/Testmessung2/Leer.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei)

    zeilennummer = 0
    for row in csv_reader_object:

        if zeilennummer == 0:
            print(f'Spaltennamen sind: {", ".join(row)}')
        else:
            print(f'- Label: {row[0]} \t| Time: {row[1]} \t| SensorNr: {row[2]} \t| Identifier: {row[3]} \t| Interval: {row[4]} \t| Measurement: {row[5]} \t| Iteration: {row[6]}')
        zeilennummer += 1

    for row in csv_reader_object:

        if {row[2]} == 1:
            avg_measurement_sensor1 += {row[5]}

        print(avg_measurement_sensor1)

    avg_measurement_sensor1
    print(f'Durchschnittswert Sensor 1: {avg_measurement_sensor1}')

    print(f'Anzahl Datensätze: {zeilennummer-1}')