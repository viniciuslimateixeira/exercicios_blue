# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

lista = list()
lista_par = list()
lista_impar = list()

while True:
    numero = int(input('Insira um número na lista: '))
    lista.append(numero)
    if numero % 2 == 0:
        lista_par.append(numero)  
    else:
        lista_impar.append(numero)
    resp = input('Você deseja encerrar o programa? [S/N]: ').upper().strip()
    if resp == "S":
        break
print(f'A lista com todos os números digitados é: {lista}')
print(f'A lista com os números pares digitados é: {lista_par}')
print(f'A lista com os números ímpares digitados é: {lista_impar}')
