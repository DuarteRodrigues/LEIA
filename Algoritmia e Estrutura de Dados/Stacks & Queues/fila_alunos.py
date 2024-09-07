from collections import deque
import profile_SQ

class QueueUsingList:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return self._data == []

    def enqueue(self, item):
        self._data.insert(0,item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyError("A fila está vazia!")

        return self._data.pop()    

    def __len__(self):
        return len(self._data)

    def first(self):
        if self.is_empty():
            raise EmptyError("A fila está vazia!")

        return self._data[-1]

class QueueUsingDeque:
    def __init__(self):
        self._data = deque()

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyError("A fila está vazia")

        return self._data.popleft()

    def __len__(self):
        return len(self._data)

    def first(self):
        if self.is_empty():
            raise EmptyError("A fila está vazia")

        return self._data[0]    


class EmptyError(Exception):
    pass


def test_queue_implementation(queue_class, values=[5, 4, 3, 2, 1]):
    

    if "List" in queue_class.__name__:
        test_desc  = "Teste à implementação de uma Fila usando uma lista                         "
    else:
        test_desc = "Teste à implementação de uma Fila usando uma dequeue                       "

    print(f"+-------------------------------------------------------------------------------+")
    print(f"| {test_desc}   |")
    print(f"+-------------------------------------------------------------------------------+")


    # Cria uma fila.
    q = queue_class()

    # Adiciona e remove um elemento.
    print(f"Inserir {values[0]} na fila ...")
    q.enqueue(values[0])
    assert q.is_empty() is False
    assert len(q) == 1
    assert q.first() == values[0]

    print("Remover da fila: ", end=" ")
    el = q.dequeue()
    assert q.is_empty()
    assert len(q) == 0
    print(el)

    # Adicionar elementos do array values
    nelements = 0
    for i in values:
        print(f"Inserir na fila: {i} ...")
        q.enqueue(i)
        nelements += 1
        assert not q.is_empty()
        assert len(q) == nelements
        assert q.first() == values[0]

    # Verificar a fila
    assert len(q) == len(values)
    print(f"Dimensão da fila: {len(q)}")

    try:
        # Tentar remover len(values) + 1 valores
        # (No último deve gerar uma exceção)
        el_index = 0
        for _ in range(len(values) + 1):
            el = q.dequeue()
            nelements -= 1
            print(f"Removeu da fila: {el}")
            assert el == values[el_index]
            el_index += 1
            assert len(q) == nelements
            if nelements:
                assert q.first() == values[el_index]

            # Quando a fila está vazia, acesso ao primeiro deve gerar exceção.
            try:
                print(f"Cabeça da fila: {q.first()}")
            except EmptyError:
                assert q.is_empty()
                assert len(q) == 0
                print("Tentativa de aceder à cabeça da fila com fila vazia gera exceção!")

    except EmptyError:
        assert q.is_empty()
        assert len(q) == 0
        print("Tentativa de retirar da fila com fila vazia gera exceção!")

    # Verifica estado final da fila
    print(f"Fila está vazia? {q.is_empty()}")

    print("+-------------------------------------------------------------------------------+")
    print("| Testes concluidos com sucesso.                                                |")
    print("+-------------------------------------------------------------------------------+")


def main():
    import profile

    testq = None

    def setup_queue_list(n):
        """
        Setup de uma Fila implementada com uma Lista, para teste de desempenho.
        Para usar em profile.profile_algorithm().

        :param n: Dimensão do stack.
        :return:  None
        """
        nonlocal testq
        testq = QueueUsingList()
        for i in range(n):
            testq.enqueue(i)

    def setup_queue_deque(n):
        """
        Setup de uma Fila implementada com uma deque, para teste de desempenho.
        Para usar em profile.profile_algorithm().

        :param n: Dimensão do stack.
        :return:  None
        """
        nonlocal testq
        testq = QueueUsingDeque()
        for i in range(n):
            testq.enqueue(i)

    def test_queue(n):
        """
        Para teste aos tempos de execução dos algoritmos que implementam Queues.
        Noatr que este teste, executa um valor fixo de operações, mas sobre
        uma fila de n valores.

        :param n: Número de elementos na queue (não usado)
        :return: None
        """
        for i in range(100000):
            testq.enqueue(i)
            testq.dequeue()

    test_queue_implementation(QueueUsingList)
    test_queue_implementation(QueueUsingDeque)

    
    # Remover os comentários seguintes para avaliar os tempos de execução das
    # duas implementações.
    # Note que, se estas usarem listas Python, as operações "no fim" são O(1),
    # mas as operações no início são O(n).
    # Usando o módulo Double Ended Queue (deque) as operações em ambas as
    # extremidades da fila são O(1).
    #
    profile_SQ.profile_algorithm(test_queue,
                               [10000, 20000, 30000, 40000, 50000],
                               "Queue - Implementação com lista.",
                               use_number_list=False,
                               setup=setup_queue_list,
                               adjust_for_length=False)
    #
    profile_SQ.profile_algorithm(test_queue,
                               [10000, 20000, 30000, 40000, 50000],
                               "Queue - Implementação com deque.",
                               use_number_list=False,
                               setup=setup_queue_deque,
                               adjust_for_length=False)


if __name__ == "__main__":
    main()

