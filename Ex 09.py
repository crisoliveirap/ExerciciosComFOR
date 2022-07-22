# Ex 09: Grupo da Maioridade
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu?'))
    idade = atual - ano
    if idade < 18:
        menor += 1
    elif idade >= 18:
        maior += 1
print(f'Temos {menor} pessoas menores de idade.')
print(f'Temos {maior} pessoas maiores de idade.')