## Desenvolvimento de um agente baseado em IA (Teller_Agent) para realizar consultas de medicamentos de farmácia, utilizando a linguagem Python e o sistema métrico do CosineSimilarity (similaridade de cosseno)
#
# Descrição do ficheiro
# Curso: Engenharia Informática e Aplicações
# UC: Inteligência Artificial
# Trabalho: Teller Agent
#
# Número: a22206488
# Nome: Duarte Rodrigues
#
import numpy as np
from collections import defaultdict
from math import log, sqrt

# Conjunto de dados
# Medicamentos
perguntas_respostas = {
    'O que é Paracetamol?': 'Paracetamol é um medicamento utilizado para tratar dores e febres.',
    'O que é Ibuprofeno?': 'Ibuprofeno é um medicamento anti-inflamatório não esteroide usado para aliviar a dor, reduzir a febre e diminuir a inflamação.',
    'O que é Aspirina?': 'Aspirina é um medicamento usado para reduzir a dor, febre ou inflamação.',
    'O que é Amoxicilina?': 'Amoxicilina é um antibiótico usado para tratar várias infecções bacterianas.',
    'O que é Omeprazol?': 'Omeprazol é um medicamento utilizado para tratar problemas gástricos, como refluxo ácido e úlceras gástricas.',
    'O que é Metformina': 'Metformina é um medicamento usado para o tratamento de diabetes tipo 2.',
    'O que é Sinvastatina': 'Sinvastatina é um medicamento utilizado para controlar os níveis de colesterol no sangue.',
    'O que é Loratadina': 'Loratadina é um anti-histamínico utilizado para aliviar os sintomas de alergias.',
    'O que é Cetirizina': 'Cetirizina é um anti-histamínico usado para tratar sintomas de alergia, como espirros e coceira.',
    'O que é Pantoprazol': 'Pantoprazol é um medicamento utilizado para tratar esofagite de refluxo e outras condições relacionadas ao ácido estomacal.',
    'O que é Atorvastatina': 'Atorvastatina é um medicamento usado para baixar os níveis de colesterol e prevenir doenças cardiovasculares.',
    'Quais são os efeitos colaterais do Paracetamol': 'Os efeitos colaterais comuns do paracetamol incluem danos no fígado se tomado em doses muito altas.',
    'Quais são os efeitos colaterais do Ibuprofeno?': 'Os efeitos colaterais do ibuprofeno podem incluir dor de estômago, náusea, e tontura.',
    'Quais são os efeitos colaterais da Aspirina?' : 'Os efeitos colaterais comuns da aspirina incluem irritação estomacal, úlceras gástricas e aumento do risco de sangramento.',
    'Quais são os efeitos colaterais da Amoxicilina?': 'Os efeitos colaterais comuns da amoxicilina incluem náuseas, vômitos, diarreia e erupções cutâneas.',
    'Quais sáo os efeitos colaterais do Omeprazol?': 'Os efeitos colaterais comuns do omeprazol incluem dor de cabeça, náuseas, diarreia e prisão de ventre.',
    'Quais são os efeitos colaterais da Metformina?': 'Os efeitos colaterais comuns da metformina incluem problemas gastrointestinais, como náuseas e diarreia.',
    'Quais são os efeitos colaterais da Sinvastatina?': 'Os efeitos colaterais comuns da sinvastatina incluem dores musculares, fadiga e aumento dos níveis de açúcar no sangue.',
    'Quais são os efeitos colaterais da Loratadina?': 'Os efeitos colaterais comuns da loratadina incluem sonolência, boca seca e dor de cabeça.',
    'Quais sáo os efeitos colaterais do Pantoprazol?': 'Os efeitos colaterais comuns do pantoprazol incluem dor de cabeça, náuseas e diarreia.',
    'Quais são os efeitos colaterais da Atorvastatina?': 'Os efeitos colaterais comuns da atorvastatina incluem dores musculares, fadiga e dor de cabeça.',
}

# Função para calcular TF
def calcular_TF(documento):
    tf = defaultdict(int)
    for palavra in documento.split():
        tf[palavra.lower()] +=1
    for palavra in tf:
        tf[palavra] /= len(documento.split())
    return tf

# Função para calcular IDF
def calcular_IDF(documentos):
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
def calcular_TFIDF(tf, idf):
    tfidf = defaultdict(float)
    for palavra, valor in tf.items():
        tfidf[palavra] = valor * idf[palavra]
    return tfidf

# Função para vetorizar perguntas
def vetorizar_perguntas(perguntas):
    tfs = [calcular_TF(pergunta) for pergunta in perguntas]
    idf = calcular_IDF(perguntas)
    tfidfs = [calcular_TFIDF(tf, idf) for tf in tfs] 
    return tfidfs

# Função para calcular similaridade de cosseno
def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1[word] * vec2[word] for word in vec1 if word in vec2)
    norm1 = sqrt(sum(val ** 2 for val in vec1.values()))
    norm2 = sqrt(sum(val ** 2 for val in vec2.values()))
    return dot_product / (norm1 * norm2) if norm1 and norm2 else 0.0

# Função para encontrar a pergunta mais similar
def encontrar_pergunta_similar(consulta, perguntas, tfidfs):
    consulta_tf = calcular_TF(consulta)
    consulta_tfidf = calcular_TFIDF(consulta_tf, calcular_IDF(perguntas + [consulta]))
    similaridades = [cosine_similarity(consulta_tfidf, tfidf) for tfidf in tfidfs]
    index_max = np.argmax(similaridades)
    return perguntas[index_max], similaridades[index_max]

# Função de interface de usuário
def interface_usuario():
    print("Bem vindo ao Teller_Agent da farmácia!")
    print("Digite a sua pergunta ou 'sair' para encerrar:")

    while True:
        pergunta_cliente = input("Você: ")
        if pergunta_cliente.lower() == 'sair':
            print("Obrigado por utilizar o Teller_Agent. Até já!")
            break
        pergunta_similar = encontrar_pergunta_similar(pergunta_cliente, perguntas, tfidfs)
        resposta =perguntas_respostas[pergunta_similar]
        print(f"{resposta}")

# Vetorizar perguntas
perguntas = list(perguntas_respostas.keys())
tfidfs = vetorizar_perguntas(perguntas)

# Executrar a interface de usuário
interface_usuario()