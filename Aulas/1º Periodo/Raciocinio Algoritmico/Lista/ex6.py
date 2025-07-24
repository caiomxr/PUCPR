pares = [numero for numero in range(1, 11) if numero % 2 == 0]
impar = [numero for numero in range(1, 11) if numero % 2 != 0]

lista = pares + impar


print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impar}")
print("___________________________________")
print(f"Lista final: {lista}")