# # nome = input("Digite seu nome: ") #Dando valor a variavel nome
# # idade = int(input("Digite sua idade: ")) #Dando valor a variavel idade

# # print(f"Olá, {nome}! Você tem {idade} anos de idade") #Utilizando o "F" de format
# # print(nome) #printando apenas a variavel nome
# # print(idade) #printando apenas a variavel idade

# # #=======================================================================================================================================#
# # print("============Sem o 'F' do format===============")
# # print("Nome: ",nome, "\nIdade: ",idade, "\n") #\n é para quebra de linha
# # #=======================================================================================================================================#
# # print("============Usando metodo format()============\n")
# # print("Nome: {}, Idade: {}\n".format(nome,idade))
# # #=======================================================================================================================================#
# # print("============Usando % na formatação============\n")
# # print("Nome: %s, Idade: %d"%(nome,idade))
# # # d = decimal inteiro s = string
# # mensagem = "Está é uma linha.\nE esta é outra linha."

# # print(mensagem)

# # mensagem_multilinha="""Esta é minha primeira linha.
# # Está é minha segunda linha."""

# # print(mensagem_multilinha)

# # #======================================================================================================================================#

# # print("======Exercico de uso do AND, OR e NOT======\n")

# # n1 = True
# # n2 = False

# # #operador and
# # res1 = n1 and n2
# # print("And: ", res1)

# # #Operador OR
# # res2 = n1 or n2
# # print ("OR: ", res2)

# # #Operador NOT

# # res3 = not n1
# # print("NOT: ", res3)

# #=======================================================================================================================================#

# # print("===========Operadores Lógicos===========\n")

# # idade = 32
# # altura = 1.75

# # resultado = (idade >= 18) and (altura >= 1.70)
# # msg = "Pode participar do evento? " + str(resultado)
# # print(msg)

# #=======================================================================================================================================#

# # print("==========Programa de disparo de alarme==========\n")

# # porta = "a"
# # janela = "f"

# # alarme = (porta == "f") and (janela == "a")

# # mgs = "Alarme disparado? " + str(alarme)
# # print(mgs)

# #=======================================================================================================================================#

# # print ("=Adição, subtração, multiplicação, divisão, resto da divisão e exponenciação=\n")

# # n1 = 10
# # n2 = 3

# # #adição
# # soma = n1 + n2
# # print("Adição: ", soma)

# # #subtração

# # sub = n1 - n2
# # print("Subtração: ", sub)

# # #multiplicação

# # mult = n1 * n2
# # print("Multiplicação: ", mult)

# # #divisão

# # div = n1 / n2
# # print("Divisão: ", div)

# # #resto da divisão

# # resto = n1 % n2
# # print("Resto da divisão: ", resto)

# # #exponenciação

# # exp = n1 ** n2
# # print("Exponenciação: ", exp)

#     # 1° parenteses ()
#     # 2° exponenciação
# #     # 3° multiplicação e divisão
# #     # 4° soma e subtração
# #     # calc = 2 * (2*3) + 1
# # calc = ((2*(2*3)) + 1)
# # print("Valor do Cálculo: ", calc)

# # x = y = z = 0

# # x = int (input("Digite um numero: "))
# # y = int (input("Digite outro numero: "))

# # z = x + y

# # print("A soma dos valores é ", z)

# # atribuição

# n1 = 3
# n2 = 2

# # igualdade relacionais
# #tem como resposta: true ou false

# #igualdade ==
# res1 = (n1 == n2)
# print(res1)

# #diferença !=
# res2 = (n1 != n2)
# print(res2)

# #maior que >
# res3 = (n1 > n2)
# print(res3)

# #menor que <
# res4 = (n1 < n2)
# print(res4)

# #maior ou igual >=
# res5 = (n1 >= n2)
# print(res5)

# #menor ou igual <=

# res6 = (n1 <= n2)
# print(res6)

x = y = z = False

print ("Digite um número: ")
n1 = int(input())
n2 = int(input("Digite outro número: "))

x = n1 == n2
print("São iguais? ", x, "\n")

z = n1 > n2
print(n1, "É maior que ", n2,'?', z, "\n")

y = n1 != n2
print("São diferentes? " + str(y))
