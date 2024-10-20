class DataSummary:
    def __init__(self, data):
        self.data = data

    def total_passengers(self):
        return len(self.data)

    def count_by_class(self):
        classes = {}
        for row in self.data:
            pclass = row['Pclass']
            classes[pclass] = classes.get(pclass, 0) + 1
        return classes
