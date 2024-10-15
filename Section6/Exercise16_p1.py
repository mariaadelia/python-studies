import math

# 1.1 - retorna a subtração de dois elementos considerando o valor absoluto deles
def soma_abs(a,b):
    a = abs(a)
    b = abs(b)
    return a - b

print(soma_abs(200,-100))

# 1.2 - retorna soma de dois valores, mas a soma não pode passar de 10000 e deve ser maior que 0 (sem usar if)
def soma(a,b):
    soma = a + b
    return max(1,min(soma,10000))

print(soma(10,-20))

# 1.3 - recebe argumento de tamanho arbitrário sendo todos os números e retorna o menor número entre eles
def menor_num(*args):
    return min(args)

print(menor_num(10,40,70,15000,-2))

# 1.4 - calcule bhaskara recebendo a, b e c por input
def baskhara (a,b,c):
    delta = pow(b,2) - 4*a*c
    if(delta < 0):
        return 'Valor negativo'
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

input_a = float(input("Digite o valor de a: "))
input_b = float(input("Digite o valor de b: "))
input_c = float(input("Digite o valor de c: "))

print(baskhara(input_a, input_b, input_c))


# 1.5 - inverte o que está maiúsculo para minúsculo e vice-versa
def inverte_maius_minus(frase):
    return frase.swapcase()

print(inverte_maius_minus("o caRRO é MuiTO lindo e LEGAL"))

