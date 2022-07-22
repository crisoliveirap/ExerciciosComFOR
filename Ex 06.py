# Ex 06: Progressão aritmética
primeiro = int(input('Digite o número que você deseja que a progressão comece:'))
razao = int(input('Razão:'))
decimo = primeiro + 10 * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end='→ ')
print('Acabou')