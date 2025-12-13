"""
FUNÇÕES:

São operacoes para trabalhar com valores, especialmente
strings e listas, permitindo modificar, transformar ou reorganizar 
os dados durante a execução do programa. Essas operações incluem.

- alterar o conteudo de variaveis;
- aplicar operadores aritmeticos e logicas;
- realizar conversoes de tipos (como transformar numeros em texto)
- trabalhar com partes de textos (como cortar, juntar ou substituir)
- adicionar, remover ou acessar elementos em listas;
- organizar e preparar dados para exibição ou processamento

Essas tecnicas sao fundamentais para tornar os programas dinamicos e interativos,
permitindo que o Python reaja às entradas do usuario e produza saidas uteis personalizadas.



funções nativas(embutidas) em Python
print() 
len()
type()
input()
sum(), max(), min()
sorted () 
range()
zip()

"""
# #print()- exibe as informações no console
# print("Ola Mundo")

# #len() - Retorna o tamanho (numero de elemtnos) de uma coleção
# nomes = ['Ana', "Paulo", "Carlos"]
# print(len(nomes))

# #type() - Mostra o tipo de dado
# idade = 35
# print(type(idade))

# #input() - Recebe dados do usuario
# input()
# nome = input("Digite seu nome: ")
# print("Ola, ",nome)

# # sum(), max(), min() - operaçoes com listas numericas
# numeros = [10, 20, 30, 40]
# print(sum(numeros)) # soma todos os itens
# print(max(numeros)) # exibe maior valor da lista
# print(min(numeros)) # exibe menor valor da lista


# sorted () - ordenar uma lista (sem mudar o original)
# valores = [5, 2, 9, 1]
# ordenados = sorted(valores)
# print(ordenados)
# print(valores)

# range() - gera uma sequencia de numeros
# numero = 5
# for i in range(numero):
#     print(i+1)

# zip() - combina elementos de duas listas
nomes = ["Diego","Messi", "Cristiano Ronaldo"]
idades = [28,38,40]
for nome, idade in zip(nomes,idades):
    print(f"{nome} tem {idade} anos")