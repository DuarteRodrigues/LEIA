import numpy as np
import matplotlib.pyplot as plt

##Permite visualizar diferentes funções tipicamente usadas com a notação O-Grande.
##Date created: 22/03/2017
##Big-O | Duarte Rodrigues
# --------+---------------
# 1 | Constant
# log(n) | Logarithmic
# n | Linear
# nlog(n) | Log Linear
# n^2 | Quadratic
# n^3 | Cubic
# 2^n | Exponential

# Estilo do gráfico a usar (saber mais em https://matplotlib.org/stable/gallery/index.html)
plt.style.use('bmh')
# Definir dados das curvas a traçar.
n = np.linspace(1, 50, 1000) # Devolve 100 números igualmente espaçados entre 1 e 50
labels = ['O(1) - Constante',
          'O(log n) - Logarítmica', 
          'O(n) - Linear', 
          'O(n.log n) - Linear Logarítmica', 
          'O(n^2) - Quadrática', 
          'O(n^3) – Cúbica', 
          'O(2^n) – Exponencial']

big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]
# Setup do gráfico
plt.figure(figsize=(12, 12)) # Formato da imagem
plt.ylim(0, 50) # Tamanho do eixo dos y (x é determinado por n)
for i in range(len(big_o)): # Percorrer todas as funções definidas
    plt.plot(n, big_o[i], label=labels[i]) # Desenhar função e usar label adequada
    
plt.legend(loc=0) # Posição da legenda
plt.ylabel('Tempo de Execução') # Nome do eixo dos x
plt.xlabel('Dimensão dos dados de entrada') # Nome do eixo dos y
# plt.savefig('big-o-notation.png') # Remover comentário para gerar ficheiro png.
plt.show() # Mostrar gráfico