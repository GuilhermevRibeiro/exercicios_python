#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados ps: sem repetição

num = int(input('Digite um número entre 0 e 9999:'))
print(f'Analisando o número {num}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
