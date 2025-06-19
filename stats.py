import statistics

class Statistics:
    def __init__(self, values):
        self.values = values

    def calculate_mean(self):
        return sum(self.values) / len(self.values)

    def calculate_median(self):
        if not self.values:
            return None
        return statistics.median(self.values)

    def calculate_mode(self):
        try:
            return statistics.mode(self.values)
        except:
            return "No definido"

    def calculate_std_dev(self):
        n = len(self.values)
        mean = sum(self.values) / n
        squared_diffs = []
        for x in self.values:
            squared_diffs.append((x - mean) ** 2)
        variance = sum(squared_diffs) / n
        return variance ** 0.5