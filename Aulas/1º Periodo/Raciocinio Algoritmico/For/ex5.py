import random

vetor = []
for i in range(10):
    numero = random.randint(1, 100)
    vetor.append(numero)

print("numero:", vetor)

num = int(input("Escolha um Numero inteiro: "))


if num in vetor:
    print(f"O numero {num} está no vetor")
else:
    print(f"O numero {num} nao está no vetor")