def display_result(mean, median, mode, std_dev):
    print("\n--- Resultados del Análisis ---")
    print("Media:", mean)
    print("Mediana:", median)
    print("Moda:", mode)
    print("Desviación Estándar:", std_dev)


def log_analysis(data, labels, balance_info):
    print("\n--- Log de Datos ---")
    print("Cantidad de datos:", len(data))
    print("Etiquetas únicas:", set(labels))
    print("Balance:", balance_info)
    # Información sensible removida para evitar riesgos de privacidad
    # print("Log de datos completo:", data, labels)
