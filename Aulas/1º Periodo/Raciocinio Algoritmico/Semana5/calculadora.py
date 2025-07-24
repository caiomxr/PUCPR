opcao = input("Escolha a operação: + = Soma | - = Subtração | / = Divisão | * = Multiplicação: ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if opcao == '+':
    print("Resultado:", n1 + n2)

elif opcao == '-':
    print("Resultado:", n1 - n2)

elif opcao == '/':
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Divisão por 0 nao existe! Volte para o fudamental por favor!!")

elif opcao == '*':
    print("Resultado:", n1 * n2)

else:
    print("ESCOLHA UMA OPÇÃO VALIDA!!!")
