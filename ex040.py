"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
-Média abaixo de 5.0: reprovado
-Média entre 5.0 e 6.9: recuperação
-Média 7.0 ou superior: aprovado"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
print(f'A média das notas {n1} e {n2} é {media}')

if media < 5.0:
    print('reprovado')
elif media >= 7.0:
    print('aprovado')
else:
    print('recuperação')