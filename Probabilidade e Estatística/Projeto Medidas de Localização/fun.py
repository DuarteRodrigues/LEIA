## Ficheiro de Funções 
## Diogo Silva - a
## Duarte Rodrigues - a22206488
## Ecleber Monteiro - a
## 
## Projeto no âmbito da cadeira de Probabilidade e Estatística

from collections import Counter # O pacote 'collections' é utilizado para contar a frequência de elementos em um array. Ele fornece a classe Counter que simplifica a contagem de elementos em uma coleção
import numpy as np     # O pacote 'numpy' é utilizado para realizar cálculos eficientes em arrays. Neste caso, estamos usando a função percentile para calcular os percentis. Certifique-se de ter o NumPy instalado usando 'pip install numpy' no terminal

# Função da média aritmética
def media_aritmetica(array):
    # Verifica se o array de dados não está vazio para evitar divisão por zero
    if len(array)==0:
        return None
    else:
        # Calcula a média aritmética
        soma = sum(array)
        media=soma/len(array)
        return media

# Função da mediana
def mediana(array):
    # Verifica se o array de dados não está vazio
    if len(array) == 0:
        return None
    else:
        # Ordena o array de dados
        array.sort()
        # Calcula a mediana
        meio = len(array)//2

        if len(array) % 2 == 0:
            # Se for par, calcula a mediana como a média dos dois valores do meio
            mediana = (array[meio] + array[meio - 1])/2
        else:
            # Se for impar, usa o valor do meio
            mediana = array[meio]
        return mediana

# Função da moda
def moda(array):
    # Verifica se o array de dados não está vazio
    if len(array) == 0:
        return None 
    else:
        # Usa Counter para contar a frequência de cada elemento no array
        contagem = Counter(array)

        # Encontra os elementos com a maior frequência
        moda = [elemento for elemento, frequencia in contagem.items() if frequencia == max(contagem.values())]

        # Se todos os elementos aparecerem com a mesma freqência,o conjunto é amodal
        if len(moda) == len(set(array)):
            return None
        else:
            return moda

# Função dos percentis
def percentis(array, percentis):
    # Verifica se o array de dados não está vazio
    if len(array) == 0:
        return None
    else:
        # Verifica se todos os percentis estão na faixa válida (0 a 100)
        if any (p < 0 or p > 100 for p in percentis):
            raise ValueError("Os percentis devem estar entre 0 e 100")
        else:
            # Calcula os percentis usando a função 'percentile' do NumPy
            result = np.percentile(array,percentis)
            return result

# Função dos quartis
def quartis(array):        
    # Verifica se o array de dados não está vazio
    if len(array) == 0:
        return None
    else:
        # Calcula os quartis usando a função 'percentile' do NumPy
        q = np.percentile(array, [25,50,75])
        return q

# Função da média ponderada
def media_ponderada(x, w):
    print(":)")