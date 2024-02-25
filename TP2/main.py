import argparse
from pathlib import Path

from scaloni import *


def ejecutar_datos_propios(archivo_datos, archivo_resultados):
    if (not archivo_datos.exists()):
        print("El archivo ", archivo_datos, " no existe o el path fue mal ingresado")
        return
    
    if (not archivo_resultados.exists()):
        print("El archivo ", archivo_resultados, " no existe o el path fue mal ingresado")
        return
    
    print("Datos: ", archivo_resultados, ", Resultados: ", archivo_resultados)

    #Obtenemos los resultados esperados para luego compararlos
    resultados_esperados = abrir_archivo_resultados_esperados(archivo_resultados)[0]
    ganancia_maxima_esperada = resultados_esperados["Ganancia Máxima"]
    entrenamiento_esperado = resultados_esperados["Plan de entrenamiento"]

    #Ejecutamos la planificacion de scaloni.
    e, s = abrir_archivo_datos(archivo_datos)
    d = len(e)
    G = scaloni(d, e, s)
    P = np.matrix(G)
    p, j = np.unravel_index(P.argmax(), P.shape)
    entrenamiento_obtenido = reconstruccion_scaloni(G, j, e, s)
    
    #Prints para feedback al usuario.
    valor_maximo = P.max()
    print("El máximo valor es: ", valor_maximo)
    print("El plan de Entrenamiento es: ", entrenamiento_obtenido)
    
    #Chequeamos si coincide.
    print("")
    if (ganancia_maxima_esperada == valor_maximo and 
        entrenamiento_esperado == entrenamiento_obtenido):
        print("Los datos obtenidos coinciden con los datos esperados!")
    else:
        print("Algo salio mal, los datos obtenidos no coinciden con los datos esperados")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="TDA",
        description='Trabajo Práctico Nro 2 (Main) - Programación Dinámica.'
    )

    parser.add_argument("--archivo_datos", help="Path al archivo que contiene los datos con el formato de la catedra.", nargs='?', default=False, type=Path)
    parser.add_argument("--archivo_resultados", help="Path al archivo que contiene los resultados con el formato de la catedra.", nargs='?', default=False, type=Path)

    args = parser.parse_args()

    archivo_datos = args.archivo_datos
    archivo_resultados = args.archivo_resultados

    ejecutar_datos_propios(archivo_datos, archivo_resultados)

