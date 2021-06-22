# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = list()
numero = 0

while True:
    numero = int(input('Insira um número na lista: '))
    if numero not in lista:
        lista.append(numero)     
    resp = input('Você deseja encerrar o programa? [S/N]: ').upper().strip()[0]
    if resp == "S":
        break
print(sorted(lista))