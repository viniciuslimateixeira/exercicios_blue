# Exercícios Tuplas:
# 01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
# Dica: utilizar a biblioteca random do Python.

from random import randint

n = (randint(1,50), randint(1,50), randint(1,50), randint(1,50), randint(1,50))
print(n)
print(f'O maior valor é: {max(n)}')
print(f'O menor valor é: {min(n)}')

