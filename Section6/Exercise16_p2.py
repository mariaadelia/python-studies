import datetime

# 1.1 - recebe uma string e letra do alfabeto e retorna quantas vezes aparece. Se não aparecer nenhuma vez, retorna 0
def recorrencia_letra(frase, letra):
    repeticao = 0
    # for l in frase:
    #     if l in letra:
    #         repeticao += 1
    # Versão simplificada
    repeticao = frase.count(letra)
    return repeticao

print(recorrencia_letra("o carro é muito lindo e legal", "o"))

# 1.2 - recebe uma string e letra do alfabeto retorna uma lista contendo o índice de cada ocorrência da letra na string
def indices_letra(frase, letra):
    indice_repeticao = [i for i in range(len(frase)) if frase[i] in letra]
    indice_repeticao.sort()
    return indice_repeticao

print(indices_letra("corro","o"))
print(indices_letra("o carro é muito lindo e legal","o"))

# 1.3 - recebe um input do usuário e recebe também uma lista contendo palavras proibidas. A func retornará o input do usuário com * no lugar das palavras proibidas
def censura (frase, palavras_censuradas):
    for palavra in palavras_censuradas:
        if palavra in frase:
            frase = frase.replace(palavra, '*')
    return frase

palavras_censuradas = ["porcaria", "caramba", "daora"]
frase = input("Digite uma frase: ")
print(censura(frase, palavras_censuradas))

# 1.4 - retorna verdadeiro se a string é completamente minúscula ou maiúscula
def verifica_maiuscula_minuscula(frase):
    return frase.islower() or frase.isupper()

print(verifica_maiuscula_minuscula("O carro "))

# 1.5 - recebe string, identifica os valores inteiros, transforma em int e retorna como lista ordenada
def lista_int (lista):
    nova_lista = []
    for x in lista:
        if x.isdecimal():
            nova_lista.append(int(x))
    nova_lista.sort()
    return nova_lista

print(lista_int(["3","4","uds5","bala","c","2","1"]))

# 1.6 - recebe a data de nascimento e diga quantos dias já viveu
def count_dias_vida(data_nascimento):
    data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    dias_vividos = datetime.datetime.now() - data_nascimento
    return dias_vividos.days

data_user = input("Digite sua data de nascimento(dia/mês/ano): ")
print(count_dias_vida(data_user))

# 1.7 - recebe a próxima data de nascimento e mostra quantos dias faltam
def proximo_aniversario(data_nascimento):
    data_aniversario = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    dias_faltantes = data_aniversario - datetime.datetime.now()
    return dias_faltantes.days

data_user = input("Digite a próxima data do seu aniversário(dia/mês/ano): ")
print(proximo_aniversario(data_user))