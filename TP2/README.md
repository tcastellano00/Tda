# TP2
| Integrantes                        | Padron |
| -------------------------------    | ------ |
| Adriana Macarena Iglesias Tripodi  | 103384 |
| Ezequiel Lassalle                  | 105801 |
| Martín Tomás                       | 100835 |


## Instalación de librerias utilizadas
Primero necesitaras instalar las librerias utilizadas por el proyecto.
```
pip install -r requirements.txt
```

## Ejecucion de pruebas (test.py)
Para ver todos los parametros posibles al momento de ejecutar las pruebas:
```
python test.py -h
```

Si lo que desea es ejecutar todas las pruebas de la catedra con nuestra parametrizacion por default corra:
```
python test.py
```

Si por ejemplo, desea plotear los resultados finales de las ejecuciones:
```
python test.py --plot=True
```

## Ejecucion con un set de datos propio (main.py)
El programa no chequea que los archivos cumplan con el formato dado por la catedra, solo chequea que los archivos existan.
Un ejemplo de ejecucion es el siguiente, tambien podras encontrar dentro de la carpeta DatosPropios los archivos con los cuales se realizaron las pruebas.
```
python main.py --archivo_datos DatosPropios/3.txt --archivo_resultados DatosPropios/3_resultados.txt
```