# # Cada lista interna representa as notas de um aluno 
# tabela_de_notas = [ 
#     ['Ana', 8.5, 9.0],    # Aluno 1: Nome, Nota Prova 1, Nota Prova 2 
#     ['Bruno', 7.0, 6.5],   # Aluno 2 
#     ['Carla', 9.5, 10.0]   # Aluno 3 
# ] 

# # Acessar a nota da segunda prova de Bruno (linha 1, coluna 2) 
# nota_bruno = tabela_de_notas[1][2] 
# print(f"A segunda nota de {tabela_de_notas[1][0]} foi: {nota_bruno}") # Saída: A segunda nota de Bruno foi: 6.5 

# nota_ana = tabela_de_notas[0][1] 
# print(f"A primeira nota da {tabela_de_notas[0][0]} foi: {nota_ana}")

# nota_carla = tabela_de_notas[2][1] 
# print(f"A primeira nota da {tabela_de_notas[2][0]} foi: {nota_carla}")


# # Imprimir o nome de todos os alunos 
# print("\nAlunos na turma:") 
# for aluno in tabela_de_notas: 
#     print(f"- Nome: {aluno[0]} - Primeira nota: {aluno[1]} - Segunda nota: {aluno[2]}")

numeros_pares = [] # Começamos com uma lista vazia 
numeros_impares = [] # Começamos com uma lista vazia

print("Digite 5 números e eu guardarei e separarei em pares e ímpares.") 
for i in range(5): 
    numero = int(input(f"Digite o {i+1}º número: ")) 
    if numero % 2 == 0:  # Verifica se o número é par 
        numeros_pares.append(numero)
    else: # Verifica se o número é impar 
        numeros_impares.append(numero)

print(f"\nOs números pares que você digitou foram: {numeros_pares}")

print(f"\nOs números impares que você digitou foram: {numeros_impares}") 
