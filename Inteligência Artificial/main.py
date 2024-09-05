import numpy as np
from collections import defaultdict
from math import log, sqrt

# Conjunto de dados de exemplo
perguntas_respostas = {
    "O que é paracetamol?": "Paracetamol é um medicamento utilizado para tratar dores e febres.",
    "Quais são os efeitos colaterais do ibuprofeno?": "Os efeitos colaterais do ibuprofeno podem incluir dor de estômago, náusea, e tontura."
}

# Função para calcular TF
def calcular_tf(documento):
    tf = defaultdict(int)
    for palavra in documento.split():
        tf[palavra.lower()] += 1
    for palavra in tf:
        tf[palavra] /= len(documento.split())
    return tf

# Função para calcular IDF
def calcular_idf(documentos):
    idf = defaultdict(int)
    total_documentos = len(documentos)
    for documento in documentos:
        palavras_unicas = set(documento.split())
        for palavra in palavras_unicas:
            idf[palavra.lower()] += 1
    for palavra in idf:
        idf[palavra] = log(total_documentos / (1 + idf[palavra]))
    return idf

# Função para calcular TF-IDF
def calcular_tfidf(tf, idf):
    tfidf = defaultdict(float)
    for palavra, valor in tf.items():
        tfidf[palavra] = valor * idf[palavra]
    return tfidf

# Função para vetorizar perguntas
def vetorizar_perguntas(perguntas):
    tfs = [calcular_tf(pergunta) for pergunta in perguntas]
    idf = calcular_idf(perguntas)
    tfidfs = [calcular_tfidf(tf, idf) for tf in tfs]
    return tfidfs

# Função para calcular similaridade de cosseno
def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1[word] * vec2[word] for word in vec1 if word in vec2)
    norm1 = sqrt(sum(val ** 2 for val in vec1.values()))
    norm2 = sqrt(sum(val ** 2 for val in vec2.values()))
    return dot_product / (norm1 * norm2) if norm1 and norm2 else 0.0

# Função para encontrar a pergunta mais similar
def encontrar_pergunta_similar(consulta, perguntas, tfidfs):
    consulta_tf = calcular_tf(consulta)
    consulta_tfidf = calcular_tfidf(consulta_tf, calcular_idf(perguntas + [consulta]))
    similaridades = [cosine_similarity(consulta_tfidf, tfidf) for tfidf in tfidfs]
    index_max = np.argmax(similaridades)
    return perguntas[index_max], similaridades[index_max]

# Vetorizar perguntas
perguntas = list(perguntas_respostas.keys())
tfidfs = vetorizar_perguntas(perguntas)

# Interface de consola
def interface_consola():
    print("Bem-vindo ao Teller_Agent. Digite 'sair' para terminar.")
    while True:
        consulta = input("Digite sua pergunta: ")
        if consulta.lower() == 'sair':
            print("Encerrando o Teller_Agent. Até logo!")
            break
        pergunta_similar, score = encontrar_pergunta_similar(consulta, perguntas, tfidfs)
        resposta = perguntas_respostas[pergunta_similar]
        print(f"Pergunta Similar Encontrada: {pergunta_similar}")
        print(f"Resposta: {resposta}")

# Executar a interface de consola
interface_consola()