
# for c in range (0,5):
#     peso = int(input('Qual o seu peso? '))
#     a = print(peso)


#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

# numero = int(input('Digite um número: '))

# for c in range(0,11):
#     if numero != 0:
#         resultado = numero * c

#         print(f' {numero} x {c} = {resultado}')

    
#03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
     
# maior = menor = 0

# for c in range(1,8):
#     ano_nascimento = int(input('Qual o ano de seu nascimento? '))
#     if 2021 - ano_nascimento >= 18:
#         maior += 1
#     else:
#         menor += 1
# print(f'O número de pessoas maior de idade é: {maior}')
# print(f'O número de pessoas menor de idade é: {menor}')

#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

# pares = 0
# soma = 0

# for c in range (1,7):
#     numero = int(input('Digite um número: '))
#     if numero % 2 == 0:
#         soma += numero
#         pares += 1

# print(f' A soma de números pares é igual a: {soma}')
# print(f'Foram digitados {pares} números pares')

# #01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)


x = soma = multi = maior = novos = sair = a = c = 0

while x < 2:
    valor = int(input('Digite um valor: '))
    soma += valor
    if x == 0:
        multi = valor
    else:
        multiplicacao = multi * valor
    a = valor
    if a < valor:
         b = valor
    else:
        c = a
    x += 1

print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')
    escolha = int(input('Digite o n° referente a sua escolha: '))
    if escolha == 1:
        print(soma)
    if escolha == 2:
        print(multiplicacao)
    if escolha == 3:
        if a < valor:
            print(b)
        else:
            print(c)
    if escolha == 4:
     x = 0
    if escolha == 5:
        print('Você saiu do programa!')

