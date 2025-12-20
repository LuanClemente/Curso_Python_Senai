import sqlite3
conn = sqlite3.connect("../TABELA_CLIENTE/clientes.db")
cursor = conn.cursor()

id_cliente = 1
novo_fone = "11-9500-2011"
novo_nome = "Paulo Silva"
novo_data_registro = "2025-06-11"

cursor.execute("""
UPDATE clientes
SET fone = ?, nome = ?, data_registro = ?
WHERE id = ?
""", (novo_fone, novo_nome, novo_data_registro, id_cliente))

conn.commit()

print("Dados Atualizados com sucesso.")

conn.close()