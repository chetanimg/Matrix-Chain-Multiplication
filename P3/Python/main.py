import etc
import tabulation
import memoization

flagT = 0
flagF = 0
flagDi = 0
flagDo = 0
flagMem = 0
flagTab = 0

args, flagF, flagT, flagDi, flagDo, flagMem, flagTab = etc.ProcesaArgumentos(flagT, flagF, flagDi, flagDo, flagMem,
                                                                             flagTab)

if (flagT == 0) and (flagF == 0) and (flagDi == 0) and (flagDo == 0):
    print "Para que el programa funciones correctemente use alguno de los comandos disponibles, 'python main.py -h'"
    exit(1)

if flagDo == 1 and flagTab == 0 and flagMem == 0:
    print "Para mostrar el output ha de indicar que metodo quiere aplicar, indique -mem o -tab"
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

        if flagMem == 1:
            memoization.initalizeMem(size)

        print "Size =>", size
        print "Matrices =>", arr

        if flagT == 1:
            etc.time.clock()

        if flagTab == 1:
            print "min operaciones por Tabulation => " + str(tabulation.MatrixChainOrder(arr, size))
            if flagT == 1:
                print "Tiempo por Tabulation => " + str(etc.time.clock())

        if flagT == 1:
            etc.time.clock()

        if flagMem == 1:
            print "min operaciones por Memoization => " + str(memoization.MatrixChainOrder(arr, 1, size-1))
            if flagT == 1:
                print "Tiempo por Memoization => " + str(etc.time.clock())
        print "--------------------------------------------------------"

etc.cerrarFichero(fichero)
