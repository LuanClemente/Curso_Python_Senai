import sqlite3

conn = sqlite3.connect("../TABELA_CLINTE/clientes.db")
cursor = conn.cursor()

id_cliente = 3

cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print("Registro Excluido com sucesso")

conn.close()