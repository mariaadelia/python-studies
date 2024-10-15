# 1.1 String que tenha nome e sobrenome, depois dividir a sting em outras duas var de nome e sobrenome
nome_completo = "Joao Paulo Pereira Souza"
nome = nome_completo[:10]
sobrenome = nome_completo[11:]
print(f"Seu nome é: {nome}\nSeu sobrenome é: {sobrenome}")

# 1.2 Ler um input e tirar o último caracter
user_input = input("Digite sua palavra / frase aqui: ")
input_sem_ultimo = user_input[:(len(user_input)-1)]
print(f"Input sem o último caracter: {input_sem_ultimo}")

# 1.3 Ler um input e dizer se tem vogal
tem_vogal = ('a' in user_input.lower()) or ('e' in user_input.lower()) or ('i' in user_input.lower()) or ('o' in user_input.lower()) or ('u' in user_input.lower())
print(f"O input '{user_input}' tem vogal? {tem_vogal}")

# 1.4 - Adicionar ABC na primeira posição da string
new_string = "ABC" + user_input[0:]
print(f"Nova string: {new_string}")