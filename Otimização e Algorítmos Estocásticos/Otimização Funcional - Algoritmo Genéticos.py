import random

GENE_NUM = 4
SEARCH_SPACE_MIN = -100.0
SEARCH_SPACE_MAX = 100.0
POPU = 120
ELITE_RATE = 30
MUTATION_PROB = 120
ROW_COUNT = 1

def FUNCION_QUALITY(x1, x2, x3, x4):
    return ((x1-4)*(x1-4)) + ((x2-3)*(x2-3)) + ((x3-2)*(x3-2)) + (x4*x4)
    pass

array = [[random.uniform(SEARCH_SPACE_MIN, SEARCH_SPACE_MAX) for _ in range(GENE_NUM)] for _ in range(POPU)]

for row in array:
    print("Row {}: {}".format(ROW_COUNT, row))
    row_gene_1 = array[ROW_COUNT-1][0]
    row_gene_2 = array[ROW_COUNT-1][1]
    row_gene_3 = array[ROW_COUNT-1][2]
    row_gene_4 = array[ROW_COUNT-1][3]
    print("Função de Qualidade: {}".format(FUNCION_QUALITY(row_gene_1,row_gene_2,row_gene_3,row_gene_4)))
    ROW_COUNT += 1
