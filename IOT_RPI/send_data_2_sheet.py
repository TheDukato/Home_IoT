import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Funkcja do autoryzacji i połączenia z Google Sheets
def authenticate_google_sheets(credentials_file):
    # Zakresy wymagane do pracy z Google Sheets API
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    
    # Autoryzacja za pomocą pliku JSON z danymi uwierzytelniającymi
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scopes)
    client = gspread.authorize(creds)
    
    return client

# Funkcja do odczytu danych z pliku backup.txt
def read_backup_file(backup_file):
    # Wyrażenie regularne do wyodrębnienia daty, adresu MAC oraz stanu licznika
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*MAC: ([0-9A-F]{10,14}).*Total: (\d+.\d+)')
    
    entries = []
    
    with open(backup_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        match = pattern.search(line)
        if match:
            date_str = match.group(1)
            mac_address = match.group(2)
            total = float(match.group(3))
            entries.append((date_str, mac_address, total))
    
    return entries

# Funkcja do wysyłania danych do Google Sheets
def send_data_to_sheets(sheet_id, data, client):
    sheet = client.open_by_key(sheet_id).sheet1
    existing_data = sheet.get_all_values()
    # Dodaj nagłówki (jeśli jeszcze nie istnieją)
    headers = ['Data', 'Adres MAC', 'Stan licznika']
    if not existing_data or existing_data[0] != headers:
        # Jeśli brak danych lub nagłówków w pierwszym wierszu, dodaj nagłówki
        sheet.insert_row(headers, 1)  # Dodaj nagłówki w pierwszym wierszu
    
    # Dodaj dane
    for entry in data:
        sheet.append_row(entry)

# Główna funkcja do uruchomienia programu
def main():
    # Wskazanie pliku z danymi i pliku z danymi uwierzytelniającymi
    backup_file = 'backup_important.txt'
    credentials_file = '/home/kamil/REPO/Home_IoT/IOT_RPI/massive-capsule-441311-v7-bdf3228a5a0c.json'  # Podaj ścieżkę do pliku JSON z danymi uwierzytelniającymi
    
    # ID arkusza Google Sheets (znajdziesz je w URL arkusza)
    sheet_id = '12bqE9exr-ko6KE-W2obp4_3IjaJ7WixCrH-Wu0D-O2I'  # Podaj identyfikator arkusza Google Sheets
    
    # Autoryzacja do Google Sheets
    client = authenticate_google_sheets(credentials_file)
    
    # Odczytaj dane z pliku backup.txt
    data = read_backup_file(backup_file)
    
    # Jeśli dane są dostępne, wyślij je do Google Sheets
    if data:
        send_data_to_sheets(sheet_id, data, client)
        print("Dane zostały wysłane do Google Sheets.")
    else:
        print("Brak danych do wysłania.")

# Uruchomienie programu
if __name__ == '__main__':
    main()
