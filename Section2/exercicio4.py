# Mostrar a estimativa da idade baseada pelos anos
ano_atual = 2024
ano_nascimento = 1987
idade = ano_atual - ano_nascimento

print(f"A idade dessa pessoa é de {idade} anos")

# Média de 3 números
num1= 4
num2= 9
num3= 15
media = (num1 + num2 + num3) / 3

print("A média dos números é de %.3f" % media)

# Cálculo do IMC(kg/altura em metros ao quadrado)
peso = 100.2
altura = 1.59
IMC = peso / (altura ** 2)

print("O IMC é de %.2f" %IMC)

# Quantos ovos de páscoa devem ser dados para cada pessoa
pessoas = 3
ovos_pascoa = 7
divisao_ovos =  ovos_pascoa // pessoas
ovos_sobra = ovos_pascoa % pessoas

print(f"Cada pessoa receberá {divisao_ovos} ovo(s) de páscoa e sobrará {ovos_sobra} ovo(s)")