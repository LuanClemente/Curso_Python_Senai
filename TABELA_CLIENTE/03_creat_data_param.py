import sqlite3

conn = sqlite3.connect("../TABELA_CLIENTE/clientes.db")
cursor = conn.cursor()

p_nome = input("Digite seu nome: ")
p_idade = input("Digite sua idade: ")
p_cpf = input("Digite seu CPF: ")
p_email = input("Digite seu Email: ")
p_fone = input("Digite o seu telefone: ")
p_cidade = input("Digite seu Cidade: ")
p_uf = input("Digite UF: ")
data_registro = input("Registrado em (aaaa-mm-dd): ")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, data_registro)
VALUES (?,?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, data_registro))

conn.commit()
print("Dados inseridos com sucesso")