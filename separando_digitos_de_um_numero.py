numero = int(input('Digite o número: '))

unidade = numero % 10
dezena = ((numero % 100) // 10)
centena = ((numero % 1000) // 100)
milhar = ((numero % 10000) // 1000)

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')