
def deprecia_valor():
    valor_atual = float(input("Digite um valor monetário: "))
    print(f"O valor atual é: {valor_atual}")
    valor_depreciado = valor_atual * 0.75
    print(f"O valor após depreciação de 15% é: {valor_depreciado}")

print(deprecia_valor())