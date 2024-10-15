# 1.1 Conta quantos caracteres tem (com exceção de espaços em branco) sem usar o len()
count = 0
user_input = input("Digite sua string: ")
for c in user_input:
    if(c != " "):
        count += 1
print(f"Sua string tem um total de {count} caracteres (com exceção de caracteres em branco)")



# 1.2 Fazer o cálculo do fatorial do número
num_usuario = int(input('Digite o número natural: '))
fatorial = 1

if(num_usuario >= 0):
    if(num_usuario == 0 or num_usuario == 1):
        fatorial = 1
    else:
        fim_num = 0
        for i in range(num_usuario, fim_num, -1):
            fatorial *= i

    print(f"{num_usuario}! = {fatorial}")

else:
    print(f"O número {num_usuario} não é natural")



# 1.3 Recebe uma quantidade de textos (definidas pelo usuário) e concatena tudo em uma string
string_final = " "
qtd_textos = int(input("Quantos textos você deseja receber? "))
index = 0
textos_recebidos = []

while(index < qtd_textos):
    texto = input("Digite o texto: ")
    textos_recebidos.append(texto)
    index += 1

for t in textos_recebidos:
    string_final += t + " " 

print (string_final)

# 1.4 - Tabuada de divisão de um número recebido por input
num_div = float(input("Digite o número que deseja a tabuada de divisão: "))
inicio_range = 1
fim_range = 11

for i in range(inicio_range, fim_range):
    divsion = i / num_div
    print(f"{i} : {num_div} = %.2f" %(divsion))




# Desafio: de 3 a 30 diz se o número é primo (divide apenas por si mesmo e 1) ou não
num_inicial = 3
num_final = 30

for i in range(3,31):
    # Crivo de Erastóstenes https://mundoeducacao.uol.com.br/matematica/numeros-primos.htm
    if(i % 2 != 0):
        if((i % 3 != 0) or (i == 3)):
            if((i % 5 != 0) or (i == 5)):
                if((i % 7 != 0) or (i == 7)):
                    print(f"{i} é primo")