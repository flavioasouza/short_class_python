print("Responda <s> para SIM ou <n> para NÃO, para as 5 perguntas seguintes: ")

pergunta_1 = input("Mora perto da vítima? ").lower()
if pergunta_1=='s':
    p1 = 1
else:
    p1 = 0

pergunta_2 = input("Já trabalhou com a vítima? ").lower()
if pergunta_2=='s':
    p2 = 1
else:
    p2 = 0

pergunta_3 = input("Telefonou para a vítima? ").lower()
if pergunta_3=='s':
    p3 = 1
else:
    p3 = 0

pergunta_4 = input("Esteve no local do crime ").lower()
if pergunta_4=='s':
    p4 = 1
else:
    p4 = 0

pergunta_5 = input("Devia para a vítima? ").lower()
if pergunta_5=='s':
    p5 = 1
else:
    p5 = 0

score = p1+p2+p3+p4+p5
if score==5:
    print(f"Sua pontuação é: {score}")
    print("Preso em nome da lei, você é o assassino!")
elif score == 3 or score == 4:
    print(f"Sua pontuação é: {score}")
    print("Preso em nome da lei, você é cumplice do crime!")
elif score == 2:
    print(f"Sua pontuação é: {score}")
    print("Mantenha-se na cidade, evite viagens, você é suspeito.")
else:
    print(f"Sua pontuação é: {score}")
    print("Obrigado pela sua cooperação, você está liberado.")


