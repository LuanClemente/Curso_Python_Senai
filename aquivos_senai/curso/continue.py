notas_alunos = [8.5, 9.0, -1.0, 7.2, 10.0, -5.0, 6.8, 11]
soma_notas_validas = 0.0
quantidade_notas_validas = 0
soma_notas_invalidas = 0.0
quantidade_notas_invalidas = 0
notas_invalidas = [] 

print("--- Processando Notas dos Alunos ---")
for nota in notas_alunos:
    if nota < 0 or nota > 10:
        print(f"Nota inválida encontrada ({nota}). Ignorando cálculo válido...")
        soma_notas_invalidas += nota
        quantidade_notas_invalidas += 1
        notas_invalidas.append(nota)
        
    else:
        print(f"Nota válida processada: {nota}")
        soma_notas_validas += nota
        quantidade_notas_validas += 1

print("\n" + "=" * 30)

if quantidade_notas_validas > 0:
    media_validas = soma_notas_validas / quantidade_notas_validas
    print(f"Média das notas válidas: {media_validas:.2f}") 
else:
    print("Não há notas válidas para calcular a média.")

print("-" * 30)

if quantidade_notas_invalidas > 0:
    media_invalidas = soma_notas_invalidas / quantidade_notas_invalidas
    print(f"Média das notas inválidas: {media_invalidas:.2f}")
    print(f"Notas Inválidas: {notas_invalidas}")
else:
    print("Nenhuma nota inválida foi encontrada.")
    
print("=" * 30)