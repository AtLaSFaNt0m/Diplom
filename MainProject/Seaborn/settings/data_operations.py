class DataOperations:
    def __init__(self, data):
        self.data = data

    def add_record(self, record):
        self.data.append(record)

    def edit_record(self, index, column, value):
        if index < len(self.data) and column in self.data[index]:
            self.data[index][column] = value

    def delete_record(self, index):
        if index < len(self.data):
            del self.data[index]

    def sort_by_column(self, column, reverse=False):
        # Обработка ошибок: Преобразуем строки в числа для сортировки
        def safe_convert(value):
            try:
                return float(value) if value else None
            except ValueError:
                return None

        # Сортировка с учетом None, отправляем None в конец списка
        return sorted(
            self.data, 
            key=lambda x: (safe_convert(x.get(column)) is None, safe_convert(x.get(column))), 
            reverse=reverse
        )
