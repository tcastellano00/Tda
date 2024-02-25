import numpy as np
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
