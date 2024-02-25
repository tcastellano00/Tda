import argparse

import time
import os
import sys
from scaloni import *

def comparar_resultados(name, ganancia_maxima_obtenida, entrenamiento_obtenido, resultados_dados):
    comparacion = False

    for resultados in resultados_dados:
        if (name == resultados["Archivo"]):
            comparacion = (ganancia_maxima_obtenida == resultados["Ganancia Máxima"] and entrenamiento_obtenido == resultados["Plan de entrenamiento"])
            break

    return comparacion

def tests(mostrar_plot = False, mostrar_plan_entrenamiento = False, ejecutar_5000_test = False):
    ARCHIVO_RESULTADOS_ESPERADOS = "Resultados Esperados.txt"
    ARCHIVOS_DE_PRUEBA = [
        "3.txt",
        "10.txt",
        "10_bis.txt",
        "10_todo_entreno.txt",
        "50.txt",
        "50_bis.txt",
        "100.txt",
        "500.txt",
        "1000.txt",
        "5000.txt"
    ]
    if (not ejecutar_5000_test):
        ARCHIVOS_DE_PRUEBA.pop()
    
    path_carpeta_datos = os.path.dirname(os.path.abspath(sys.argv[0])) + "/Datos/"
    cantidad_dias_planeados = []
    tiempo_ejecucion_en_segundos = []
    
    resultados_dados = abrir_archivo_resultados_esperados(
        path_carpeta_datos + ARCHIVO_RESULTADOS_ESPERADOS
    )

    for archivo_prueba in (ARCHIVOS_DE_PRUEBA):
        e,s = abrir_archivo_datos(
            path_carpeta_datos + archivo_prueba
        )
        d = len(e)
        cantidad_dias_planeados.append(d)
        
        # Medimos cuanto demora en calcular.
        start = time.perf_counter()
        G = scaloni(d, e, s)
        end = time.perf_counter()
        tiempo_ejecucion = end - start
        tiempo_ejecucion_en_segundos.append(tiempo_ejecucion)

        P = np.matrix(G)
        p, j = np.unravel_index(P.argmax(), P.shape)
        entrenamiento_obtenido = reconstruccion_scaloni(G, j, e, s)
        
        #Prints para feedback al usuario.
        valor_maximo = P.max()
        print("El archivo analizado es: ", archivo_prueba, ". Su máximo es: ", valor_maximo)

        if (mostrar_plan_entrenamiento):
            print("El plan de Entrenamiento es: ", entrenamiento_obtenido)
        
        print("Si lo comparamos con los datos dados es", 
              comparar_resultados(archivo_prueba, valor_maximo, entrenamiento_obtenido, resultados_dados), 
              "que se cumple lo esperado")

        if (mostrar_plot):
            print("Se tardó", end-start, "segundos en realizar el análisis")

    #Graficamos resultados si es necesario.
    if (mostrar_plot):
        plot_resultados(cantidad_dias_planeados, tiempo_ejecucion_en_segundos)
    
    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="TDA",
        description='Trabajo Práctico Nro 2 (Test) - Programación Dinámica.'
    )

    parser.add_argument("--plot", help="Muestra un grafico con los resultados de las ejecuciones.", nargs='?', default=False, type=bool)
    parser.add_argument("--plan", help="Muestra el plan de entrenamiento calculado para cada una de las pruebas.", nargs='?', default=False, type=bool)
    parser.add_argument("--hard_test", help="Ejecuta la prueba de 5000 (precaucion, esta prueba demora segundos en ejecutarse).", nargs='?', default=False, type=bool)

    args = parser.parse_args()

    mostrar_plot = args.plot
    mostrar_plan_entrenamiento = args.plan
    ejecutar_5000_test = args.hard_test
    
    tests(mostrar_plot, mostrar_plan_entrenamiento, ejecutar_5000_test)