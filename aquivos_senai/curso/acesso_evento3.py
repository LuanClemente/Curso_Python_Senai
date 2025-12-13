# Criar um programa que determine se uma pessoa pode participar de um evento 
# com base em sua idade e se está acompanhada por um responsável.
# Regras do Evento:
#  - Idade mínima para entrar desacompanhado: 18 anos.
#  - Pessoas com idade entre 12 e 17 anos;
#     - Podem entrar apenas se estiverem acompanhadas por um responsável com idade maior ou igual a 18 anos.
#  - Pessoas com menos de 12 anos não podem entrar, mesmo com responsável.
#
# ----------------------------------------------------------------------------

def regras_acesso_evento(idade, idade_responsavel, com_responsavel):
    if idade >= 18:
        return "Acesso permitido. \nBem-vindo ao evento!"
    elif idade >= 12 and idade < 18:
        if com_responsavel and idade_responsavel >= 18:
            return "Acesso permitido com responsável. \nBem-vindos ao evento!"
        else:
            return "Acesso negado. \nMenores de 18 anos devem estar acompanhados por um responsável maior de idade."


# ==============================================================================

print("Bem-vindo ao sistema de acesso ao evento!")
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 0:
            break
    except ValueError:
        print("Idade inválida. Por favor, insira uma idade válida.")
        
if idade >= 18:
    resultado = regras_acesso_evento(idade, 0, False)
    print(resultado)
if idade >= 12 and idade < 18:
    while True:
        try:
            com_responsavel = input("Você está acompanhado por um responsável? (s/n): ").lower() == 's'
            break
        except ValueError:
            print("Resposta inválida. Por favor, insira 's' ou 'n'.") 
    if com_responsavel:
        idade_responsavel = int(input("Digite a idade do responsável: "))
        resultado = regras_acesso_evento(idade, idade_responsavel, True)
        print(resultado)    
    else:
        resultado = regras_acesso_evento(idade, 0, False)
        print(resultado)
if idade < 12:
        print("Acesso negado. \nIdade insuficiente para participar do evento.")


# ==============================================================================