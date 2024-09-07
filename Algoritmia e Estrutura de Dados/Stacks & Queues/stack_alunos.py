import profile_SQ

class StackUsingListEnd:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return not bool(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if len(self._data) == 0:
            raise EmptyError("A stack está vazia!")

        return self._data.pop()    

    def top(self):
        if len(self._data) == 0:
            raise EmptyError("A stack está vazia!")

        return self._data[-1]    

    def __len__(self):
        return len(self._data)

    def __del__(self):
        self._data = None    


class StackUsingListStart:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return not bool(self._data)

    def push(self, item):
        self._data.insert(0,item)

    def pop(self):
        if len(self._data) == 0:
            raise EmptyError("A stack está vazia!")

        return self._data.pop(0)    

    def top(self):
        if len(self._data) == 0:
            raise EmptyError("A stack está vazia!")

        return self._data[0]    

    def __len__(self):
        return len(self._data)

    def __del__(self):
        self._data = None


class EmptyError(Exception):
    pass


def test_stack_implementation(stack_class, values=[5, 4, 3, 2, 1]):
    if "Start" in stack_class.__name__:
        test_desc  = "Teste à implementação de um stack usando operações 'no início' de uma lista"
    else:
        test_desc = "Teste à implementação de um stack usando operações 'no fim' de uma lista   "

    print(f"+-------------------------------------------------------------------------------+")
    print(f"| {test_desc}   |")
    print(f"+-------------------------------------------------------------------------------+")

    # Criar um stack
    st = stack_class()
    assert st.is_empty()             # Assegurar que stack é criado vazio.

    # Empilhar elementos descritos na lista "values".
    nelements = 0
    for value in values:
        print(f"Push {value} ...")
        st.push(value)
        nelements += 1
        assert not st.is_empty()     # Assegurar que stack não está vazio.
        assert len(st) == nelements  # Assegurar que dimensão é a correta.
        assert st.top() == value     # Assegurar que valor no topo é o correto.

    # Verificar que estado do stack está de acordo com os valores indicados para o teste
    assert st.is_empty() == False
    assert len(st) == len(values)
    assert st.top() == values[-1]

    try:
        # Tentar remover todos os itens + 1
        # (A última tentativa deve gerar uma exceção!)
        for _ in range(len(values) + 1):
            el = st.pop()
            nelements -= 1
            print(f"Fez pop de: {el}")
            assert el == values[nelements]   # Assegurar que valor retirado é o esperado.
            assert len(st) == nelements      # Assegurar que dimensão do stack foi atualizada.
            if nelements:
                assert st.top() == values[nelements - 1]  # Assegurar que valor no topo é o esperado.

            # Mostrar valor no topo do stack.
            # Deve gerar exceção quando stack estiver vazio. Bloco try serve para detetar esse caso.
            try:
                print("Valor no topo: " + str(st.top()))
            except EmptyError:
                assert len(st) == 0         # Assegurar que exceção foi gerada com dimensão = 0.
                print("Tentativa de aceder elemento do topo num stack vazio gera exceção!")

    except EmptyError:
        print("Tentativa de retirar elemento do stack vazio gera exceção!")

    # Verificar que o stack está vazio
    assert st.is_empty()                    # Assegurar que o stack está vazio no final.

    print("+-------------------------------------------------------------------------------+")
    print("| Testes concluidos com sucesso.                                                |")
    print("+-------------------------------------------------------------------------------+")


def main():
    import profile

    stk = None

    def setup_stack_list_start(n):
        
        nonlocal stk
        stk = StackUsingListStart()
        for i in range(n):
            stk.push(i)

    def setup_stack_list_end(n):
        """
        Setup de um stack operações "no fim", com n elementos, para teste de desempenho.
        Para usar em profile.profile_algorithm().

        :param n: Dimensão do stack.
        :return:  None
        """
        nonlocal stk
        stk = StackUsingListEnd()
        for i in range(n):
            stk.push(i)

    def test_stack(n):
        """
        Para teste aos tempos de execução dos algoritmos que implementam Stacks.
        Noatr que este teste, executa um valor fixo de operações, mas sobre
        um stack de n valores.

        :param n: Número de elementos no stack (não usado)
        :return: None
        """
        for i in range(100000):
            stk.push(i)
            stk.pop()

    test_stack_implementation(StackUsingListStart)
    test_stack_implementation(StackUsingListEnd)

    #
    # Remover os comentários seguintes para avaliar os tempos de execução das
    # duas implementações.
    # Note que, se estas usarem listas Python, espera-se que a implementação
    # com operações "no fim" seja O(1) e a implementação com operações
    # "no início" seja O(n).
    #
    profile_SQ.profile_algorithm(test_stack,
                               [10000, 20000, 30000, 40000, 50000],
                               "Stack - Implementação com lista. Operações no início.",
                               use_number_list=False,
                               setup=setup_stack_list_start,
                               adjust_for_length=False)
    #
    profile_SQ.profile_algorithm(test_stack,
                               [10000, 20000, 30000, 40000, 50000],
                               "Stack - Implementação com lista. Operações no fim.",
                               use_number_list=False,
                               setup=setup_stack_list_end,
                               adjust_for_length=False)


if __name__ == "__main__":
    main()

