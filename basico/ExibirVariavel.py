ano_atual = int(input("Ano atual (yyyy): "))
ano_nasc = int(input("Ano de nascimento (yyyy): "))

idade = ano_atual - ano_nasc
print("Idade:", idade)

if idade >= 18:
    print("Apto a tirar a carteira")
else:
    print("Inapto para tirar a carteira")