import argparse

from scaloni import tests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="TDA",
        description='Trabajo Práctico Nro 2 - Programación Dinámica.'
    )

    parser.add_argument("--plot", help="Muestra un grafico con los resultados de las ejecuciones.", nargs='?', default=False, type=bool)
    parser.add_argument("--plan", help="Muestra el plan de entrenamiento calculado para cada una de las pruebas.", nargs='?', default=False, type=bool)
    parser.add_argument("--hard_test", help="Ejecuta la prueba de 5000 (precaucion, esta prueba demora segundos en ejecutarse).", nargs='?', default=False, type=bool)

    args = parser.parse_args()

    mostrar_plot = args.plot
    mostrar_plan_entrenamiento = args.plan
    ejecutar_5000_test = args.hard_test
    
    tests(mostrar_plot, mostrar_plan_entrenamiento, ejecutar_5000_test)
