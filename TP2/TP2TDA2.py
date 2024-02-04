from itertools import islice
import numpy as np
import time
import matplotlib.pyplot as plt
#Adaptamos el problema comparandolo con el de la mochila
#max(max(G[w-2,j])+min(ei,s1),G[w-1,j-1] +min (ei, sj))
#max(G[n-1,W];G[n-1,W-P]+Vi)
 
 
def scaloni( d, e, s): 
    G = [[0 for x in range(d + 1)] for x in range(d + 1)] 
    G[1][1] = min(e[0],s[0])
    for i in range(1,d+1):
        p=1 
        for j in range(1,d + 1): 
            if i == 0 or j == 0 or (j>i): 
                G[i][j] = 0
            else:
                    G[i][j]=max(min(e[i-1],s[j-1])+ G[i-1][j-1],min(e[i-1],s[0])+ max(G[i-2]))
 
    return G  

def reconstruccion(G, p, e, s):
    res=["Descanso" for x in range(len(e))] 
    i=len(e)
    while(i> 1):
        if max(G[i-2])+min(e[i-1],s[p-1]) == G[i][p]:
            p=G[i-2].index(max(G[i-2]))+1
            res[i-1]="Entreno"  
            i-=1
        elif(p!=0):
            res[i-1]="Entreno" 
        p-=1
        i-=1
    if G[2][1]+min(e[2],s[2]) !=G[3][p+2]:
            res[0]="Entreno" 
    return (res)
def abrir_archivo(path):
   
    with open(path) as archivo:
        datos = archivo.readlines()
        n = int(datos[0])
        e = [int(datos[i]) for i in range(1, n + 1)]
        s = [int(datos[i]) for i in range(n + 1, 2 * n + 1)]
    archivo.close()
    return e, s
 
def resultados_esperados(path):
    with open(path) as archivo:
        resultados=[]
        while (True):
            datos = list(islice(archivo,4))
            #dias= datos[0]
            #ganancia_maxima = int(datos[1].split(":")[1])
            #secuencia =datos[2].split(":")[1]
            if not datos:
                break
            resultados.append({
            "Archivo": datos.pop(0).split("\n")[0],
            "Ganancia Máxima": int((datos.pop(0).split(":")[1]).split("\n")[0]),
            "Plan de entrenamiento":((datos.pop(0).split(":")[1]).split("\n")[0])[1:].split(", ")
            })
    archivo.close()
    return resultados
 
def comparar_resultados(name,ganancia_maxima_obtenida,entrenamiento_obtenido,resultados_dados):
    #resultados_dados=resultados_esperados("Datos/Resultados Esperados.txt")
    comparacion= False 
    for resultados in resultados_dados:
        if(name==resultados["Archivo"]):
            comparacion= True if (ganancia_maxima_obtenida==resultados["Ganancia Máxima"] and entrenamiento_obtenido==resultados["Plan de entrenamiento"]) else False
            break
    return comparacion

def comparaciones(x_name,resultados_dados,plot=False,No_calculate_5000=False,obtener_Plan_entrenamiento=False):
    y=[]
    x=[]
    path1='C:/Users/amitr/Downloads/TP2/Datos/'
    resultados_dados=resultados_esperados(path1+resultados_dados)
    if No_calculate_5000:
         x_name.pop()
    for i in (x_name):
         path=path1+i
         e,s=abrir_archivo(path)
         d = len (e)
         x.append(d)
         start=time.perf_counter()
         G=scaloni( d, e, s)
         end=time.perf_counter()
         y.append(end-start)
         P=np.matrix(G)
         Max=P.max()
         p, j = np.unravel_index(P.argmax(), P.shape)
         entrenamiento_obtenido =reconstruccion(G,j,e,s)
         print("El Archivo analizado es:", i, ". Su máximo es: ", Max)
         if obtener_Plan_entrenamiento:
            print("El Plan de Entrenamiento es:", entrenamiento_obtenido) 
         print("Si lo comparamos con los datos dados es", comparar_resultados(i,Max,entrenamiento_obtenido,resultados_dados), "que se cumple lo esperado")
         if (plot):
            print("Se tardó", end-start, "segundos en realizar el análisis")
         print()
    if(plot):
        plt.figure(figsize=(20, 8))
        plt.plot(x, y,marker='o',label = "nuestro")
        plt.xlabel('Cantidad de Dias Planeados', fontsize=16)
        plt.ylabel('Tiempo de Implementación [s]', fontsize=16)
        plt.title('Cantidad de Días Vs Tiempo de Implementación', fontsize=26)
        plt.legend()
        plt.grid(True)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.show()
    return 
    
