# 1.1 verifica se o número é ou não negativo
def e_negativo(num):
    if num < 0:
        return True
    else:
        return False
    
user_input_1 = int(input("Digite um número: "))
print(f"O número é negativo? {e_negativo(user_input_1)}")

# 1.2 recebe um  array de números e retorna a soma
def soma(nums):
    return sum(nums)

nums_soma = [1,2,3,4,5,6]
print(f"A soma do array {nums_soma} é {soma(nums_soma)}")

# 1.3 recebe uma string e retorna o número de vogais
def vogais(strings):
    vogais = "aeiou"
    soma = 0
    for l in strings:
        if l in vogais:
            soma += 1
    return soma

user_input_3 = input("Digite uma palavra: ")
print(f"O número de vogais em {user_input_3} é {vogais(user_input_3)}")

# 1.4 receba uma string e retorna o último caractere
def ultimo_caractere(word):
    return word[-1]

user_input_4 = input("Digite uma palavra: ")
print(f"O último caractere de {user_input_4} é {ultimo_caractere(user_input_4)}")

# 1.5 recebe 2 nums e uma string que indica se é soma ou subtração
def operacoes(num1,num2,op):
    
    def soma(num_a,num_b):
        return num_a + num_b
    
    def sub(num_a,num_b):
        return num_a - num_b
    
    if (op == '+'):
        return soma(num1, num2)
    elif (op == '-'):
        return sub(num1, num2)
    else:
        return 'Operação inválida'
    
user_input_1 = float(input("Digite o primeiro número: "))
user_input_2 = float(input("Digite o segundo número: "))
input_operacao = input("Digite a operação (+ ou -): ")

print(f"{user_input_1} {input_operacao} {user_input_2} = {operacoes(user_input_1, user_input_2, input_operacao)}")