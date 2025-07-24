import random

palavras = ['Vini', 'Nicolas', 'Marina', 'Mariana', 'Luisa', 'Paralelepipedo']

curta = min(palavras, key=len)
longa = max(palavras, key=len)

print(f"Palavra mais longa: {longa}")
print(f"Palavra mais curta: {curta}")