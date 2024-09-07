#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

def binary_search(A, n, x):
    """
    Binary search algorithm
    Parameters
    ----------
    A : Array de pesquisa
        DESCRIPTION.
    n : Dimensão do array
        DESCRIPTION.
    x : Valor a procurar
        DESCRIPTION.

    Returns indice da posição em A onde x foi encontrado ou -1 se x não for encontrado.
    """
    
    p = 0
    u = n - 1
    while p <= u:
        m = (p + u)//2
        if A[m] == x:
            return m
        elif A[m] > x:
            u = m - 1
        else: 
            p = m + 1
    return -1


if __name__ == "__main__":
    import random
    
    ARRAY_LENGTH = 30
    
    lst = random.sample(range(1, 100), ARRAY_LENGTH)
    lst = sorted(lst)
    
    
    print("Array: ", end=" ")
    
    for item in lst:
        print(item, end=" ")
    print()
    
    i = binary_search(lst, len(lst), 34)
    
    if i != -1:
        print(f"Valor foi encontrado na posição {i}.")
    else:
        print("Valor não encontrado.")
