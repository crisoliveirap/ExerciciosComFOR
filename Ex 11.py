# Ex 11: Analisando dados
soma = 0
maior_idade = 0
total_mulher = 0
nome_maisvelho = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    soma += idade
    media = soma / 4
    if sexo not in 'F':
        if c == 1:
            maior_idade = idade
            nome_maisvelho = nome
        elif idade > maior_idade:
            maior_idade = idade
            nome_maisvelho = nome
    if sexo in 'F':
        if idade < 20:
            total_mulher += 1
print(f'O homem mais velho tem {maior_idade} anos e se chama {nome_maisvelho}.')
print(f'A média de idade do grupo é {media} anos.')
print(f'Ao todo são {total_mulher} mulheres com menos de 20 anos.')