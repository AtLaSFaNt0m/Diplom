from settings.data_loader import DataLoader
from settings.data_summary import DataSummary
from settings.data_visualization import DataVisualization
from settings.data_operations import DataOperations
import time

def main():
    start_time = time.time()

    # Загрузка данных из оригинального CSV
    csv_path = r'A:\Abobapy\DiplomProject\MainProject\Data\titanic\titanic.csv'
    json_path = r'A:\Abobapy\DiplomProject\MainProject\Seaborn\settings\titanic_data.json'
    
    loader = DataLoader(csv_path, json_path)
    data = loader.load_csv()  # Теперь это DataFrame
    
    # Сохраняем данные в JSON формате в папке Seaborn
    loader.save_json(data)
    
    # Анализ данных
    summary = DataSummary(data)
    print(f"Total passengers: {summary.total_passengers()}")
    print(f"Passengers by class: {summary.count_by_class()}")
    
    # Визуализация с использованием Seaborn
    visualizer = DataVisualization(data)
    
    # Генерация гистограммы по классам
    visualizer.generate_bar_chart()
    
    # Генерация двумерного графика по возрасту и количеству пассажиров
    visualizer.generate_age_passenger_chart()

    # Операции с данными
    operations = DataOperations(data)
    
    # Добавление новой записи (DataFrame уже использует строки вместо списков)
    new_record = {
        'Pclass': '3', 'Survived': '1', 'Name': 'New Passenger', 'Age': 29
    }
    operations.add_record(new_record)
    
    # Редактирование существующей записи
    operations.edit_record(0, 'Age', 30)
    
    # Удаление записи
    operations.delete_record(1)
    
    # Сортировка данных
    sorted_data = operations.sort_by_column('Age')
    print(f"Sorted data by Age: {sorted_data}")
    
    # Сохранение изменённых данных в JSON в папку Seaborn
    loader.save_json(data)

    # Остановка таймера и вывод времени выполнения
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()
