from TP2TDA2 import comparaciones

if __name__ == '__main__': 
    x_name=["3.txt","10.txt","10_bis.txt","10_todo_entreno.txt", "50.txt","50_bis.txt","100.txt","500.txt","1000.txt","5000.txt"]
    resultados_dados="Resultados Esperados.txt"
    plt_time=False #Si no se desea graficar la complejidad temporal cambiar a False
    No_calculate_5000= True #Si no se desea calcular el set de 5000 cambiar a True
    obtener_Plan_entrenamiento= False #Si se desea Obtener el Plan de entrenamiento para cada archivo cambiar a True
    comparaciones(x_name, resultados_dados, plt_time,No_calculate_5000,obtener_Plan_entrenamiento)
