#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

import profile_EIA
import SelectionSort
import InsertionSort
import MergeSort
import QuickSort

ns = [100, 200, 300, 400, 500, 600, 700, 800, 900,
      #10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000, 17000000, 18000000, 19000000,
      #20000000, 21000000, 22000000, 23000000, 24000000, 25000000, 26000000, 27000000, 28000000, 29000000,
      #30000000, 31000000, 32000000, 33000000, 34000000, 35000000, 36000000, 37000000, 38000000, 39000000
          
]

def test_selectionsort(arr):
    SelectionSort.selection_sort(arr, len(arr))

def test_insertsort(arr):
    InsertionSort.insertion_sort(arr, len(arr))

def test_mergesort(arr):
    MergeSort.merge_sort(arr, 0, len(arr)-1)

def test_quicksort(arr):
    QuickSort.quick_sort(arr, 0, len(arr)-1)


profile_EIA.profile_algorithm(test_selectionsort, ns, "Selection Sort", False)  
profile_EIA.profile_algorithm(test_insertsort, ns, "Insertion Sort", False)
profile_EIA.profile_algorithm(test_mergesort, ns, "Merge Sort", False)  
#profile_EIA.profile_algorithm(test_quicksort, ns, "Quick Sort", False)
