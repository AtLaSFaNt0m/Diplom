import dask.dataframe as dd

class TitanicDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ddf = dd.read_csv(self.file_path)

    def remove_column(self, column_name):
        """Удалить указанный столбец из данных."""
        if column_name in self.ddf.columns:
            self.ddf = self.ddf.drop(column_name, axis=1)
            print(f"Столбец '{column_name}' удален.")
        else:
            print(f"Столбец '{column_name}' не найден.")

    def rename_column(self, old_name, new_name):
        """Переименовать указанный столбец."""
        if old_name in self.ddf.columns:
            self.ddf = self.ddf.rename(columns={old_name: new_name})
            print(f"Столбец '{old_name}' переименован в '{new_name}'.")
        else:
            print(f"Столбец '{old_name}' не найден.")

    def sort_by_column(self, column_name):
        """Сортировать данные по указанному столбцу."""
        if column_name in self.ddf.columns:
            self.ddf = self.ddf.sort_values(by=column_name)
            print(f"Данные отсортированы по столбцу '{column_name}'.")
        else:
            print(f"Столбец '{column_name}' не найден.")

    def save_to_csv(self, output_file_path):
        """Сохранить обработанные данные в CSV."""
        self.ddf.to_csv(output_file_path, single_file=True, index=False)
        print("Данные успешно сохранены.")

    def get_summary(self):
        """Получить сводную информацию о данных."""
        return self.ddf.describe().compute()


class DataFilter:
    """Класс для фильтрации данных."""
    def __init__(self, ddf):
        self.ddf = ddf

    def filter_by_condition(self, column_name, condition):
        """Фильтровать данные по указанному условию."""
        filtered_ddf = self.ddf[self.ddf[column_name] == condition]
        print(f"Отфильтровано по условию '{column_name} == {condition}'.")
        return filtered_ddf


class DataAggregator:
    """Класс для агрегации данных."""
    def __init__(self, ddf):
        self.ddf = ddf

    def group_by(self, column_name):
        """Группировка данных по указанному столбцу."""
        grouped_ddf = self.ddf.groupby(column_name).size().compute()
        print(f"Данные сгруппированы по столбцу '{column_name}'.")
        return grouped_ddf


class MissingValueHandler:
    """Класс для обработки пропущенных значений."""
    def __init__(self, ddf):
        self.ddf = ddf

    def fill_missing_values(self, column_name, value):
        """Заполнить пропущенные значения в указанном столбце."""
        if column_name in self.ddf.columns:
            self.ddf[column_name] = self.ddf[column_name].fillna(value)
            print(f"Пропущенные значения в '{column_name}' заполнены значением '{value}'.")
        else:
            print(f"Столбец '{column_name}' не найден.")

    def drop_missing_values(self):
        """Удалить строки с пропущенными значениями."""
        initial_length = len(self.ddf)
        self.ddf = self.ddf.dropna()
        print(f"Удалены строки с пропущенными значениями. Осталось строк: {len(self.ddf)} из {initial_length}.")


def create_processor():
    """Создать экземпляр TitanicDataProcessor."""
    file_path = r"A:\Abobapy\DiplomProject\MainProject\Data\titanic\titanic.csv"
    return TitanicDataProcessor(file_path)
