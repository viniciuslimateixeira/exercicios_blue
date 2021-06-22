# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))
tupla = (a, b, c, d)

print(tupla)
print(f' A quantidade de números 9 é = {tupla.count(9)}')
print(f' O número 3 está na posição = {tupla.index(3)}')



