from variable import counters

# Funkcja do odczytu liczby z pliku
def read_number_from_file(file_path):
     with open(file_path, 'r') as file:
         return float(file.read().strip())

# Funkcja do liczenia liczby wystąpień '1' w pliku
def count_ones_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content.count('1')
    except FileNotFoundError:
        return 0

for counter in counters:
    if counter["sensor_type"] != "Digital_RPI_Energy_Meter":
        continue 
    # Odczytanie aktualnej wartości licznika i liczby '1' w sensorze
    ones_count = count_ones_in_file(counter['sensor_file'])
    if ones_count == 0:
        print(f"ones_count is 0, skipping...")
        continue
    counter_value = read_number_from_file(counter['counter_file'])

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

    print(f"Nowa wartość licznika {counter['name']}: {result}\n\n")
