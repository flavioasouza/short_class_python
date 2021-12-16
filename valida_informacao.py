def valida_idade():
    idade = int(input("Qual a sua idade? "))
    if idade >=0 and idade <=150:
        print(f"Parabéns você tem {idade} anos!")
    else:
        return "Idade inválida, tente novamente da próxima vez ;)"
print(valida_idade())

def valida_salario():
    salario = float(input("Digite seu salário: "))
    if salario>0:
        print(f"Seu salário é {salario}")
    else:
        return "Seu trabalho é voluntário? Se não, peça um aumento!! ;)"
print(valida_salario())

def valida_genero():
    genero = input("Digite um gênero: <M> para masculino, <F> para feminino ou <Outro> para outros: ").upper()
    if genero=='M':
        return "Você digitou " + genero
    elif genero=='F':
        return "Você digitou " + genero
    elif genero=="OUTRO":
        return "Você digitou " + genero
    else:
        return "Você digitou um gênero inválido, tente novamente mais tarde ;)"
print(valida_genero())