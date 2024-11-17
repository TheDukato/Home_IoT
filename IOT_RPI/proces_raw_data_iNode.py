from variable import counters
import re
from datetime import datetime

# Funkcja do odczytu i analizy danych
def process_meter_data(sensor_file, counter_file):
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*MAC: ([0-9A-F]{10,14}).*TOTAL: (\d+.\d+) kWh')

    # Odczyt danych z pliku
    with open(sensor_file, 'r') as f:
        lines = f.readlines()
    print(f"KP1 {lines}")    
    # Analiza danych
    entries = []
    for line in lines:
        print(f"KP2 {line}")
        match = pattern.search(line)
        if match:
            print(f"KP2 {line}")
            date_str = match.group(1)
            mac_address = match.group(2)
            total = float(match.group(3))
            entries.append((date_str, mac_address, total))
    print(f"KP {entries}")
    
    # Jeśli dane są dostępne, wybierz najnowszy wpis
    if entries:
        # Zamień stringi dat na obiekty datetime, aby porównać
        entries.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=True)
        print(f"entries{entries}")
        for entry in entries:
                print(f"Najnowszy wpis: Data: {entry[0]}, MAC: {entry[1]}, Total: {entry[2]}")
                with open(counter_file, 'w') as f:
                    f.write(f"{entry[2]}")


    else:
        print("Brak danych do przetworzenia.")

# Uruchomienie programu

for counter in counters:
    process_meter_data(counter["sensor_file"], counter["counter_file"])
