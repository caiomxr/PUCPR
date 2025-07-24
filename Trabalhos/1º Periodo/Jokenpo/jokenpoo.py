#importar a biblioteca "ramdom"
import random

#Escolha de Modos
print("Escolha um modo:")
print("1 - Humano x Humano")
print("2 - Humano x Computador")
print("3 - Computador x Computador")


modo = input("Digite 1, 2 ou 3: ")

if modo == '1':
    nome1 = input("Digite o nome do Jogador 1: ")
    nome2 = input("Digite o nome do Jogador 2: ")
elif modo == '2':
    nome1 = input("Digite o nome do Jogador: ")
    nome2 = 'PC'
elif modo == '3':
    nome1 = 'PC 1'
    nome2 = 'PC 2'
else:
    print("Escolha uma opção valida!!!!")

#listar quais as opções para usar o ramdom
opcoes = ['pedra', 'papel', 'tesoura']

#"Placar"
v1 = 0
v2 = 0
empates = 0
continuar = 'continuar'

#Se voce quiser continuar a jogar
while continuar == 'continuar':

    print("    NOVA PARTIDA    ")

    # Escolha das opções para jogaR
    if modo == '1':
        p1 = input(nome1 + ", escolha pedra, papel ou tesoura: ")
        p2 = input(nome2 + ", escolha pedra, papel ou tesoura: ")
    elif modo == '2':
        p1 = input(nome1 + ", escolha pedra, papel ou tesoura: ")
        p2 = random.choice(opcoes)
        print(nome2 + " jogou: " + p2)
    else:
        p1 = random.choice(opcoes)
        p2 = random.choice(opcoes)
        print(nome1 + " jogou: " + p1)
        print(nome2 + " jogou: " + p2)

    # Jogo e acumular pontos
    if p1 == p2:
        print("Resultado: Empate!")
        empates = empates + 1
    elif p1 == "pedra" and p2 == "tesoura":
        print("Resultado:" + nome1 + " venceu!")
        v1 = v1 + 1
    elif p1 == "tesoura" and p2 == "papel":
        print("Resultado:" + nome1 + " venceu!")
        v1 = v1 + 1
    elif p1 == "papel" and p2 == "pedra":
        print("Resultado:" + nome1 + " venceu!")
        v1 = v1 + 1
    elif p2 == "pedra" and p1 == "tesoura":
        print("Resultado:" + nome2 + " venceu!")
        v2 = v2 + 1
    elif p2 == "tesoura" and p1 == "papel":
        print("Resultado:" + nome2 + " venceu!")
        v2 = v2 + 1
    elif p2 == "papel" and p1 == "pedra":
        print("Resultado:" + nome2 + " venceu!")
        v2 = v2 + 1
    else:
        print("Escolha uma opção valida!!!!")

    print("--------------")
    print("Placar:")
    print(nome1 + ":", v1, "vitória(s)")
    print(nome2 + ":", v2, "vitória(s)")
    print("Empates:", empates)
    print("--------------")


#Se voce deseja continuar ou sair do jogo
    continuar = input("Deseja continuar ou sair? ")

# FIM e tabela final de pontos
if continuar == 'sair':
    print("------------------")
    print("Placar final:")
    print(nome1 + ":", v1, "vitória(s)")
    print(nome2 + ":", v2, "vitória(s)")
    print("Empates:", empates)
    print("")
    print("Obrigado por jogar!!")
    print("Desenvolvido por: Caio Eduardo, Vinicius Yukiharu, João Lucas")