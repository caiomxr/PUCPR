lista = []

for i in range(3):
    num = int(input("Digite um numero: "))
    lista.append(num)

def maior(lista):
    print(f"O maior numero é: {max(lista)}")

maior(lista)