import re
import math

def quantidadeTotalDeCaracteres(conjuntos):
    quantidadeCaracteres = 0

    for conjunto in conjuntos:
        quantidadeCaracteres += len(conjunto)

    return quantidadeCaracteres


def TamanhoMedioDasPalavras(palavras):

    return (quantidadeTotalDeCaracteres(palavras) / len(palavras))

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    somatorio = 0

    for i in range(0, 6):
        somatorio += math.fabs(as_a[i] - as_b[i])

    somatorio = (somatorio / 6)
    return round(somatorio, 2)


def calcula_assinatura(texto):
    frases = []
    palavras = []


    sentencas = separa_sentencas(texto)


    for sentenca in sentencas:
        frases += separa_frases(sentenca)


    for frase in frases:
        palavras += separa_palavras(frase)


    wal = TamanhoMedioDasPalavras(palavras)
    ttr = (n_palavras_diferentes(palavras) / len(palavras))
    hlr = (n_palavras_unicas(palavras) / len(palavras))
    sal = (quantidadeTotalDeCaracteres(sentencas) / len(sentencas))
    sac = (len(frases) / len(sentencas))
    pal = (quantidadeTotalDeCaracteres(frases) / len(frases))

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    comparacoes = []

    for texto in textos:
        assinatura = calcula_assinatura(texto)
        comparacao = compara_assinatura(assinatura, ass_cp)
        comparacoes.append(comparacao)

    menorComparacao = min(comparacoes)
    indiceMenorComparacao = (comparacoes.index(menorComparacao) + 1)
    print("O autor do texto {} está infectado com COH-PIAH".format(indiceMenorComparacao))

    return indiceMenorComparacao


def main():
    
    ass_cp = le_assinatura()
    
    textos = le_textos()
    
    avalia_textos(textos, le_assinatura())

main()
