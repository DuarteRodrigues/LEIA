#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 3º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

def pesquisa_linear(A,n,x):
    """
    Parameters for basic linear search
    ----------
    A : Array to search.
    n : Array diimension.
    x : Wanted Value.

    Returns position index where x is or -1if it doesn't find it 
    -------
    None.
    """
    resultado = -1
    for i in range(n):
        if A[i] == x:
            resultado = i
    return resultado

def pesquisa_linear_melhorada():
    pass

def pesquisa_linear_com_sentinela():
    pass