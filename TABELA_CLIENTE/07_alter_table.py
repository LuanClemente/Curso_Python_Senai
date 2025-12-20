import sqlite3

conn = sqlite3.connect("../TABELA_CLIENTE/clientes.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE clientes
ADD COLUMN cliente BOOLEAN
""")

conn.commit()

print("Novo campo adicionado com sucesso.")

conn.close()
