"""
def bubble_sort(A):
    trocado = True
    while trocado:
        trocado = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                trocado = True
                return A
lista = [6, 10, 25, 12, 22, 11, 1000, 222, 77, 34, 2]
bubble_sort(lista)
print("a ordem da lista é:", lista)
"""
def bubbleSort(A):
    trocado = True
    while trocado:
        trocado = False
        for i in range(len(A) - 1): 
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                trocado = True

lista = [6, 10, 25, 12, 22, 11, 1000, 222, 77, 34, 2]
bubbleSort(lista)
print("Lista ordenada:", lista)