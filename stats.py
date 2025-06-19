import statistics
import math

class Statistics:
    def __init__(self, values):
        self.values = values

    def calculate_mean(self):
        if len(self.values) == 0:
            return "Error: Lista vacía"
        return sum(self.values) / len(self.values)

    def calculate_median(self):
        return statistics.median(self.values)

    def calculate_mode(self):
        try:
            return statistics.mode(self.values)
        except:
            return "Múltiples modas o no definida"

    def calculate_std_dev(self):
        n = len(self.values)
        if n == 0:
            return None
        mean = sum(self.values) / n
        squared_diffs = [(x - mean) ** 2 for x in self.values]
        variance = sum(squared_diffs) / n
        return math.sqrt(variance)