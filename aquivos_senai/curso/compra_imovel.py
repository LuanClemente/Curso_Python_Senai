print("Bem vindo ao programa minha casa minha divida!!!")

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
renda = float(input("Qual a sua renda atual em R$? "))
valor_imovel = float(input("Qual o valor do imóvel desejado em R$? "))

entrada_20 = valor_imovel * 0.20
entrada_10 = valor_imovel * 0.10
aprovado = False
entrada_necessaria = 0.0

if idade < 21:
    print(f"{nome}, sua idade ({idade}) não é aprovada. Volte quando tiver 21 anos.")

elif renda < 2000.00:
    print(f"{nome}, sua renda atual (R${renda:.2f}) não atende ao mínimo exigido (R$2000.00).")

elif idade >= 21 and renda >= 3000.00:
    entrada_necessaria = entrada_20
    aprovado = True
    print(f"{nome}, você está APROVADO! Entrada necessária: R${entrada_necessaria:.2f} (20%).")

elif idade >= 25 and renda >= 2000.00:
    entrada_necessaria = entrada_10
    aprovado = True
    print(f"{nome}, você está APROVADO! Entrada necessária: R${entrada_necessaria:.2f} (10%).")

else:
    print(f"{nome}, não foi possível aprovar seu perfil com a idade de {idade} anos e renda de R${renda:.2f}.")

print("---")
if aprovado:
    pergunta_entrada = input("Você tem o dinheiro da entrada? (sim/não) ").lower()
    
    if pergunta_entrada == "sim":
        print(f'{nome}, Parabéns, você pode assumir uma nova dívida e agora ter "sua" casa!')
    else:
        print(f"{nome}, Reprovado! Você precisa da entrada de R${entrada_necessaria:.2f}, pegue com um agiota ou sei lá e retorne aqui com a grana!")