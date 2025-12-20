import sqlite3

conn = sqlite3.connect("../TABELA_CLIENTE/clientes.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome    TEXT NOT NULL,
        idade   INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email   TEXT NOT NULL,
        fone    TEXT,
        cidade  TEXT,   
        uf      VARCHAR(2) NOT NULL,
        data_registro   DATE NOT NULL
);
""")

print("Tabela Criada com Sucesso.")

conn.close()