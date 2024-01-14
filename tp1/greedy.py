tiempoScaloniAyudantes = [(3, 200), (10, 195), (2, 19), (20, 38), (3, 1), (15, 1)]
tiempoScaloniAyudantes.sort(key=lambda tup: tup[1], reverse=True)

tiempoEnFinalizarAyudante = []
tiempoAcumuladoScaloni = 0

for tiempo in tiempoScaloniAyudantes:
    tiempoScaloni = tiempo[0]
    tiempoAyudante = tiempo[1]

    tiempoEnFinalizarAyudante.append(tiempoScaloni + tiempoAyudante + tiempoAcumuladoScaloni)

    tiempoAcumuladoScaloni += tiempoScaloni

print("Lo que demora cada ayudante en terminar de ver su video es: ")
print(tiempoEnFinalizarAyudante)

print("El tiempo que se demora terminar de ver todos los videos es: ", max(tiempoEnFinalizarAyudante))