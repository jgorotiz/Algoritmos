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
    tam=1000000/tamanio
    for i in range(tam):
        minilista=[]
        for i in range (tamanio):
            elemento=padre.pop(-1)
            minilista.append(elemento)
        arreglos.append(minilista)
        
def calcularTiempoAlgoritmos(arreglo, tamanio,archivo):
    tiempos=[]
    #Tiempo RadixSort
    arreglo = generarArreglo(arreglo,tamanio)
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


    # Tiempo bubbleSort
    aux2 = arreglo.copy()
    inicio = time()
    bubbleSort(aux2)
    final = time()
    tiempos.append(final-inicio)


    #Tiempo shellSort
    aux3 = arreglo.copy()
    inicio = time()
    shellSort(aux3)
    final = time()
    tiempos.append(final-inicio)
    

    #Tiempo heapsort
    aux4 = arreglo.copy()
    inicio = time()
    heapsort(aux4)
    final = time()
    tiempos.append(final-inicio)
    
    
    archivo.write(str(tamanio))
    for element in tiempos:
        linea+=","+str(element*1000) #para que quede en milisegundos
    archivo.write("\n")

arreglo = []
for i in range(1000000):
    num=randint(1000000000,9999999999)
    arreglo.append(num)
file=open("algoritmos_ordenamiento_resultados.csv","w")
file.write("elementos,radix,quick,bubble,shell,heap"+"\n")
saltos=[10,100,1000,10000,100000,100000]
