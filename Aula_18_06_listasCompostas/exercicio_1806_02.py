#01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lista = list()

for c in range(0,3):
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    lista.append([n1, n2, n3])
    if n1 % 2 == 0:
    elif n2 % 2 == 0:
    elif n3 % 2 == 0:
    soma_pares = n1 + n2 +n3
  
# for line in lista:
#     for number in line:
#         print(f'[ {number} ]', end=' ')
#     print('\n')

print(soma_pares)



#02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.