# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escolar
#  [ ] 1. O aluno deverá digitar 3 notas através do teclado
#  [ ] 2. Seu programa deverá calcular a média das notas    
#  [ ] 3. A partir da média, verificar qual situação o aluno se encontra 
# conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#  [ ] 4. Não será permitido médias acima de 100 e abaixo de zero
#  [ ] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de 
# digitação
#  [ ] 6. Mostrar na tela para o aluno a situação final baseado na nota 
# digitada.
# ============= continuação =============================
#  [ ] 7. Acrescente no desafio anterior a frequencia de no minimo 75% 
# para ser aprovado
#  [ ] 8. O aluno pode ser aprovado se ele recebeu uma dispensa da 
#   disciplina
#  * Solicitar nome do aluno
# 1ª Dispensa  -> 2ª frequencia  -> 3ª média --> 4ª apresentar retorno

nome_aluno = input("Digite o nome do aluno: ")

dispensa_input = input("O aluno recebeu dispensa da disciplina? (S/N): ").lower()
dispensa = dispensa_input == 's'
frequencia_percentual = 0

if not dispensa:
    while True:
        try:
            frequencia_percentual = float(input("Digite a frequência do aluno (em %): "))
            if 0 <= frequencia_percentual <= 100:
                break
            else:
                print("Erro de digitação! A frequência deve estar entre 0 e 100.")
        except ValueError:
            print("Erro de digitação! Por favor, insira um número para a frequência.")
else:
    frequencia_percentual = 100 


nota1 = 0
nota2 = 0
nota3 = 0
media = -1 

while not (0 <= media <= 100):
    try:
        print("\n--- Digite as Notas de 0 a 100 ---")
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        nota3 = float(input("Digite a 3ª nota: "))

        media = (nota1 + nota2 + nota3) / 3

        if media < 0 or media > 100:
            print("Erro de digitação! A média calculada (%.2f) está fora do limite permitido (0 a 100)." % media)
            media = -1

    except ValueError:
        print("Erro de digitação! Por favor, insira apenas números para as notas.")
        media = -1
        
situacao_final = "INDEFINIDA"

frequencia_suficiente = dispensa or (frequencia_percentual >= 75)

if frequencia_suficiente:
    if media > 70:
        situacao_final = "APROVADO"  
    elif media < 40:
        situacao_final = "REPROVADO" 
    else:
        situacao_final = "EXAME/RECUPERAÇÃO" 
else:
    situacao_final = "REPROVADO POR FREQUÊNCIA"

print("\n=============================================")
print(f"FICHA DE SITUAÇÃO ESCOLAR DE {nome_aluno.upper()}")
print("---------------------------------------------")
print(f"Média das Notas: \t\t{media:.2f}")
print(f"Frequência: \t\t\t{frequencia_percentual:.1f}%")
print(f"Dispensa Recebida: \t\t{'Sim' if dispensa else 'Não'}")
print("---------------------------------------------")
print(f"SITUAÇÃO FINAL: \t\t**{situacao_final}**")
print("=============================================")