# 1.1 Recebe saldo do banco em string e desconta 1k desse valor
saldo_bancario = "15000"
saldo_menos_mil= float(saldo_bancario) - 1000
print(f"Seu novo saldo é de R${saldo_menos_mil}")

# 1.2 Indica se o saldo bancario está nulo
novo_saldo = 1000
saldo_nulo = not(bool(novo_saldo))
print(f"Seu saldo está nulo? {saldo_nulo}")

# 1.3 Programa que só mostra a parte inteira da altura
altura = 1.59
altura_inteira = int(altura)
print(f"A parte inteira da altura de {altura} m é de {altura_inteira} m")