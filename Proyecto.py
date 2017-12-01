from RadixSort import radixSort
from QuickSort import quickSort
from CountingSort import countingSort
from CombSort import combsort
from ShellSort import shellSort
from InsertionSort import insertsort
from MergeSort import mergesort
from time import time


def generarArreglo(tamanio):
    from random import shuffle
    arreglo = [i+1 for i in range(tamanio)]
    shuffle(arreglo)
    return arreglo

def calcularTiempoAlgoritmos(tiemposEjecucion, tamanio):
    #Tiempo RadixSort
    arreglo = generarArreglo(tamanio)
    inicio = time()
    ordenadoRadix = radixSort(arreglo.copy(), 10)
    final = time()
    tiemposEjecucion.get("Radix").append(final-inicio)

    #Tiempo QuickSort
    aux = arreglo.copy()
    inicio = time()
    quickSort(aux)
    final = time()
    tiemposEjecucion.get("Quick").append(final - inicio)

    # Tiempo CountingSort
    aux2 = arreglo.copy()
    inicio = time()
    countingSort(aux2, tamanio)
    final = time()
    tiemposEjecucion.get("Counting").append(final - inicio)

    #Tiempo CombSort
    aux3 = arreglo.copy()
    inicio = time()
    combsort(aux3)
    final = time()
    tiemposEjecucion.get("Comb").append(final - inicio)

    #Tiempo ShellSort
    aux4 = arreglo.copy()
    inicio = time()
    shellSort(aux4)
    final = time()
    tiemposEjecucion.get("Shell").append(final - inicio)

    #Tiempo InsertionSort
    aux5 = arreglo.copy()
    inicio = time()
    insertsort(aux5)
    final = time()
    tiemposEjecucion.get("Insertion").append(final - inicio)

saltos = [1000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
dic = {"Radix": [], "Quick": [], "Counting": [], "Shell": [], "Comb": [], "Insertion": []}
for i in saltos:
    calcularTiempoAlgoritmos(dic, i)

print(dic)