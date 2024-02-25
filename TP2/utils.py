from itertools import islice
import matplotlib.pyplot as plt

def abrir_archivo_datos(path):
    with open(path) as archivo:
        datos = archivo.readlines()
        n = int(datos[0])
        e = [int(datos[i]) for i in range(1, n + 1)]
        s = [int(datos[i]) for i in range(n + 1, 2 * n + 1)]

    archivo.close()
    
    return e, s
 
def abrir_archivo_resultados_esperados(path):
    with open(path) as archivo:
        resultados=[]
        while (True):
            datos = list(islice(archivo,4))
            if not datos:
                break
            resultados.append({
                "Archivo": datos.pop(0).split("\n")[0],
                "Ganancia Máxima": int((datos.pop(0).split(":")[1]).split("\n")[0]),
                "Plan de entrenamiento":((datos.pop(0).split(":")[1]).split("\n")[0])[1:].split(", ")
            })

    archivo.close()
    
    return resultados

def plot_resultados(cantidad_dias_planeados, tiempo_implementacion_en_segundos):
    plt.figure(figsize=(20, 8))
    plt.plot(cantidad_dias_planeados, tiempo_implementacion_en_segundos, marker='o', label = "nuestro")
    plt.xlabel('Cantidad de Dias Planeados', fontsize=16)
    plt.ylabel('Tiempo de Implementación [s]', fontsize=16)
    plt.title('Cantidad de Días Vs Tiempo de Implementación', fontsize=26)
    plt.legend()
    plt.grid(True)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()