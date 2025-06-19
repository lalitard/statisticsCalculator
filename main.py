from stats import Statistics
from classifier import DataClassifier
from utils import display_result, log_analysis




def main():
    data = [10, 20, 30, 40, 50, 0, 0, 0, 100, -20, -20, 100]
    labels = ["bajo", "bajo", "medio", "medio", "alto", "bajo", "bajo", "bajo", "muy alto", "muy bajo", "muy bajo", "muy alto"]

    stat = Statistics(data)
    classifier = DataClassifier(data, labels)

    print("--- INICIO DEL ANÁLISIS ---")

    mean = stat.calculate_mean()
    median = stat.calculate_median()
    mode = stat.calculate_mode()
    std_dev = stat.calculate_std_dev()

    try:
        class_balance = classifier.check_balance()
    except ValueError as ve:
        class_balance = f"Error analizando clases: {str(ve)}"

    display_result(mean, median, mode, std_dev)
    log_analysis(data, labels, class_balance)

    # eval("print('Fin de ejecución')")  # Eliminado por seguridad
    print("Fin de ejecución")

if __name__ == "__main__":
    main()