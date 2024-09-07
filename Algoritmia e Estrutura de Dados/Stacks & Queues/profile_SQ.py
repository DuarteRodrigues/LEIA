"""Avaliação experimental do tempo de execução de um algoritmo.

Este é um módulo muito simples que demonstra uma possível forma de analisar experimentalmente o tempo de
execução de um algoritmo para diferentes dimensões dos dados de entrada.

Notas importantes:
    * O algoritmo especificado recebe um único parâmetro: uma lista de números.

    * Se o algoritmo a avaliar necessita de mais parâmetros, deve especificar uma função intermédia que será invocada
      com uma lista de números e este poderá depois invocar o algortimo a avaliar com os parâmetros necessários.

    * Por uma questão de eficiência, as listas de números com cada das dimensões especificadas são slices da lista
      de maior dimensão. Deve ter isto em atenção quando analisar os resultados.

    * Por defeito, as listas de números podem conter repetições. Pode usar o parâmetro can_repeat=False para gerar
      listas sem números repetidos.

    * Se este módulo for executado diretamente realizará a avaliação de dois algoritmos simples como exemplo.

    * O gráfico com o resultado da avaliação do algoritmo será mostrado numa página Web usando o seu browser
      por defeito.

Author:
    Carlos Limão - 2022-11-04

License:
    MIT License

    Copyright (c) 2022 Carlos Limão

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import random
import time
import timeit
import plotly.express as px
import pandas as pd
import locale


def profile_algorithm(algorithm, input_sizes, algorithm_name="Nome do Algoritmo",
                      can_repeat=True, should_sort=False, adjust_for_length=False, use_number_list = True,
                      setup=None,
                      x_axis_label="Dimensão da Lista", y_axis_label="Tempo de Execução"):
    """
    Esta função mede o tempo de execução de um algoritmo para um conjunto de dads de entrada com diferentes dimensões.

    :param algorithm: Nome da função a avaliar. Chamada com uma lista de números de cada uma das dimensões em input_sizes.
    :type  algorithm: function
    :param input_sizes: Lista de dimensões da lista que será passada ao algoritmo (são usadas por ordem.)
    :type  input_sizes: list
    :param algorithm_name: Nome a usar para descrever o algoritmo no título do gráfico.
    :param can_repeat: Indica se podem existir repetições nas listas de números a usar para invocar o algoritmo.
    :param should_sort: Indica se a lista a usar para invocar o algoritmo deve ser ou não ordenada.
    :param adjust_for_length: Se True o tempo final é ajustado para refletir o tempo de execução que a operação
                              demoraria sobre a lista mais pequena.
    :param use_number_list: Se True usa listas de números para chamar o algoritmo a avaliar.
    :param setup: Function to be called before each algorithm invocation.
    :param x_axis_label: Nome do eixo dos x (por defeito 'Dimensão da Lista').
    :param y_axis_label: Nome do eixo dos y (por defeito 'Tempo de Execução').
    :return: Os tempos de execução, em segundos, para cada uma das dimensões indicadas no array input_sizes.
    """
    # Lista onde vamos guardar os tempos de execução para cada execução do algoritmo.
    times = []

    print(f"A avaliar algoritmo '{algorithm.__name__}'.")

    if use_number_list:
        print(f"A gerar lista aleatória de {input_sizes[-1]:n} números, {'com' if can_repeat else 'sem'} repetições...", end=' ')
        # Gerar a maior lista pretendida. As mais pequenas serão depois geradas a partir desta.
        if (not can_repeat):
            fulllist = random.sample(range(1, input_sizes[-1] + 1), input_sizes[-1])        # gera lista sem repetições (mais lento)
        else:
            fulllist = random.choices(range(1, input_sizes[-1] + 1), k=input_sizes[-1], )   # gera lista com eventuais repetições
        print("OK")

        # Ordenar a lista se isso foi solicitado
        if should_sort:
            fulllist = sorted(fulllist)

    # Executar o algoritmo especificado com lista de números com cada uma das dimensões indicadas em 'input_sizes'.
    for n in input_sizes:

        if setup:
            setup(n)

        if use_number_list:
            # Usar sublista com dimensão especiificada
            randomlist = fulllist[:n]
            print(f"A invocar '{algorithm.__name__}' com lista de dimensão {n:n}...", end=" ")
        else:
            print(f"A invocar '{algorithm.__name__}' com n={n:n}...", end=" ")

        # Medir o tempo de execução do nosso algoritmo quando executa com a lista de números gerada antes.
        start = timeit.default_timer()
        if use_number_list:
            algorithm(randomlist)
        else:
            algorithm(n)
        stop = timeit.default_timer()
        print(f"OK ({round(stop - start, 4)} seg.)")

        # Guardar o tempo de execução na lista 'times'
        if adjust_for_length:
            times.append((stop - start) / (n/input_sizes[0]))
        else:
            times.append((stop - start) / 1)

    # Usar o pandas para gerar uma tabela (DataFrame) com os dados a mostrar no gráfico.
    # 'input_sizes' no eixo dos x, e 'times' no eixo dos y.
    df = pd.DataFrame(dict(n=input_sizes, time=times))

    # Usar o plotty para mostrar o gráfico do tempo de execução em função do n.
    fig = px.scatter(df, y="time", x="n",
                     title=algorithm_name,
                     labels={"n": x_axis_label, "time": y_axis_label})
    fig.update_traces(marker_size=10)
    if min(times) < 1:
        fig.update_yaxes(range=[-0.01, 1])
    #fig.show()
    fig.write_html('fig.html', auto_open=True)
    time.sleep(1)

    return times


# Importante para não termos virgula, mas sim ponto, como separador de milhares.
locale.setlocale(locale.LC_ALL, 'pt')

if __name__ == '__main__':
    # Dimensões das listas de números a usar para invocar o algoritmo especificado.
    ns = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000,
          #10000000, 11000000, 12000000, 13000000, 14000000, 15000000, 16000000, 17000000, 18000000, 19000000,
          #20000000, 21000000, 22000000, 23000000, 24000000, 25000000, 26000000, 27000000, 28000000, 29000000,
          #30000000, 31000000, 32000000, 33000000, 34000000, 35000000, 36000000, 37000000, 38000000, 39000000,
         ]

    #
    # Uma função intermédia apenas para mostrar como avaliar um algoritmo que não pode ser invocado diretamente.
    #
    def search_list(lst):
        for i in range(len(lst)):
            if lst[i] == 111111111:
                return i
        return -1

    #
    # Avaliação de dois algoritmos. Gera duas páginas Web distintas.
    #
    profile_algorithm(sorted, ns, "Ordenação de uma lista com builtin sorted().", False)
    profile_algorithm(search_list, ns, "Pesquisa numa lista com ciclo 'for'.", False)

