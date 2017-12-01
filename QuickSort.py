def quickSort(lista):
   quickSortHelper(lista,0,len(lista)-1)

def quickSortHelper(lista,primero,ultimo):
   if primero<ultimo:
       puntoCorte = partition(lista,primero,ultimo)
       quickSortHelper(lista,primero,puntoCorte-1)
       quickSortHelper(lista,puntoCorte+1,ultimo)


def partition(lista,primero,ultimo):
   pivote = lista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo
   
   done = False
   while not done:

       while marcaIzq <= marcaDer and lista[marcaIzq] <= pivote:
           marcaIzq = marcaIzq + 1

       while lista[marcaDer] >= pivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           done = True
       else:
           temp = lista[marcaIzq]
           lista[marcaIzq] = lista[marcaDer]
           lista[marcaDer] = temp

   temp = lista[primero]
   lista[primero] = lista[marcaDer]
   lista[marcaDer] = temp


   return marcaDer
