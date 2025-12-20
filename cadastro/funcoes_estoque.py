import sqlite3

# --- 1. Funções de Conexão e Inicialização do Banco de Dados ---

def conectar_bd(nome_bd="estoque.db"):
    """Conecta ao banco de dados e retorna o objeto de conexão."""
    conn = sqlite3.connect(nome_bd)
    return conn

def criar_tabela(conn):
    """Cria a tabela 'produtos' se ela ainda não existir."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    print("Tabela 'produtos' verificada/criada com sucesso!")

# --- 2. Funções CRUD ---

def adicionar_produto(conn, nome, descricao, preco, quantidade):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
                    (nome, descricao, preco, quantidade))
        conn.commit()
        print(f"Produto '{nome}' adicionado com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao adicionar produto: {e}")
        return False

def listar_produtos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return []
    
    print("\n--- Produtos Cadastrados ---")
    print(f"{'ID':<4} {'Nome':<20} {'Descrição':<30} {'Preço':<10} {'Qtd':<5}")
    print("-" * 75)
    for p in produtos:
        print(f"{p[0]:<4} {p[1]:<20} {p[2]:<30} R${p[3]:<9.2f} {p[4]:<5}")
    print("-" * 75)
    return produtos

def buscar_produto_por_id(conn, id_produto):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()
    if produto:
        print("\n--- Detalhes do Produto ---")
        print(f"ID: {produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Descrição: {produto[2]}")
        print(f"Preço: R${produto[3]:.2f}")
        print(f"Quantidade: {produto[4]}")
        return produto
    else:
        print(f"Produto com ID {id_produto} não encontrado.")
        return None

def atualizar_produto(conn, id_produto, nome=None, descricao=None, preco=None, quantidade=None):
    cursor = conn.cursor()
    set_clauses = []
    params = []

    if nome is not None: set_clauses.append("nome = ?"), params.append(nome)
    if descricao is not None: set_clauses.append("descricao = ?"), params.append(descricao)
    if preco is not None: set_clauses.append("preco = ?"), params.append(preco)
    if quantidade is not None: set_clauses.append("quantidade = ?"), params.append(quantidade)

    if not set_clauses:
        print("Nenhum campo para atualizar fornecido.")
        return False

    params.append(id_produto)
    query = f"UPDATE produtos SET {', '.join(set_clauses)} WHERE id = ?"

    try:
        cursor.execute(query, tuple(params))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Produto com ID {id_produto} atualizado com sucesso!")
            return True
        else:
            print(f"Produto com ID {id_produto} não encontrado.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao atualizar produto: {e}")
        return False

def deletar_produto(conn, id_produto):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Produto com ID {id_produto} removido com sucesso!")
            return True
        else:
            print(f"Produto com ID {id_produto} não encontrado.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao deletar produto: {e}")
        return False

def exibir_menu():
    print("\n--- Sistema de Controle de Produtos ---")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Buscar Produto por ID")
    print("4. Atualizar Produto")
    print("5. Deletar Produto")
    print("6. Sair")
    print("---------------------------------------")