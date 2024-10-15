# 1.1 Recebe a nota da prova e a média e só é aprovado se a média for maior igual a 7 ou se a nota do prova for maior igual a 5
media = float(input("Digite sua média: "))
nota = float(input("Digite sua nota: "))
aprovado = (media >= 7) or (nota >= 5)
print(f"Aprovado: {aprovado}")

# 1.2 Dizer se a senha inputada é a correta
password = "BatataBatata00"
user_input = input("Digite a senha: ")
#Ternario no python
access_approved = "APROVADO" if user_input == password else "NEGADO"
print(f"Acesso {access_approved}")