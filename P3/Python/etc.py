import argparse
import os
import time

"""
    ProcesaArgumentos => Funcion que procesa los argumentos que se usan al invocar al programa.
"""


def ProcesaArgumentos(flagT, flagF, flagDi, flagDo):
    # type: (int, int, int, int) -> object


    # creamos el objeto que contedra las opciones
    parser = argparse.ArgumentParser()

    # agregamos las opciones
    parser.add_argument("-t", "--time", action='store_true',
                        help="Muestra el tiempo que se tarda en ejecutar dichas hacer las permutaciones.")
    parser.add_argument("-f", "--file", required=True,
                        help="Se usara F para calcular las permutaciones y ejecutar el programa.")
    parser.add_argument("-di", action='store_true',
                        help="Muestra el contenido del input.")
    parser.add_argument("-do", action='store_true',
                        help="Muestra el contenido del output.")
    # establecemos que queremos que actuen como opciones del programa
    args = parser.parse_args()

    # establecemos que ocurrira con cada opcion, cuando esta se active.
    if args.time:
        flagT = 1
    if args.file:
        flagF = 1
    if args.di:
        flagDi = 1
    if args.do:
        flagDo = 1

    return args, flagF, flagT, flagDi, flagDo


"""
    lstStringToInt(linea) => Convierte la lista
    de Strings a lista de enteros
"""
def lstStringToInt(linea):
    lst = linea.split(",")
    # Lista de strings a lista de integers
    lst = [int(i) for i in lst]
    return lst



"""
    obtenerPath => Obtiene el path del fichero de lectura
    del que obtendremos los valores a permutar 
"""


def obtenerPath(path):
    """"
     'os.path.pardir' => Cambias el directorio de trabajo a la
     carpeta padre donde esta el archivo de lectura
     'os.path.join' => Construimos el path que accede al archivo de lectura
    """
    return os.path.abspath(path)


"""
    obtenerArchivo => devuelve el nombre del archivo
"""


def obtnerArchivo(path):
    return os.path.basename(path)


"""
    abrirFichero => Abre el fichero de lectura
"""


def abrirFichero(path):
    return open(path, 'r')


"""
    cerrarFichero => Cierra el fichero de lectura
"""


def cerrarFichero(fichero):
    fichero.close

"""
    paraTimer => hace una segunda medida del tiempo y calcula la diferencia,
    ademas de mostrarlo por pantalla
"""


def paraTimer():
    print "Tiempo => ", time.clock(), " s"
