#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

def pesquisa_linear(A, n ,x):
    indice = -1
    for i in range(n):
        if A[i] == x:
            indice = i
    return indice        
    
    
def pesquisa_linear_melhorada(A, n, x):
    for i in range(n):
        if A[i] == x:
            return i+1
    return -1
    

def pesquisa_linear_com_sentinela(A, n, x):
    ultimo = A[-1]
    A[-1] = x
    i = 0
    while A[i] != x:
        i += 1
    A[-1] = ultimo
    if i < n - 1 or ultimo == x:
        return i+1
    return -1


if __name__ == "__main__":
    import random
    
    ARRAY_LENGTH = 30
    
    lst = random.sample(range(1, 100), ARRAY_LENGTH)
    #lst = sorted(lst)
    
    
    print("Array: ", end=" ")
    
    for item in lst:
        print(item, end=" ")
    print()
    
    i = pesquisa_linear_melhorada(lst, len(lst), 92)
    
    if i != -1:
        print(f"Valor foi encontrado na posição {i}.")
    else:
        print("Valor não encontrado.")
