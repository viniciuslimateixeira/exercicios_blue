# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

l = [input("Telefonou para a vítima?").upper().strip(), input("Esteve no local do crime?").upper().strip(), input("Mora perto da vítima?").upper().strip(), input("Devia para a vítima?").upper().strip(), input("Já trabalhou com a vítima?").upper().strip()]
b = l
p = b.count(S)
print(p)

