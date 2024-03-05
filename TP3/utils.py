from itertools import islice

def abrir_archivo_datos(path):
    with open(path) as archivo:
        datos = archivo.readlines()
        jugadores = []
        for dato in datos:
            jugadores.append(dato.strip().split(","))
    archivo.close()
    
    return jugadores
 
def abrir_archivo_resultados_esperados(path):
    with open(path) as archivo:
        resultados=[]
        while (True):
            datos = list(islice(archivo, 3))
            if not datos:
                break

            resultados.append({
                "Archivo": datos.pop(0).split("\n")[0],
                "CantidadMinima": int((datos.pop(0).split(":")[1]).split(" (")[0])
            })

    archivo.close()
    
    return resultados