#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 2º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

import profile_EIA as profile
import PesquisaLinear

def algoritmo_a_testar(lst):
    PesquisaLinear.pesquisa_linear(lst, len(lst), 33)
    


ns= [1000000, 2000000, 3000000, 4000000, 5000000]

profile.profile_algorithm(algoritmo_a_testar, ns, "Descrição do algorítmo", False)
