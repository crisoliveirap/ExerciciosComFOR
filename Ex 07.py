# Ex 07: Números primos
num = int(input('Digite um número:'))
divisiveis = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        divisiveis += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, divisiveis))
if divisiveis == 2:
    print('Portanto ele é um número PRIMO!')
else:
    print('Portanto ele NÃO É um número primo!')
