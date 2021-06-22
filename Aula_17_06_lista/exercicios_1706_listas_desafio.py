# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
lista = list()
jogos = list()

while True:
    escolha = input('Deseja fazer um jogo? [S/N]: ').upper().strip()[0]
    if escolha == 'S':
        for i in range(1,7):
            n = randint(1,60)
            lista.append(n)
    # if escolha == "N":
    #     break
    # # jogos.append(lista)
        print(lista)
