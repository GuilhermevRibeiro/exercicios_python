"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
a) quantas pessoas cadastradas
b) a média de idade
c) uma lista com mulhres
d) uma lista com idade acima da média."""

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] :')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] :')).upper()[0]
        if resp in 'SN':
            break
        print('erro. responda apenas S ou N')
    if resp == 'N':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma/ len(galera)
print(f'B: A média de idade é de {média:5.2f} anos')
print('C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()