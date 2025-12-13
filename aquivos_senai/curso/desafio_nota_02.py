# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escolar
#  [ ] 1. O aluno deverá digitar 3 notas através do teclado
#  [ ] 2. Seu programa deverá calcular a média das notas    
#  [ ] 3. A partir da média, verificar qual situação o aluno se encontra 
#       conforme notas abaixo:
#       3.1 media > 70 - aprovado
#       3.2 media < 40 - reprovado
#       3.3 media entre 40 e 70 - exame/recuperação
#  [ ] 4. Não será permitido médias acima de 100 e abaixo de zero (0)
#        4.1 Verificar nota < 0 or nota > 100;
#  [ ] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de 
#         digitação.
#  [ ] 6. Mostrar na tela para o aluno a situação final baseado na nota 
#         digitada.
# ============= continuação =============================
#  [ ] 7. Acrescente no desafio anterior a frequencia de no minimo 
#         75% para ser aprovado.
#  [ ] 8. O aluno pode ser aprovado se ele recebeu uma dispensa da 
#          disciplina.
#  * Solicitar nome do aluno
# 1ª Dispensa  -> 2ª frequencia  -> 3ª média --> 4ª apresentar retorno

def main():
    print ("---- Nota e Frequencia ------")
    nome = input("Digite o nome do aluno: ")
    dispensa = input("Você possui dispensa da disciplina (s/n): ").upper()

    # upper -> string que converte 
    # todos os caracteres de uma string para letras maiúsculas

    if dispensa == "S":
        print(f"{nome}, você esta aprovado por dispensa.")
    else:
        frequencia = int(input("Digite sua frequencia (%): "))
        while frequencia < 0 or frequencia > 100:
            print('Erro: Digite a frequencia correta (entre 0 e 100)') 
            frequencia = int(input("Digite sua frequencia (%): "))
        
        if frequencia < 75:
            print(f"{nome},Você Reprovou por frequencia !! {frequencia}% de presença")
            
        else:
            nt1 = float(input("Digite nota 1 (0 a 100): ")) 
            while nt1 < 0 or nt1 > 100:
                print(f'Nota incorreta {nt1}:')
                nt1 = float(input("Digite nota 1 (0-100): "))
                
            nt2 = float(input("Digite nota 2(0 a 100): "))
            while nt2 < 0 or nt2 > 100:
                print(f'Nota incorreta {nt2}:')
                nt2 = float(input("Digite nota 2 (0-100): "))
            
            nt3 = float(input("Digite nota 3 (0-100): "))
            while nt3 < 0 or nt3 > 100:
                print(f'Nota incorreta {nt3}:')
                nt3 = float(input("Digite nota 3 (0 - 100): "))
            
            media = ((nt1 + nt2 + nt3) / 3) 
            media = round (media,2)

            if media >= 0 and media <= 100:
                if media >= 70:
                    print(f"olá {nome}, sua media foi {media}, voce foi APROVADO.")
                elif media >= 40 and media < 70:
                    print(f"olá {nome}, sua media foi {media}, voce ficou em EXAME.")
                else:
                    print(f"olá {nome}, sua media foi {media},  voce foi REPROVADO.")
            else:
                print("Voce digitou um valor errado !!")

if __name__ == "__main__":
    main()

