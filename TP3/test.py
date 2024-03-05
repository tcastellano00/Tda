import argparse
import os
import sys
import time

from hitting_set_bt import *
from hitting_set_ple import *
from hitting_set_greedy import *
from utils import *


def comparar_resultados(name, cantidad_minima_obtenida, resultados_dados):
    comparacion = False

    for resultados in resultados_dados:
        if (name == resultados["Archivo"]):
            comparacion = (cantidad_minima_obtenida == resultados["CantidadMinima"])
            break

    return comparacion

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="TDA",
        description='Trabajo Práctico Nro 3 (Test)'
    )

    ARCHIVO_RESULTADOS_ESPERADOS = "Resultados Esperados.txt"
    ARCHIVOS_DE_PRUEBA = [
        "5.txt",
        "7.txt",
        "10_pocos.txt",
        "10_todos.txt",
        "10_varios.txt",
        "15.txt",
        "20.txt",
        "50.txt",
        "75.txt",
        "100.txt",
        #"200.txt"
    ]
    
    path_carpeta_datos = os.path.dirname(os.path.abspath(sys.argv[0])) + "/Datos/"
    tiempo_ejecucion_en_segundos = []
    
    resultados_dados = abrir_archivo_resultados_esperados(
        path_carpeta_datos + ARCHIVO_RESULTADOS_ESPERADOS
    )

    for archivo_prueba in (ARCHIVOS_DE_PRUEBA):
        B = abrir_archivo_datos(
            path_carpeta_datos + archivo_prueba
        )
        
        # Medimos cuanto demora en calcular.
        solucion = []
        solucion_actual = []
        start = time.perf_counter()
        hitting_set_bt(B, 0, solucion_actual, solucion)
        end = time.perf_counter()
        tiempo_ejecucion = end - start
        tiempo_ejecucion_en_segundos.append(tiempo_ejecucion)
        
        print(archivo_prueba, " Si lo comparamos con los datos dados es", 
              comparar_resultados(archivo_prueba, len(solucion), resultados_dados), 
              "que se cumple lo esperado")