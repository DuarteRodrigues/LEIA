#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Algoritmia e Estrutura de Dados
# Trabalho: 4º Trabalho
#
# Número: a22206488
# Nome: Duarte Rodrigues
#

import Profile_Search
import BSearch
import LSearch

def test_bsearch(lst):
    BSearch.binary_search(lst, len(lst), 33)
    
def test_lsearch(lst):
    LSearch.pesquisa_linear(lst, len(lst), 33)
    
ns = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000]

#Profile_Search.profile_algorithm(test_bsearch, ns, "Pesquisa Binaria", can_repeat=False, should_sort=True)

Profile_Search.profile_algorithm(test_bsearch, ns, "Pesquisa Binaria", can_repeat=False, should_sort=True)


        