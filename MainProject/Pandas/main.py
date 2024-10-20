import time
import pandas as pd
from settings.data_operations import DataProcessor, DatabaseEditor
from settings.settings import DataSorter, DataEditor
from settings.redacted import TableEditor

def main():
    # Пути к файлам и папкам
    csv_path = 'A:/Abobapy/DiplomProject/MainProject/Data/titanic/titanic.csv'
    db_path = 'A:/Abobapy/DiplomProject/MainProject/Pandas/titanic.db'
    settings_folder = 'A:/Abobapy/DiplomProject/MainProject/Pandas/settings'

    # Инициализация DataProcessor
    print("Инициализация DataProcessor...")
    start_time = time.time()
    processor = DataProcessor(csv_path, db_path, settings_folder)
    end_time = time.time()
    print(f"Инициализация DataProcessor заняла {end_time - start_time:.2f} секунд.")

    # Сортировка данных по возрасту с использованием DataSorter
    print("Сортировка данных по возрасту...")
    sorter = DataSorter(processor.df, settings_folder)
    start_time = time.time()
    sorted_file = sorter.sort_by_column('Age')
    end_time = time.time()
    print(f"Сортировка данных заняла {end_time - start_time:.2f} секунд. Сохранено в: {sorted_file}")

    # Добавление возрастной группы с использованием DataEditor
    print("Добавление возрастных групп...")
    editor = DataEditor(processor.df, settings_folder)
    start_time = time.time()
    edited_file = editor.add_age_group()
    end_time = time.time()
    print(f"Добавление возрастных групп заняло {end_time - start_time:.2f} секунд. Сохранено в: {edited_file}")

    # Построение детализированного графика по возрасту
    print("Построение детализированного графика по возрасту...")
    start_time = time.time()
    plot_file = processor.plot_age_distribution_detailed()
    end_time = time.time()
    print(f"Построение графика заняло {end_time - start_time:.2f} секунд. График сохранен в: {plot_file}")

    # Инициализация TableEditor для редактирования столбцов
    print("Инициализация TableEditor...")
    start_time = time.time()
    editor = TableEditor(csv_path, settings_folder)
    end_time = time.time()
    print(f"Инициализация TableEditor заняла {end_time - start_time:.2f} секунд.")

    # Пример удаления столбца
    print("Удаление столбца 'Cabin'...")
    start_time = time.time()
    try:
        updated_file = editor.delete_column('Cabin')
        end_time = time.time()
        print(f"Удаление столбца заняло {end_time - start_time:.2f} секунд. Обновленная таблица сохранена в: {updated_file}")
    except ValueError as e:
        print(e)

    # Пример переименования столбца
    print("Переименование столбца 'Survived' в 'SurvivalStatus'...")
    start_time = time.time()
    try:
        renamed_file = editor.rename_column('Survived', 'SurvivalStatus')
        end_time = time.time()
        print(f"Переименование столбца заняло {end_time - start_time:.2f} секунд. Обновленная таблица сохранена в: {renamed_file}")
    except ValueError as e:
        print(e)

    # Сохранение текущей таблицы
    print("Сохранение текущего состояния таблицы...")
    start_time = time.time()
    saved_path = editor.save_table()
    end_time = time.time()
    print(f"Сохранение текущей таблицы заняло {end_time - start_time:.2f} секунд. Файл сохранен в: {saved_path}")

if __name__ == "__main__":
    main()
