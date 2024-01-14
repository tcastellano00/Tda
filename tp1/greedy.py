import random
import time

def calcularTiempoMaximo(n, tiempoScaloni, tiempoAyudantes, debug=True, showElapsedTime=False):
    if (n <= 0):
        return
    
    start = time.perf_counter()
    #plotTime=[]
    tiempoScaloniAyudantes = []
    for i in range(0, n):
         tiempoScaloniAyudantes.append((tiempoScaloni[i], tiempoAyudantes[i]))
    
    # Complejidad O(nlogn)
    tiempoScaloniAyudantes.sort(key=lambda tup: tup[1], reverse=True)

    tiempoEnFinalizarAyudante = []
    tiempoAcumuladoScaloni = 0

    # Complejidad O(n)
    for tiempo in tiempoScaloniAyudantes:
        tiempoScaloni = tiempo[0]
        tiempoAyudante = tiempo[1]

        tiempoEnFinalizarAyudante.append(tiempoScaloni + tiempoAyudante + tiempoAcumuladoScaloni)

        tiempoAcumuladoScaloni += tiempoScaloni

    end = time.perf_counter()

    if (showElapsedTime):
        print((n, end - start))
        #plotTime.append(n,end - start)

    if (debug):
        print("Lo que demora cada ayudante en terminar de ver su video es: ")
        print(tiempoEnFinalizarAyudante)

        print("El tiempo que se demora terminar de ver todos los videos es: ", max(tiempoEnFinalizarAyudante))

#Tests
videosAMirarScaloni = []
videosAMirarAyudantes = []


for n in range(1, 500):
    videosAMirarScaloni.append(random.randint(1, 25))
    videosAMirarAyudantes.append(random.randint(1, 50))
    
    
    calcularTiempoMaximo(
        n, 
        videosAMirarScaloni, 
        videosAMirarAyudantes, 
        debug=False, 
        showElapsedTime=True
    )
