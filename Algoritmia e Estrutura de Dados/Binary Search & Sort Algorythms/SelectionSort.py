#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

def selection_sort(A, n):    
    for i in range(n):
        index_min = i
        for j in range(i+1, n):
            if A[j] < A[index_min]:
                index_min = j
        A[i], A[index_min] = A[index_min], A[i]          
        

if __name__ == "__main__":

    import random

    LIST_LEN = 30
    arr = random.sample(range(1,LIST_LEN+1), LIST_LEN)

    print("unsorted array: ")
    for item in arr:
        print(item, end=" ")
    
    selection_sort(arr, len(arr))

    print("\nsorted array: ")
    for item in arr:
        print(item, end=" ")
    
    
    