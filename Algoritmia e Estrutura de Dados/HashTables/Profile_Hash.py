from faker import Faker
import time
from Hashtable_Chaining import HashTable as HashTableChaining
#from hashtable_probing import HashTable as HashTableProbing


def get_unique_names_using_list(phone_book):
    """
    Obtem lista de nomes únicos (sem repetições) existentes numa lista telefónica.
    Para guardar a lista de nomes usa uma lista Python que percorre para verificar duplicados.
    :param phone_book: Sequência de pares (nome, nº de telefone)
    :return: número de nomes únicos na lista telefónica.
    """
    unique_names = []
    for name, phonenumber in phone_book:
        first_name, last_name = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
        else:
            unique_names.append(first_name)
    return len(unique_names)


def get_unique_names_using_set(phone_book):
    """
    Obtem lista de nomes únicos (sem repetições) existentes numa lista telefónica.
    Para guardar a lista de nomes usa um Conjunto Python que evita duplicados.
    :param phone_book: Sequência de pares (nome, nº de telefone)
    :return: número de nomes únicos na lista telefónica.
    """
    unique_names = set()
    for name, phonenumber in phone_book:
        first_name, last_name = name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)


def get_unique_names_using_hashtable_chaining(phone_book):
    """
    Obtem lista de nomes únicos (sem repetições) existentes numa lista telefónica.
    Para guardar a lista de nomes usa uma hash table que evita duplicados.
    :param phone_book: Sequência de pares (nome, nº de telefone)
    :return: número de nomes únicos na lista telefónica.
    """
    unique_names = HashTableChaining(len(phone_book))
    for name, phonenumber in phone_book:
        first_name, last_name = name.split(" ", 1)
        unique_names.put(first_name, first_name)
    return len(unique_names)


# def get_unique_names_using_hashtable_probing(phone_book):
#     """
#     Obtem lista de nomes únicos (sem repetições) existentes numa lista telefónica.
#
#     Para guardar a lista de nomes usa uma hash table que evita duplicados.
#
#     :param phone_book: Sequência de pares (nome, nº de telefone)
#     :return: número de nomes únicos na lista telefónica.
#     """
#     unique_names = HashTableProbing(len(phone_book))
#     for name, phonenumber in phone_book:
#         first_name, last_name = name.split(" ", 1)
#         unique_names.put(first_name, first_name)
#     return len(unique_names)


def main():

    # Usar uma lista de fakers para garantir maior quantidade de nomes únicos.
    fakers = [Faker('pt_PT'), Faker('en_US'), Faker('en_UK'), Faker('es_ES'),
              Faker('fr_FR'), Faker('de_DE'), Faker('it_IT'), Faker('fi_FI')]

    print("A gerar lista telefónica. Aguarde ...")

    phonebook = set()
    for i in range(55000):
        for faker in fakers:
            name = faker.first_name() + " " + faker.last_name()
            phone_number = faker.phone_number()
            phonebook.add((name, phone_number))
        if i % 10000 == 0: print(".", end="")
    print()

    input(f"Lista telefónica gerada com {len(phonebook)} entradas. Prima tecla para continuar...")

    # Teste usando Python Set
    start = time.time()
    nr_names = get_unique_names_using_set(phonebook)
    end = time.time()
    print(f"Detetados {nr_names} nomes únicos na lista telefónica usando Set, em {end - start} segundos")

    # Teste usando Python List
    start = time.time()
    nr_names = get_unique_names_using_list(phonebook)
    end = time.time()
    print(f"Detetados {nr_names} nomes únicos na lista telefónica usando List, em {end - start} segundos")

    # Teste usando a nossa implementação da Hash Table com Chaining como estratégia de tratamento de colisões.
    start = time.time()
    nr_names = get_unique_names_using_hashtable_chaining(phonebook)
    end = time.time()
    print(f"Detetados {nr_names} nomes únicos na lista telefónica usando HashTable com Chaining, em {end - start} segundos")

    # # Teste usando a nossa implementação da Hash Table com Linear Probing como estratégia de tratamento de colisões.
    # start = time.time()
    # nr_names = get_unique_names_using_hashtable_probing(phonebook)
    # end = time.time()
    # print(f"Detetados {nr_names} nomes únicos na lista telefónica usando HashTable com Probing, em {end - start} segundos")


if __name__ == "__main__":
    main()