numeros = []

tamanho = int(input("Quantos números são? "))


def media(numeros, tamanho):
    for i in range(tamanho):
        num = int(input("Digite um número: "))
        numeros.append(num)

    media = sum(numeros) / tamanho
    print(f"A média é: {media}")


media(numeros, tamanho)
