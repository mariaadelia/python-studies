# 1.1 Escolha 3 objs com a função e receba o input do nome do objeto e dê um print na função dele
objetos_funcao = {"papel": "receber escrita", "caneta":"escrever","livro":"coleção de escritas"}
resp_usuario = input("Digite o objeto: ").lower()
if resp_usuario in objetos_funcao:
    print(f"Objeto {resp_usuario} tem a função de {objetos_funcao[resp_usuario]}")
else:
    print("Objeto não encontrado")

# 1.2 Crie uma lista contendo os números negativos de -30 a -20 e print a lista
lista_negativo = [x for x in range(-30,-19)]
print(f"Lista: {lista_negativo}")

# 1.3 Percorra os números de 4 a 100 e mantenha apenas os divisíveis por 4 e print a lista
lista_4_100 = [x for x in range(4,101) if x % 4 == 0]
print(f"Lista: {lista_4_100}")

# 1.4 Crie uma lista de 0 a 100, mas filtre apenas os números que terminam com 0
lista_termina_0 = [x for x in range(0,101) if x % 10 == 0]
# alternativa:
    # lista_termina_0 = [x for x in range (0,101) if str(x)[-1] == '0'] # Se a última posição for 0 (transformando em string para ver isso)
print(f"Lista: {lista_termina_0}")

# 1.4 Percorra os números de 0 a 20, e substitua por 0 os números que terminam com 0 e por '-' os outros
lista_0 = ['0' if x % 10 == 0 else '-' for x in range(0,21)]
print(f"Lista: {lista_0}")