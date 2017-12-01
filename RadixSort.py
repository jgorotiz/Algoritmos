def obtenerDigito(num, base, digito):
    return (num // base ** digito) % base


def crearBlancos(tamanio):
    return [[] for i in range(tamanio)]


def dividir(lista, base, digito):
    cubetas = crearBlancos(base)
    for num in lista:
        cubetas[obtenerDigito(num, base, digito)].append(num)
    return cubetas


def merge(lista):
    lista2 = []
    for sublista in lista:
        lista2.extend(sublista)
    return lista2


def maxAbs(lista):
    return max(abs(num) for num in lista)


def radixSort(lista, base):
    from math import log
    passes = int(round(log(maxAbs(lista), base)) + 1)
    lista2 = list(lista)
    for digito in range(passes):
        lista2 = merge(dividir(lista2, base, digito))
    return lista2