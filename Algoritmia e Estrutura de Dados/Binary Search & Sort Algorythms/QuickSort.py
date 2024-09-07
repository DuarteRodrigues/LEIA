#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

def partition(A, p, u):
    q = p
    for i in range(p, u):
        if A[i] <= A[u]:
            A[q], A[i] = A[i], A[q]
            q += 1
    A[q], A[u] = A[u], A[q]
    return q

def quick_sort(A, p, u):
    if p >= u:
        return
    m = partition(A, p, u)
    quick_sort(A, p, m - 1)
    quick_sort(A, m + 1, u)


def quicksort_iterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


if __name__ == '__main__':
    import random

    LIST_LEN = 30

    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)

    print("Unsorted array: ")
    for item in arr:
        print(item, end=" ")

    quick_sort(arr, 0, len(arr) - 1)

    print("\nSorted array: ")
    for item in arr:
        print(item, end=" ")