from settings.settings import create_processor, DataFilter, DataAggregator, MissingValueHandler

def main():
    # Создание экземпляра обработчика данных
    processor = create_processor()

    # Пример использования функций
    processor.remove_column('Name')
    processor.rename_column('Sex', 'Gender')
    processor.sort_by_column('Age')

    # Фильтрация данных
    filter_processor = DataFilter(processor.ddf)
    filtered_data = filter_processor.filter_by_condition('Gender', 'female')

    # Сохранение отфильтрованных данных в новый файл
    output_file_filtered = r"A:\Abobapy\DiplomProject\MainProject\Dask\titanic_filtered.csv"
    filter_processor.ddf = filtered_data  # Обновляем Dask DataFrame с отфильтрованными данными
    processor.save_to_csv(output_file_filtered)

    # Аггрегация данных
    aggregator = DataAggregator(processor.ddf)
    group_data = aggregator.group_by('Gender')
    print("Группировка по полу:")
    print(group_data)

    # Обработка пропущенных значений
    missing_value_handler = MissingValueHandler(processor.ddf)
    missing_value_handler.fill_missing_values('Age', 30)  # Заполняем пропущенные значения в 'Age' значением 30
    missing_value_handler.drop_missing_values()  # Удаляем строки с пропущенными значениями

    # Сохранение обработанных данных в новый файл
    output_file_path = r"A:\Abobapy\DiplomProject\MainProject\Dask\titanic_processed.csv"
    processor.save_to_csv(output_file_path)

    # Получение сводной информации
    summary = processor.get_summary()
    print("Сводная информация о данных:")
    print(summary)

if __name__ == "__main__":
    main()
