# Ir ao mercado se faltar comida ou for sábado
falta_comida = True
e_sabado = False
ir_ao_mercado = falta_comida or e_sabado

print(f"Devo ir ao mercado? {ir_ao_mercado}")

# Atravesso a rua se o sinal estiver vermelho e não vir carro da direita e não vir carro da esquerda
sinal_vermelho = True
carro_direita = False
carro_esquerda = False
atravesso_a_rua = sinal_vermelho and not carro_direita and not carro_esquerda

print(f"Devo atravessar a rua? {atravesso_a_rua}")

# Atravesso a rua se ou o sinal estiver vermelho ou não vir carro nem da direita nem da esquerda
atravesso_a_rua = sinal_vermelho or not (carro_direita and carro_esquerda)

print(f"Devo atravessar a rua? {atravesso_a_rua}")