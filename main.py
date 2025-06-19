from stats import Statistics
from utils import display_result

def main():
    data = [10, 20, 30, 40, 50, 0, 0, 0]
    stat = Statistics(data)

    print("Calculando estadísticas...")
    mean = stat.calculate_mean()
    median = stat.calculate_median()
    mode = stat.calculate_mode()
    std_dev = stat.calculate_std_dev()

    display_result(mean, median, mode, std_dev)

if __name__ == "__main__":
    main()