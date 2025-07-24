import random

alfabeto = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

random.shuffle(alfabeto)
letra = random.choice(alfabeto)

escolha = int(input(f"Em qual posição entre 0 a 25 você acha que esta a letra '{letra}'? "))
correta = alfabeto.index(letra)

if escolha > 25 or escolha < 0:
    print("Escolha uma posição entre 0 e 25!!!")

elif escolha == correta:
    print("Voce acertou")
else:
    print(f"Você errou, a posição correta da letra '{letra}' era {correta} ")


