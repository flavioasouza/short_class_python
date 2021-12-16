# Neste caso o exercício pedia somente a tabuada do 9,
# mas resolvi deixar dinâmico, realizando algumas modificações.

tabuada = int(input("\nDigite o número da tabuada desejada: "))
print(f"\nTabuada do número {tabuada}:")
for valor in range(1,11,1):
    print(f'{tabuada} x {valor} = {tabuada*valor}')
