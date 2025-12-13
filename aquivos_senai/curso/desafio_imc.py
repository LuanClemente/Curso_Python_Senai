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

print("--- Calculando o seu IMC --")

nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
    
imc = peso / (altura ** 2)
    
print(f"{nome}, seu IMC é {imc:.1f}")
    
if imc <= 18.5:
    print("Seu IMC está abaixo do normal")
elif imc <= 24.9:
    print("O seu IMC está normal")        
elif imc <= 29.9:
    print("O seu IMC está Sobrepeso")
elif imc <= 34.9:
    print("O seu IMC está Obesidade grau 1")
elif imc <= 39.9:
    print("O seu IMC está Obesidade grau 2")
else:
    print("O seu IMC está Obesidade grau 3")

