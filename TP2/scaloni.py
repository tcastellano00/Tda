import numpy as np
import time
import os
import sys
from utils import *

#Adaptamos el problema comparandolo con el de la mochila
#max(max(G[w-2,j])+min(ei,s1),G[w-1,j-1] +min (ei, sj))
#max(G[n-1,W];G[n-1,W-P]+Vi)


def scaloni( d, e, s): 
    G = [[0 for x in range(d + 1)] for x in range(d + 1)] 
    
    G[1][1] = min(e[0], s[0])

    for i in range(1, d + 1):
        for j in range(1,d + 1):
            if i == 0 or j == 0 or (j > i):
                G[i][j] = 0
            else:
                G[i][j] = max(min(e[i-1],s[j-1]) + G[i-1][j-1], min(e[i-1],s[0]) + max(G[i-2]))

    return G

def reconstruccion_scaloni(G, p, e, s):
    res = ["Descanso" for x in range(len(e))]
    i = len(e)
    while (i> 1):
        if max(G[i-2]) + min(e[i-1], s[p-1]) == G[i][p]:
            p = G[i-2].index(max(G[i-2])) + 1
            res[i-1] = "Entreno"
            i -= 1
        elif(p!=0):
            res[i-1]="Entreno"
        
        p -= 1
        i -= 1

    if G[2][1]+min(e[2],s[2]) !=G[3][p+2]:
        res[0]="Entreno"

    return (res)
 
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
    
    resultados_dados = abrir_archivos_resultados_esperados(
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
    
