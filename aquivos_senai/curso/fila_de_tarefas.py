fila_de_tarefas = ["Imprimir relatório A", "Enviar e-mail de marketing", "Fazer backup do banco de dados", "Atualizar sistema"]
print("Iniciando processamento da fila de tarefas...")
# Enquanto a 'fila_de_tarefas' não estiver vazia...
while len(fila_de_tarefas) > 0:
# ...pegue a próxima tarefa da fila (a primeira).
    tarefa_atual = fila_de_tarefas.pop(0) # .pop(0) remove e retorna o primeiro item

    print(f"Processando: '{tarefa_atual}'...")
    # Simula o tempo de processamento
    # import time; time.sleep(1) 
    import time; time.sleep(5)
    print(f"Restam {len(fila_de_tarefas)} tarefas na fila.")

print("=" * 30)
print("Todas as tarefas foram processadas. Fila vazia!")