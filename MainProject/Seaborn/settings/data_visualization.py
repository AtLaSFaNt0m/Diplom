import seaborn as sns
import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, data):
        self.data = data
        sns.set(style="whitegrid")  # Устанавливаем стиль графиков

    def generate_bar_chart(self):
        # Извлекаем данные о пассажирских классах вручную
        pclass_data = [row['Pclass'] for row in self.data if 'Pclass' in row]
        
        # Строим график на основе списка значений
        plt.figure(figsize=(12, 6))  # Широкое окно для графика
        sns.countplot(x=pclass_data, palette="Blues_d")  # Добавляем цветовую палитру
        plt.title('Passengers by Class', fontsize=16, fontweight='bold')  # Заголовок
        plt.xlabel('Passenger Class', fontsize=14)  # Подпись оси X
        plt.ylabel('Count', fontsize=14)  # Подпись оси Y
        plt.xticks(fontsize=12, rotation=0)  # Оставляем горизонтальные метки оси X
        plt.yticks(fontsize=12)  # Размер шрифта для меток оси Y
        plt.tight_layout()  # Упорядочиваем график
        plt.show()

    def generate_age_passenger_chart(self):
        # Извлекаем данные по возрасту и сортируем их
        age_data = sorted([row['Age'] for row in self.data if 'Age' in row and row['Age'] is not None])
        
        # Строим график распределения по возрасту
        plt.figure(figsize=(12, 6))  # Широкое окно для графика
        sns.histplot(age_data, bins=10, kde=True, color="purple")  # Добавляем KDE и настраиваем цвет
        plt.title('Number of Passengers by Age', fontsize=16, fontweight='bold')  # Заголовок
        plt.xlabel('Age', fontsize=14)  # Подпись оси X
        plt.ylabel('Number of Passengers', fontsize=14)  # Подпись оси Y
        plt.xticks(fontsize=12, rotation=90)  # Вращаем метки оси X на 90 градусов
        plt.yticks(fontsize=12)  # Размер шрифта для меток оси Y
        plt.tight_layout()  # Упорядочиваем график
        plt.show()
