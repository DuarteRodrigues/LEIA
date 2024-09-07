#
# Lista Simplesmente Ligada.
#
# A usar coo base para realizar a sua implementação de uma LSL e de uma LDL.
#
# Autor: XXXXXXXXX
# Data: DD/MM/AAAA
#

# Nó de uma Lista Simplemente Ligada (LSL).
import sys


class Node:

    def __init__(self, data=None, next=None):
        """
        Construtor de um nó de uma LSL.
        Inicializa os campos do nó.

        :param data: os dados a armazenar no nó.
        :param next: o próximo nó na lista. None se existir nenhum.
        """
        self.data = data
        self.next = next

var = Node(33)


# Lista Simplesmente Ligada (LSL).
class SinglyLinkedList:
    """
    Classe que representa uma lista simplesmente ligada.

    Notas:
    1. Os procedimentos declarados numa classe chamam-se métodos.
    2. Todos os métodos têm no mínimo um parâmtro "self" que representa a instância (objeto/variável) no contexto da
       qual a invocação foi feita.
    3. Podem criar-se variáveis do tipo definido por uma classe usando "var = NomeDaClasse()".
       Esta operação invoca o construtor da classe (método __init__()).
    4. As variáveis associadas a cada instância de uma classe chamam-se propriedades e acedem-se usando
       "self.nome_da_propriedade".
    5. Ver a função main() no final do ficheiro para mais exemplos de como a classe é usada.
    """
    def __init__(self, use_tail=False):
        """
        Construtor de uma LSL.
        Inicializa os campos da lista.

        :param use_tail: indica se deve ser usada uma referência interna para a cauda da lista.
        """
        self._head = None
        self._tail = None
        self._size = 0
        self.use_tail = use_tail

    def insert_before(self, data, node):
        """
        Insere um novo nó, antes do nó especificado.
        O algoritmo usado garante que esta operação é O(1).

        :param data: dados a inserir.
        :param node: o nó, existente na lista, antes do qual inserir.
        :return: o novo nó, que foi inserido na lista.
        """
        pass

    def insert_after(self, data, node):
        """
        Insere um novo nó, após o nó especificado.
        Se, em vez de um nó, for especificada a própria lista, insere à cabeça.

        :param data: dados a inserir.
        :param node: o nó, existente na lista, depois do qual inserir.
        :return: o novo nó, que foi inserido na lista.
        """
        
        if node is not None:                
            new_node = Node(data, node.next.next)
            node.next = new_node
            if self._tail == node:
                self._tail = new_node
            self._size += 1
        else:
            raise RuntimeError("Não posso inserir um erro que seja None!")

    def insert_head(self, data):
        """
        Insere um novo nó, à cabeça da LSL.

        :param data: dados a inserir.
        :return:  o novo nó, que foi inserido na lista.
        """
        
        ##if self._head is None:
          ##  new_node = Node(data)
          ##  self._head = new_node
        ##else:
        new_node = Node(data, self._head)
        self._head = new_node
        if self._tail is None:
            self._tail = new_node
        self._size += 1
        

    def insert_tail(self, data):
        """
        Insere um novo nó, no fim da LSL.

        :param data: dados a inserir.
        :return: o novo nó, que foi inserido na lista.
        """
        
        new_node = Node(data)
        
        if self._tail is None:
            self._tail = self._head =  new_node
            
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def remove_head(self):
        """
        Remove o nó à cabeça da lista.

        :return: None
        """
        self._size -= 1

    def remove_tail(self):
        """
        Remove o nó na cauda da lista.

        :return: None
        """
        self._size -= 1

    def remove_after(self, node):
        """
        Remove o nó após o nó especificado.
        Se, em vez de um nó, for especificada a própria lista, remove à cabeça.

        :param node: o nó depois do qual remover.
        :return: None.
        """
        self._size -= 1

    def remove(self, node):
        """
        Remove o nó especificado da lista.
        O algoritmo garante que esta operação é O(1) para todos os nós, exceto o último.

        :param node: o nó a remover.
        :return: None
        """
        pass

    def head(self):
        """
        Devolve o nó à cabeça da lista.

        :return: O nó na cabeça da lista ou None se a lista está vazia.
        """
        return self._head

    def tail(self):
        """
        Devolve o nó na cauda da lista.

        :return: O nó na cauda da lista ou None se a lista está vazia.
        """
        return self._tail

    def size(self):
        """
        Devolve o número de nós presentes na lista.

        :return: número de nós presentes na lista.
        """
        return self._size

    def print(self):
        """
        Escreve o conteúdo aa lista.

        :return: None.
        """
        pass


def main() -> int:
    """
    Um teste básico para validar a implementação de uma LSL existente neste módulo.
    As instruções assert terminam a execução caso a expressão Booleana especificada seja falsa.

    :return: 0 se os testes executaram com sucesso.
    """

    def assert_head_tail_path(ll):
        """
        Confirmar que, percorrendo a lista a partir da cabeça, se chega à cauda.

        :param ll: lista
        :return: None
        """
        current = ll.head()
        print("Head->", end=" ")
        while current:
            prev = current
            print(current.data, end=" ")
            current = current.next
        print()
        assert (ll.head() is None and ll.tail() is None) or ll.tail() == prev

    print("+-----------------------------------------------------------------+")
    print("| Teste à implemementação de uma LSL existente neste módulo       |")
    print("+-----------------------------------------------------------------+")

    # Criação da lista
    ll = SinglyLinkedList(True)
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #  tail -> +----+
    #  head -> | 33 |-->None
    #          +----+
    ll.insert_head(33)
    assert ll.size() == 1
    assert ll.head().data == 33
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 34 |-->| 33 |-->None
    #          +----+   +----+
    ll.insert_head(34)
    assert ll.size() == 2
    assert ll.head().data == 34
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 34 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.insert_head(35)
    assert ll.size() == 3
    assert ll.head().data == 35
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+
    ll.insert_tail(36)
    assert ll.size() == 4
    assert ll.head().data == 35
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+
    ll.insert_after(37, ll._head)
    assert ll.size() == 5
    assert ll.head().data == 35
    assert ll.head().next.data == 37
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 38 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+   +----+
    current = ll.head()
    while current.data != 37 and current.next:
        current = current.next
    ll.insert_after(38, current)
    assert ll.size() == 6
    assert ll.head().data == 35
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+   +----+ <- tail
    #  head -> | 35 |-->| 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+   +----+
    ll.remove_after(current)
    assert ll.size() == 5
    assert ll.head().data == 35
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+   +----+ <- tail
    #  head -> | 37 |-->| 34 |-->| 33 |-->| 36 |-->None
    #          +----+   +----+   +----+   +----+
    ll.remove_head()
    assert ll.size() == 4
    assert ll.head().data == 37
    assert ll.tail().data == 36
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 37 |-->| 34 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.remove_tail()
    assert ll.size() == 3
    assert ll.head().data == 37
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 34 |-->| 33 |-->None
    #          +----+   +----+
    ll.remove_head()
    assert ll.size() == 2
    assert ll.head().data == 34
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+ <- tail
    #  head -> | 33 |-->None
    #          +----+
    ll.remove_head()
    assert ll.size() == 1
    assert ll.head().data == 33
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 39 |-->| 33 |-->None
    #          +----+   +----+
    ll.insert_before(39, ll.head())
    assert ll.size() == 2
    assert ll.head().data == 39
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+   +----+ <- tail
    #  head -> | 39 |-->| 40 |-->| 33 |-->None
    #          +----+   +----+   +----+
    ll.insert_before(40, ll.tail())
    assert ll.size() == 3
    assert ll.head().data == 39
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+   +----+ <- tail
    #  head -> | 39 |-->| 33 |-->None
    #          +----+   +----+
    current = ll.head().next
    ll.remove(current)
    assert ll.size() == 2
    assert ll.head().data == 39
    assert ll.tail().data == 33
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #          +----+ <- tail
    #  head -> | 39 |-->None
    #          +----+
    ll.remove(ll.tail())
    assert ll.size() == 1
    assert ll.head().data == 39
    assert ll.tail().data == 39
    assert_head_tail_path(ll)

    #  Estado depois da execução deste bloco:
    #  tail -> None
    #  head -> None
    #
    ll.remove(ll.head())
    assert ll.size() == 0
    assert ll.head() is None
    assert ll.tail() is None
    assert_head_tail_path(ll)

    print("+----------------------------------------------------------------+")
    print("| Todos os testes terminaram com sucesso!                        |")
    print("+----------------------------------------------------------------+")

    return 0


if __name__ == "__main__":
    sys.exit(main())
