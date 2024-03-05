import argparse
from pathlib import Path

from hitting_set_bt import *
from hitting_set_ple import *
from hitting_set_greedy import *
from utils import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="TDA",
        description='Trabajo Práctico Nro 3 (Main)'
    )

    parser.add_argument("--archivo_datos", help="Path al archivo que contiene los datos con el formato de la catedra.", nargs='?', default=False, type=Path)
    parser.add_argument("--archivo_resultados", help="Path al archivo que contiene los resultados con el formato de la catedra.", nargs='?', default=False, type=Path)

    args = parser.parse_args()

    archivo_datos = args.archivo_datos
    archivo_resultados = args.archivo_resultados

    jugadoresPorPeriodistas = abrir_archivo_datos(archivo_datos)
    resultadosEsperados = abrir_archivo_resultados_esperados(archivo_resultados)

    solucion = []
    solucion_actual = []
    hitting_set_bt(jugadoresPorPeriodistas, 0, solucion_actual, solucion)
    print("La ejecucion para HittingSet (Backtracking) dio ", solucion)
    print("La ejecucion para HittingSet (PLE) dio ", hitting_set_PLE(jugadoresPorPeriodistas))
    print("La ejecucion para HittingSet (Greedy) dio ", hitting_set_greedy(jugadoresPorPeriodistas))