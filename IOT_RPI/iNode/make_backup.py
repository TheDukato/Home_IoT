import re
from datetime import datetime

input_file = 'meter_data.txt'
backup_all_file = 'backup_all.txt'
backup_important_file = 'backup_important.txt'

# Funkcja do odczytu i analizy danych
def process_meter_data(input_file, backup_all_file):
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*MAC: ([0-9A-F]{10,14}).*TOTAL: (\d+.\d+) kWh')

    # Odczyt danych z pliku
    with open(input_file, 'r') as f:
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
            total = float(match.group(3))#####################Potencial issue KP
            entries.append((date_str, mac_address, total))
    print(f"KP {entries}")
    # Zapisz dane do backup.txt
    with open(backup_all_file, 'a') as f:
        f.writelines(lines)
    
    # Jeśli dane są dostępne, wybierz najnowszy wpis
    if entries:
        # Zamień stringi dat na obiekty datetime, aby porównać
        entries.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=True)
        print(f"entries{entries}")
        #znalezienie wszystkich urządzeń w odczytach na podstawie adresu mac
        devices = []
        for entry in entries:
            if entry[1] not in devices:
                devices.append(entry[1])
                print(f"Najnowszy wpis: Data: {entry[0]}, MAC: {entry[1]}, Total: {entry[2]}")
                with open(backup_important_file, 'a') as f:
                    f.write(f"{entry[0]}, MAC: {entry[1]}, Total: {entry[2]}\n")


    else:
        print("Brak danych do przetworzenia.")

# Uruchomienie programu
process_meter_data(input_file, backup_all_file)
