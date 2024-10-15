# 1.1 - recebe 5 números e retorna a média
count = 1
soma = 0
while( count <= 5):
    num = float(input(f"Digite o {count}° número: "))
    soma += num
    count += 1

media = soma/5
print(f"A média desses números é de %.2f" %(media))

# 1.2 - recebe 5 números e soma eles, caso seja negativo não considerar
contador = 1
somar = 0
while( contador <= 5):
    numero = float(input(f"Digite o {contador}° número: "))
    if(numero >= 0):
        somar += numero
    contador += 1

print(f"A soma desses números é de %.2f" %(somar))

# 1.3 - recebe 5 a quantidade de números definidos pelo usuário e realiza a soma de todos eles
cont = int(input("Quantos números você deseja adicionar? "))
indice = 1
add = 0
while( indice <= cont):
    num = float(input(f"Digite o {indice}° número: "))
    add += num
    indice += 1

print(f"A soma desses números é de %.2f" %(add))


# 1.4 - percorra de 2 até 10 e diga se é par ou ímpar
num_inicio = 2
num_final = 10

while( num_inicio <= num_final):
    if(num_inicio % 2 == 0):
        print(f"{num_inicio} é PAR")
    else:
        print(f"{num_inicio} é ÍMPAR")
    num_inicio += 1

# 1.5 - Recebe uma string e identifica quantos espaços em branco tem
user_string = input("Digite sua string: ")
indice_string = 0
count_string = 0

while( indice_string < len(user_string)):
    letras = user_string[indice_string]
    if(letras == " "):
        count_string += 1

    indice_string += 1

print(f"O total de espaços em branco é de: {count_string}")