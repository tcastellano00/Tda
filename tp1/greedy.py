import random
import time
import matplotlib.pyplot as plt
import numpy as np

def calcularTiempoMaximo(n, tiempoScaloni, tiempoAyudantes,debug):
    if (n <= 0):
        return
    
    tiempoScaloniAyudantes = [list(x) for x in zip(tiempoScaloni,tiempoAyudantes)]
    
    # Complejidad O(nlogn)
    tiempoScaloniAyudantes.sort(key=lambda tup: tup[1], reverse=True)

    tiempoEnFinalizarAyudante = []
    tiempoAcumuladoScaloni = 0
    tiempoMaximo = 0
 
    # Complejidad O(n)
    for tiempo in tiempoScaloniAyudantes:
        tiempoScaloni = tiempo[0]
        tiempoAyudante = tiempo[1]

        #tiempoEnFinalizarAyudante.append(tiempoScaloni + tiempoAyudante + tiempoAcumuladoScaloni)
        tiempoAcumuladoScaloni += tiempoScaloni
        if(tiempoAyudante + tiempoAcumuladoScaloni > tiempoMaximo):

            tiempoMaximo = tiempoAyudante + tiempoAcumuladoScaloni
    if (debug):        
        print("El tiempo que se demora terminar de ver todos los videos es: ", tiempoMaximo)
        
videosAMirarScaloni = []
videosAMirarAyudantes = []


x=np.arange(0,100000,1000)
#x=np.arange(0,8,1)
#x=10**x
y=[]
#rng = np.random.default_rng()
for n in x:
    #start =time.perf_counter()
    star=[]
    en=[]
    for i in range(1, 5):
        #videosAMirarScaloni=rng.integers(300,size=(1,n*10))
        #videosAMirarAyudantes=rng.integers(400,size=(1,n*10))
    #start=time.perf_counter()
        videosAMirarScaloni = [random.uniform(1, 300) for _ in range(n)]
        videosAMirarAyudantes = [random.uniform(1, 400) for _ in range(n)]
        star.append(time.perf_counter())
        calcularTiempoMaximo(
            n, 
            videosAMirarScaloni, 
            videosAMirarAyudantes,
            debug=False
        )
        en.append(time.perf_counter())
    start=np.mean(star)
    end=np.mean(en)
    #end=time.perf_counter()
    y.append(end-start)


# Crear el gráfico
plt.figure(figsize=(20, 8))
plt.plot(x, y,marker='o',label = "nuestro")
#plt.plot(x, (x*np.log(x))/(10**3),label = "n log(n)")
plt.xlabel('Cantidad de videos visualizados', fontsize=16)
plt.ylabel('Tiempo de Implementación [s]', fontsize=16)
plt.title('Cantidad de Videos Vs Tiempo de Implementación', fontsize=26)
plt.legend()
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Mostrar el gráfico
plt.show()
