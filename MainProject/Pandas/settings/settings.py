import pandas as pd
import os

class DataSorter:
    def __init__(self, df, settings_folder):
        self.df = df
        self.settings_folder = settings_folder

    def sort_by_column(self, column):
        """Сортировка данных по указанному столбцу и сохранение в CSV файл"""
        sorted_df = self.df.sort_values(by=column)
        sorted_path = os.path.join(self.settings_folder, f'sorted_by_{column}.csv')
        sorted_df.to_csv(sorted_path, index=False)
        return sorted_path

class DataEditor:
    def __init__(self, df, settings_folder):
        self.df = df
        self.settings_folder = settings_folder

    def add_age_group(self):
        """Добавление возрастной группы и сохранение в CSV файл"""
        self.df['AgeGroup'] = pd.cut(self.df['Age'], bins=[0, 12, 18, 60, 120], labels=['Child', 'Teenager', 'Adult', 'Senior'])
        edited_path = os.path.join(self.settings_folder, 'edited_with_agegroup.csv')
        self.df.to_csv(edited_path, index=False)
        return edited_path
