anoNascimento = int(input("Em que ano voce nasceu? "))
anoAtual = int(2025)
idade = int(anoAtual - anoNascimento)
anoMeses = int(idade * 12)

print("A sua idade em meses: " + str(anoMeses))