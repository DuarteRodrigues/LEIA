## Ficheiro de Funções 
## Diogo Silva - a
## Duarte Rodrigues - a22206488
## Ecleber Monteiro - a
## 
## Projeto no âmbito da cadeira de Probabilidade e Estatística

## A primeira temporada regular em que Michael Jordan foi vencedor do prémio 'Campeão de Pontuação' foi coincidentemente a sua temporada com maior média de pontos, em 86/87 com 82 jogos jogados

import fun

pontos = [50,41,34,33,39,34,28,48,40,22,37,41,40,40,45,43,43,40,41,41,11,41,41,27,43,30,44,31,34,47,27,53,31,43,47,32,31,35,27,30,27,49,38,32,36,29,45,33,43,33,43,34,58,37,30,30,61,27,33,31,49,24,13,44,21,40,40,46,56,40,22,33,36,26,32,31,39,34,53,50,61,17]
percentis = [20, 40, 60, 80, 100]


media_a_resultado = fun.media_aritmetica(pontos)
mediana_resultado = fun.mediana(pontos)
moda_resultado = fun.moda(pontos)
quartis_resultado = fun.quartis(pontos)


print("\nEis os pontos marcados por Michael Jordan nos 82 jogos jogados na temporada de 86/87 processados por medidas de localização:")
print(f"Média Aritmética: {media_a_resultado}" )
print(f"Mediana: {mediana_resultado}")
print(f"Moda: {moda_resultado}")
try:
    percentis_resultado = fun.percentis(pontos, percentis)
    # Exibir resultados
    for i, percentil in enumerate(percentis):
        print(f"{percentil}º percentil: {percentis_resultado[i]}")
except ValueError as e:
    print(f"Erro: {e}")
print(f"Primeiro quartil(Q1): {quartis_resultado[0]}")
print(f"Segundo quartil(Q2): {quartis_resultado[1]}")
print(f"Terceiro quartil(Q3): {quartis_resultado[2]}")