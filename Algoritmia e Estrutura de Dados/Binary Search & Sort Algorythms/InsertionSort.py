#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

def insertion_sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        
if __name__ == "__main__":

    import random

    LIST_LEN = 30
    arr = random.sample(range(1,LIST_LEN+1), LIST_LEN)

    print("unsorted array: ")
    for item in arr:
        print(item, end=" ")
    
    insertion_sort(arr, len(arr))

    print("sorted array: ")
    for item in arr:
        print(item, end=" ")
    
    
    