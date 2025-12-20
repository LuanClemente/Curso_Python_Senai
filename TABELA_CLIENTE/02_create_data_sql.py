import sqlite3

conn = sqlite3.connect("../TABELA_CLIENTE/clientes.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, data_registro)
VALUES ('Rodrigo', 30, '169.858.398-13', 'rd3@email.com', '11-98865-4321', 'Sao Paulo', 'SP', '2025-06-08')
""")

conn.commit()

print("Dados inseridos com sucesso.")

conn.close()