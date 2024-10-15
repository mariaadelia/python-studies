# 1.1 recebe uma lista e um valor qualquer e retorna um boolean dizendo se esse numero foi encontrado ou não
def existe_lista(lista, valor):
    if valor in lista:
        return True
    else:
        return False
    

valor = 'teste'
lista = [10,20,40,506,5, 'teste']
print(f"O valor {valor} existe na lista? {existe_lista(lista, valor)}")

# 1.1 recebe uma lista e um valor qualquer e retorna um boolean dizendo se esse numero foi encontrado ou não e a posição caso seja encontrado
def existe_lista(lista, valor):
    if valor in lista:
        return True, lista.index(valor)
    else:
        return False
    

valor = 'teste'
lista = [10,20,40,506,5, 'teste']
return_func = existe_lista(lista, valor)
if(return_func):
    print(f"O valor {valor} existe na lista? {return_func[0]}, na posição {return_func[1]}")
else:
    print(f"O valor {valor} existe na lista? {return_func}")


# 1.3 recebe parâmetros arbitrários e diga o tipo de cada um
def tipo_valor(*nova_lista):
    for x in nova_lista:
        print(f"{x} é do tipo {type(x)}")
    

tipo_valor(10, 'teste', True, 5.4)


# 1.4 recebe uma string com decorator que coloque aspas na string e que tudo esteja em lower case

def manipula_string(func):
    def lower_case(arg):
        return f'"{func(arg).lower()}"'
    return lower_case

@manipula_string
def citacao(string_texto):
    return string_texto


print(citacao("VAMOS VER O QUE ROLA"))


# 1.5 func recursiva que itere os números de 0 a 10 e printe o resultado da divisão inteira com o número 3

def recursiva_valor(valor1):
    if valor1 <= 10:
        print(f"{valor1} // 3 = {valor1 // 3}")
        valor1 += 1
        recursiva_valor(valor1)
    else:
        return
    

recursiva_valor(0)