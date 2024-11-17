from variable import counters
import re
from datetime import datetime

# Funkcja do odczytu i analizy danych
def process_meter_data(sensor_file, counter_file):
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*MAC: ([0-9A-F]{10,14}).*TOTAL: (\d+.\d+) kWh')

    # Odczyt danych z pliku
    with open(sensor_file, 'r') as f:
        lines = f.readlines()  
    # Analiza danych
    entries = []
    for line in lines:
        match = pattern.search(line)
        if match:
            date_str = match.group(1)
            mac_address = match.group(2)
            total = float(match.group(3))
            entries.append((date_str, mac_address, total))
    with open(sensor_file, 'w') as f:
        f.write("")

    # Jeśli dane są dostępne, wybierz najnowszy wpis
    if entries:
        # Zamień stringi dat na obiekty datetime, aby porównać
        entries.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=True)
        print(f"Najnowszy wpis: Data: {entries[0][0]}, MAC: {entries[0][1]}, Total: {entries[0][2]}")
        with open(counter_file, 'w') as f:
            f.write(f"{entries[0][2]}")
    else:
        print("Brak danych do przetworzenia.")

# Uruchomienie programu

for counter in counters:
    if counter["sensor_type"] == "iNode":
        process_meter_data(counter["sensor_file"], counter["counter_file"])
