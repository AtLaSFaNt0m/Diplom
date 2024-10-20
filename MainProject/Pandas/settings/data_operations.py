import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import time

class DataProcessor:
    def __init__(self, csv_path, db_path, settings_folder):
        self.csv_path = csv_path
        self.db_path = db_path
        self.settings_folder = settings_folder

        # Создание папки settings, если ее нет
        os.makedirs(self.settings_folder, exist_ok=True)
        
        # Загрузка данных
        self.df = pd.read_csv(self.csv_path)

    def save_to_db(self):
        """Сохранение данных в базу данных SQLite"""
        start_time = time.time()  # Начало отсчета времени
        conn = sqlite3.connect(self.db_path)
        self.df.to_sql('titanic', conn, if_exists='replace', index=False)
        conn.close()
        end_time = time.time()  # Окончание отсчета времени
        print(f"Данные сохранены в базу данных за {end_time - start_time:.2f} секунд.")

    def sort_data_by_age(self):
        """Сортировка данных по возрасту и сохранение в CSV файл"""
        start_time = time.time()
        sorted_df = self.df.sort_values(by='Age')
        sorted_path = os.path.join(self.settings_folder, 'sorted_by_age.csv')
        sorted_df.to_csv(sorted_path, index=False)
        end_time = time.time()
        print(f"Сортировка данных по возрасту заняла {end_time - start_time:.2f} секунд.")
        return sorted_path

    def add_age_group(self):
        """Добавление возрастной группы и сохранение результата"""
        start_time = time.time()
        self.df['AgeGroup'] = pd.cut(self.df['Age'], bins=[0, 12, 18, 60, 120], labels=['Child', 'Teenager', 'Adult', 'Senior'])
        edited_path = os.path.join(self.settings_folder, 'edited_with_agegroup.csv')
        self.df.to_csv(edited_path, index=False)
        end_time = time.time()
        print(f"Добавление возрастных групп заняло {end_time - start_time:.2f} секунд.")
        return edited_path

    def plot_age_distribution_detailed(self):
        """Построение графика распределения пассажиров по каждому возрасту и сохранение"""
        # Убираем записи с отсутствующим возрастом
        age_data = self.df.dropna(subset=['Age'])

        # Подсчет количества пассажиров для каждого возраста
        age_counts = age_data['Age'].value_counts().sort_index()

        # Построение графика
        plt.figure(figsize=(12, 6))
        age_counts.plot(kind='bar', color='skyblue')
        plt.title('Number of Passengers by Age')
        plt.xlabel('Age')
        plt.ylabel('Number of Passengers')
        plt.xticks(rotation=90)  # Поворачиваем метки на оси X для лучшей читаемости
        plt.tight_layout()

        # Сохранение графика в файл
        plot_path = os.path.join(self.settings_folder, 'age_distribution_detailed.png')
        plt.savefig(plot_path)
        plt.show()
        return plot_path


# Новый класс для редактирования базы данных
class DatabaseEditor:
    def __init__(self, db_path):
        self.db_path = db_path

    def update_column(self, table_name, column_name, value, condition_column=None, condition_value=None):
        """Обновление значений в таблице базы данных"""
        start_time = time.time()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if condition_column and condition_value:
            query = f"UPDATE {table_name} SET {column_name} = ? WHERE {condition_column} = ?"
            cursor.execute(query, (value, condition_value))
        else:
            query = f"UPDATE {table_name} SET {column_name} = ?"
            cursor.execute(query, (value,))

        conn.commit()
        conn.close()
        end_time = time.time()
        print(f"Обновление столбца '{column_name}' заняло {end_time - start_time:.2f} секунд.")

    def delete_rows(self, table_name, condition_column, condition_value):
        """Удаление строк по условию"""
        start_time = time.time()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = f"DELETE FROM {table_name} WHERE {condition_column} = ?"
        cursor.execute(query, (condition_value,))
        
        conn.commit()
        conn.close()
        end_time = time.time()
        print(f"Удаление строк заняло {end_time - start_time:.2f} секунд.")

    def add_new_column(self, table_name, column_name, data_type="TEXT"):
        """Добавление нового столбца в таблицу"""
        start_time = time.time()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}"
        cursor.execute(query)
        
        conn.commit()
        conn.close()
        end_time = time.time()
        print(f"Добавление столбца '{column_name}' заняло {end_time - start_time:.2f} секунд.")
