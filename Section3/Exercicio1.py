# 1.1 Recebe o saldo e quanto deve e printa se o saldo é negativo ou positivo
saldo_bancario = float(input("Digite seu saldo: ")) 
divida = float(input("Digite quanto você deve: ")) 
saldo_total = saldo_bancario - divida
saldo_negativo = "O seu saldo é negativo" if (saldo_total < 0) else "O seu saldo é positivo"
print(saldo_negativo)

# 1.2 Uma variável de cpf e outra de senha, recebe o input do usuário de tentativa de senha e printa o cpf (caso seja a certa) e acesso negado (caso seja a errada)
senha = "12@21"
cpf = "000.123.456-7"
senha_input = input("Digite sua senha: ")
if (senha_input == senha):
    print(f"Olá, seu cpf é {cpf}")
else:
    print("Senha incorreta")

# 1.3 Recebe a idade e mostra uma mensagem específica de acordo com a idade
idade_user = int(input("Digite sua idade: "))
mensagem = ""
if(idade_user <= 3):
    mensagem = "Você é um bebê"
elif (idade_user >= 4 and idade_user <= 13):
    mensagem = "Você é uma criança"
elif(idade_user >= 14 and idade_user <= 18):
    mensagem = "Você é um adolescente"
elif (idade_user >= 19 and idade_user <= 65):
    mensagem = "Você é um adulto"
else:
    mensagem = "Você é um idoso"

print(mensagem)

# 1.4 Calculadora básica que recebe dois inputs e a operação desejada
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada:\n'1' para soma\n'2' para subtração\n'3' para multiplicação\n'4' para divisão\nDigite: ")
resultado = 0

if(operacao == '1'):
    resultado = num_1 + num_2
    print(f"{num_1} + {num_2} = {resultado}")
elif (operacao == '2'):
    resultado = num_1 - num_2
    print(f"{num_1} - {num_2} = {resultado}")
elif(operacao == '3'):
    resultado = num_1 * num_2
    print(f"{num_1} * {num_2} = {resultado}")
elif(operacao == '4'):
    resultado = num_1 / num_2
    print(f"{num_1} / {num_2} = %.2f" %(resultado))
else:
    print("Opção inválida")