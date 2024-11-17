from variable import counters
# Definiowanie ścieżek do plików
#counters = [
#    {
#        "name": "L1",
#        "counter_file": "/home/kamil/IOT/node-red/counter_1.txt",
#        "sensor_file": "/home/kamil/IOT/node-red/sensor_1.txt",
#        "meter_constant": 2500
#    },
#    {
#        "name": "L2",
#        "counter_file": "/home/kamil/IOT/node-red/counter_2.txt",
#        "sensor_file": "/home/kamil/IOT/node-red/sensor_2.txt",
#        "meter_constant": 1000
#    },
#    {
#        "name": "L3",
#        "counter_file": "/home/kamil/IOT/iNode/counter_3.txt",
#        "sensor_file": "/home/kamil/IOT/iNode/sensor_3.txt",
#        "meter_constant": 10000
#    }
#]

# Funkcja do odczytu liczby z pliku
def read_number_from_file(file_path):
#    try:
     with open(file_path, 'r') as file:
         return float(file.read().strip())
#    except FileNotFoundError:
#        with open(file_path, 'w') as file:
#            file.write('0')
#        return 0  # Jeśli plik nie istnieje, zakładamy, że jego zawartość to 0
#    except ValueError:
#        return 0  # Jeśli w pliku nie ma liczby, również zakładamy 0

# Funkcja do liczenia liczby wystąpień '1' w pliku
def count_ones_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content.count('1')
    except FileNotFoundError:
        return 0

for counter in counters:
    # Odczytanie aktualnej wartości licznika i liczby '1' w sensorze
    counter_value = read_number_from_file(counter['counter_file'])
    ones_count = count_ones_in_file(counter['sensor_file'])

    # Obliczanie nowej wartości licznika
    print(f"Stara wartosc miernika {counter_value}")
    print(f"Liczba jedynek {ones_count}, stala{counter['meter_constant']}, ich iloczyn {ones_count / counter['meter_constant']}")
    result = counter_value + (ones_count / counter['meter_constant'])
    print(f"Nowa wartosc miernika {result}")
    # Zapisanie wyniku do pliku counter_1.txt
    with open(counter['counter_file'], 'w') as file:
        file.write(str(result))

    # Zresetowanie pliku sensor_1.txt (ustawienie na 0)
    with open(counter['sensor_file'], 'w') as file:
        file.write('0')

    print(f"Nowa wartość licznika {counter['name']}: {result}")
