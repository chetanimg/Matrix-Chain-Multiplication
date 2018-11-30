import etc
import tabulation
import memoization

"""
flagT = 0
flagF = 0
flagDi = 0
flagDo = 0

args, flagF, flagT, flagDi, flagDo = etc.ProcesaArgumentos(flagT, flagF, flagDi, flagDo)

if (flagT == 0) and (flagF == 0) and (flagDi == 0) and (flagDo == 0):
    print "Para que el programa funciones correctemente use alguno de los comandos disponibles, 'python main.py -h'"
    exit(1)

path = args.file

fichero = etc.abrirFichero(path)

if flagDi == 1:
    for linea in fichero:
        print linea
    etc.cerrarFichero(fichero)

if flagDo == 1 or flagT == 1:
    if flagDi == 1:
        fichero = etc.abrirFichero(path)
    for linea in fichero:

        arr = etc.lstStringToInt(linea)
        size = len(arr)

        print "Array =>", arr

        if flagT == 1:
            etc.time.clock()

        print "min operaciones =>", tabulation.MatrixChainOrder(arr, size)
        #print "Memoization =>", memoization.MatrixChainOrder(arr, size)

        if flagT == 1:
            etc.paraTimer()

etc.cerrarFichero(fichero)
"""

arr = [4, 8, 12, 2, 6]
size = len(arr)
tabulation.MatrixChainOrder(arr, arr.__len__())
