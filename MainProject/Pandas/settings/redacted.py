import pandas as pd
import os

class TableEditor:
    def __init__(self, csv_path, settings_folder):
        self.csv_path = csv_path
        self.settings_folder = settings_folder
        self.df = pd.read_csv(self.csv_path)

        # Создание папки settings, если она не существует
        os.makedirs(self.settings_folder, exist_ok=True)

    def delete_column(self, column_name):
        """Удаление столбца из таблицы и сохранение обновленного файла"""
        if column_name in self.df.columns:
            self.df.drop(columns=[column_name], inplace=True)
            updated_path = os.path.join(self.settings_folder, 'table_without_{}.csv'.format(column_name))
            self.df.to_csv(updated_path, index=False)
            return updated_path
        else:
            raise ValueError(f"Столбец '{column_name}' не найден в таблице.")

    def rename_column(self, old_name, new_name):
        """Переименование столбца в таблице и сохранение обновленного файла"""
        if old_name in self.df.columns:
            self.df.rename(columns={old_name: new_name}, inplace=True)
            updated_path = os.path.join(self.settings_folder, 'table_with_renamed_{}_to_{}.csv'.format(old_name, new_name))
            self.df.to_csv(updated_path, index=False)
            return updated_path
        else:
            raise ValueError(f"Столбец '{old_name}' не найден в таблице.")

    def save_table(self):
        """Сохранение текущего состояния таблицы"""
        saved_path = os.path.join(self.settings_folder, 'modified_table.csv')
        self.df.to_csv(saved_path, index=False)
        return saved_path
