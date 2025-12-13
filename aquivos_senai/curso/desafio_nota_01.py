# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [ ] 1. O aluno deverá digitar 3 notas através do teclado
#   [ ] 2. Seu programa deverá calcular a média das notas    
#   [ ] 3. A partir da média, verificar qual situação o aluno se 
# encontra conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   [ ] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [ ] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro 
# de digitação
#   [ ] 6. Mostrar na tela para o aluno a situação final baseado na 
# nota digitada.

def main():

    nt1 = float(input("Digite sua nota 1: "))
    nt2 = float(input("Digite sua nota 2: "))
    nt3 = float(input("Digite sua nota 3: "))

    media = ((nt1 + nt2 + nt3) / 3) 
    media = round (media,2)
    

    
    if media >= 70 and media <= 100:
        print(f"Aluno Aprovado !!, media : {media}")
    elif media >= 40 and media < 70: 
        print(f"Aluno em exame/recuperacao, media : {media}")
    elif media >=0 and media < 40:
        print(f"Aluno Reprovado, media : {media}")
    else :
        print(f"media invalida")





if __name__ == "__main__":
    main()