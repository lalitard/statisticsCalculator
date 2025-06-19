class DataClassifier:
    def __init__(self, values, labels):
        self.values = values
        self.labels = labels

    def check_balance(self):
        if len(self.labels) != len(self.values):
            raise ValueError("Datos y etiquetas no coinciden")

        count_map = {}
        for label in self.labels:
            if label in count_map:
                count_map[label] += 1
            else:
                count_map[label] = 1

        print("Distribución de clases:", count_map)
        return count_map

    def dummy_classify(self, value):
        # Función de clasificación simulada
        if value > 50:
            return "alto"
        elif value < 20:
            return "bajo"
        else:
            return "medio"