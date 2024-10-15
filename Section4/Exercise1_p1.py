# 1.1 Criar uma lista e printar a soma dos números
lista_num = [1,10,6,7,8,10]
soma=sum(lista_num)
print(f"A soma dos numeros da lista é {soma}")

# 1.2 Crie uma lista de 1 a 100 e imprima os valores
lista_1_100 = [x for x in range(1,101)]
print(f"Lista: {lista_1_100}")

# 1.3 Crie duas listas e concatene as duas (números repetidos não deve aparecer duas vezes)
lista1 = {30,4,43,52,65,-10}
lista2 = {43,2,4,76,32,65,3}
lista_union = lista1.union(lista2)
print(f"Lista unida: {lista_union}")

# 1.4 Crie uma lista com os meses do ano, receba o input do usuário de um número de 1 a 12 e imprima o mês correspondente
meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",
        11:"Novembro",12:"Dezembro"}
mes_nascimento = int(input("Digite seu mês de nascimento: "))
if mes_nascimento in meses:
    print(f"Você nasceu no mês de {meses[mes_nascimento]}")
else:
    print("Mês inválido")

# 1.5 Crie uma lista com os dias do mês que nasceu, receba o input do usuário do dia do nascimento e remova da lista
dia_mes = [x for x in range(1,32)]
dia_nascimento = int(input("Digite seu dia de seu nascimento: "))
if dia_nascimento in dia_mes:
    dia_mes.remove(dia_nascimento)
    print(f"Nova lista: {dia_mes}")
else:
    print("Dia inválido")