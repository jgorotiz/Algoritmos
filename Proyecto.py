from RadixSort import radixSort
from QuickSort import quickSort
from ShellSort import shellSort
from heapsort import *
from BubbleSort import bubbleSort
from time import time
from random import randint
    
def generarArreglo(arreglo,tamanio):
    padre=arreglo.copy()
    arreglos=[]
    for i in range()
def calcularTiempoAlgoritmos(tiemposEjecucion, tamanio,archivo):
    tiempos=[]
    #Tiempo RadixSort
    arreglo = generarArreglo(tamanio)
    inicio = time()
    ordenadoRadix = radixSort(arreglo.copy(), 10)
    final = time()
    tiempos.append(final-inicio)

    #Tiempo QuickSort
    aux = arreglo.copy()
    inicio = time()
    quickSort(aux)
    final = time()
    tiempos.append(final-inicio)


    # Tiempo CountingSort
    aux2 = arreglo.copy()
    inicio = time()
    countingSort(aux2, tamanio)
    final = time()
    tiempos.append(final-inicio)


    #Tiempo CombSort
    aux3 = arreglo.copy()
    inicio = time()
    combsort(aux3)
    final = time()
    tiempos.append(final-inicio)
    

    #Tiempo ShellSort
    aux4 = arreglo.copy()
    inicio = time()
    shellSort(aux4)
    final = time()
    tiempos.append(final-inicio)
    

    #Tiempo InsertionSort
    aux5 = arreglo.copy()
    inicio = time()
    insertsort(aux5)
    final = time()
    tiempos.append(final-inicio)
    
    archivo.write("10")
    for element in tiempos:
        linea+=","+str(element)
    archivo.write("\n")

arreglo = []
    for i in range(1000000):
        num=randint(1000000000,9999999999)
    return arreglo
