# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais 
# clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada 
# um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos 
# são menores de idade.

dados = list()
maior = menor = 0

for c in range(1,4):
    n = str(input('Digite seu nome: ' )).strip()
    i = int(input('Qual a sua idade: '))
    # lista = [n,i]
    dados.append([n,i])
    if i >= 18:
        maior += 1
    if i <= 18:
        menor += 1
for p, v in enumerate(dados):
    if v[1] >= 18:
        m = max(dados)
        print(f'{v[0]} é maior de idade')
    if v[1] <= 18:
        n = min(dados)
        print(f'{v[0]} é menor de idade')
print(f'{m[0]} é o mais velho com {m[1]} anos')
print(f'{n[0]} é o mais novo com {n[1]} anos')
print(f'{maior} pessoas são maiores de idade')
print(f'{menor} pessoas são menores de idade')
print(dados)


    



