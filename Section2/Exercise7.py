# 1.1 Recebe o input de 2 numeros e mostra divisão deles
num_1 = float(input("Insira o primeiro número: "))
num_2 = float(input("Insira o segundo número: "))
divisao = num_1/num_2
print(f"O resultado da divisão do número {num_1} pelo número {num_2} é de %.2f" %(divisao))

# 1.2 Recebe o input do usuário e mostra o dia, mês, ano, hora, minuto e segundo formatado
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
hora = int(input("Digite a hora(s): "))
minuto = int(input("Digite o minuto(s): "))
segundo = int(input("Digite o segundo(s): "))
print(f"{dia}/{mes}/{ano} {hora}:{minuto}:{segundo}")