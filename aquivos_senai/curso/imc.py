# Desafio - Calculo do IMC
# Desenvolver um programa que calcule do IMC da pessoa:
# Requisitos:
# [ ] Peso e altura da pessoa será digitado pelo teclado (dica: usar input() e
# converter usando o float () );
# [ ] A pessoa vai se identificar atraves do nome (Dica: usar input() );
# [ ] Realizar o calculo padrão do IMC (Dica: usar operadores aritmeticos e variaveis);
# [ ] Apresentar o resultado na tela com  o Nome e o Valor do IMC (Dica: usar o print()com
#     formatação print(f") e as variaveis).
# IMC = Peso / (Altura ^ 2)
# IMC = Peso / (Altura ** 2) python
# =========================================================================================
#  - Verificar indice de classificação conforme resultado do IMC
#  - Apresentar mensagem
#     ex: 'IMC abaixo do normal', 'IMC normal', 'sobrepeso', 
#         'Obesidade grau 1', 'Obesidade grau 2','Obesidade grau 3'
#
# ------------------------------------------------------------------------------------------

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg (ex: 75.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = 'IMC abaixo do normal'
elif imc < 24.9:
    classificacao = 'IMC normal'
elif imc < 29.9:
    classificacao = 'Sobrepeso'
elif imc < 34.9:
    classificacao = 'Obesidade Grau I'
elif imc < 39.9:
    classificacao = 'Obesidade Grau II (Severa)'
else:
    classificacao = 'Obesidade Grau III (Mórbida)'

print(f"Resultado do Cálculo do IMC para **{nome}**:")
print(f"Seu IMC é: **{imc:.2f}**")
print(f"Classificação: **{classificacao}**")
