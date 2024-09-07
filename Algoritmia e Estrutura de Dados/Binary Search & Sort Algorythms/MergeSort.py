#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

def merge_sort(A, p, u):
    if p >= u:
        return 
    else:
        m = (p + u) // 2
        merge_sort(A, p, m)
        merge_sort(A, m+1, u)
        merge(A, p, m, u)
        
        
def merge(A, p, m, u):
    n1 = m - p+1
    n2 = u-m
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(0, n1):
        L[i] = A[p + i]
        
    for j in range(0, n2):
        R[j] = A[m+1+j]
        
    i = 0
    j = 0
    
    k = p

    while i < n1 and j < n2:
        if i < n1  and L[i] >= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            k += 1
    
    while  i < n1:
        A[k] = L[i]
        i +=1
        k +=1
    
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
        
    
    

if __name__ == "__main__":

    import random

    LIST_LEN = 30
    arr = random.sample(range(1,LIST_LEN+1), LIST_LEN)

    print("unsorted array: ")
    for item in arr:
        print(item, end=" ")
    
    merge_sort(arr, 0 , len(arr)-1)

    print("\nsorted array: ")
    for item in arr:
        print(item, end=" ")