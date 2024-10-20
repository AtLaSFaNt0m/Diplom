import csv
import json

class DataLoader:
    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path  # Путь к оригинальному файлу CSV
        self.json_path = json_path  # Путь для сохранения отредактированных данных

    def load_csv(self):
        data = []
        with open(self.csv_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def save_json(self, data):
        with open(self.json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

    def load_json(self):
        with open(self.json_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
