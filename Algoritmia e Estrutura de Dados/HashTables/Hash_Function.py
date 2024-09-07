class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"

class HashTable:
    def __init__(self, capacity):
        self.max_size = capacity
        self.entries = [None] * self.max_size
        self.size = 0

    def hash_func(self, key):
        return sum(index*ord(char) for index, char in enumerate(repr(key). lstrip("'"), start=1)) % self.max_size

    def put(self, key, value):
        i = self.hash_func(key)
        if self.entries[i] is None:
            self.entries[i] = [Pair(key, value)]
        else:
            l = self.entries[i]
            for p in l:
                if p.key == key:
                    p.value = value
                    return
            l.append(Pair(key, value))
        self.size +=1

    def get(self, key):
        i = self.hash_func(key)
        if self.entries[i] is None:
            return None
        l = self.entries[i]
        for pair in l:
            if pair.key == key:
                return pair.value
        return None                            

    def delete(self, key):
        i = self.hash_func(key)
        if self.entries[i] is None:
            return
        l = self.entries[i]
        l2 = []
        for pair in l:
            if str(pair.key) != str(key):
                l2.append(pair)
        self.entries[i] = None if len(l2) == 0 else l2
        self.size -= 1

    def __len__(self):
        return self.size

    def print(self):
        for i in range(0, self.max_size):
            l = self.entries[i]
            if l is not None:
                self.print_list(l)                

    def print_list(self, l):
        if len(l) == 0:
            return
        for pair in l:
            print(str(pair), end =" ")
        print()    

def main():
    DIM_HASH_TABLE = 10
    MAX_ITEMS      = 100

    print("*******************************************")
    print("* A testar implementação da Hash Table... *")
    print("*******************************************")

    ht = HashTable(DIM_HASH_TABLE)

    for i in range(MAX_ITEMS):
        ht.put("KEY" + str(i), "VALUE " + str(i))
        assert ht.get("KEY" + str(i)) == "VALUE " + str(i)
    assert len(ht) == MAX_ITEMS
    print("* Inserção de valores com sucesso!        *")

    ht.print()

    for i in range(MAX_ITEMS):
        v = ht.get("KEY" + str(i))
        assert v == "VALUE " + str(i)
    print("* Pesquisa de chaves com sucesso!         *")

    for i in range(MAX_ITEMS):
        ht.put("KEY" + str(i), "MODIFIED VALUE " + str(i))
    assert len(ht) == MAX_ITEMS
    print("* Modificação de valores com sucesso!     *")

    for i in range(MAX_ITEMS):
        v = ht.get("KEY" + str(i))
        assert v == "MODIFIED VALUE " + str(i)
    print("* Chaves não podem ser duplicadas!        *")

    for i in range(MAX_ITEMS):
        ht.delete("KEY" + str(i))
        assert ht.get("VALUE " + str(i)) is None
    assert len(ht) == 0
    print("* Valores apagados com sucesso!           *")

    print("*******************************************")
    print("* Testes concluidos com sucesso.          *")
    print("*******************************************")


if __name__ == "__main__":
    main()