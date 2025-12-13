# Você recebeu um conjunto de dados contendo notas de alunos. 
# No entanto, houve um erro na importação e algumas notas vieram com valores (negativos ou acima de 10). 
# É necessário separar esses dados antes de calcular a média da turma.
# - Dados de Entrada:
#   * Utilize a seguinte lista de notas:
#     notas_alunos = [8.5, 9.0, -1.0, 7.2, 10.0, -5.0, 6.8, 11]
# Apresente no Relatorio
#  Notas Inválidas (Quantidade)
#    - valores
#  Notas Válidas (Quantidade)
#    - valores
#   Média Final
#    - valor

# ------------------------------------------------------------------------

notas_alunos = [8.5, 9.0, -1.0, 7.2, 10.0, -5.0, 6.8, 11]

# Listas para separar os dados
notas_validas = []
notas_invalidas = []

# PROCESSAMENTO: Separa as notas nas listas correspondentes
for nota in notas_alunos:
    if 0 <= nota <= 10:
        notas_validas.append(nota)
    else:
        notas_invalidas.append(nota)

# APRESENTAÇÃO: Exibe o relatório formatado
print("=" * 40)
print(f"{'RELATÓRIO DE NOTAS':^40}") # Centraliza o texto
print("=" * 40)

# Exibe notas inválidas (se houver)
print(f"Notas Inválidas ({len(notas_invalidas)}):")
if notas_invalidas:
    print(f"-> {notas_invalidas}")
else:
    print("-> Nenhuma nota inválida.")

print("-" * 40)

# Exibe notas válidas
print(f"Notas Válidas ({len(notas_validas)}):")
print(f"-> {notas_validas}")

print("=" * 40)

# CÁLCULO DA MÉDIA
if len(notas_validas) > 0:
    media = sum(notas_validas) / len(notas_validas)
    print(f"Média Final: {media:.2f}")
else:
    print("Média Final: Não foi possível calcular.")
    
print("=" * 40)