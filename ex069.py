"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, motres:
a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos."""
cont18 = conth = contm = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Pessoas com mais de 18 anos: {cont18}')
print(f'Total de homens cadastrados: {conth}')
print(f'Total de mulheres com menos de 20 anos: {contm}')
