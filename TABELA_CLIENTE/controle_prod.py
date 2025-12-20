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

# --- 2. Funções CRUD (Create, Read, Update, Delete) ---

def adicionar_produto(conn, nome, descricao, preco, quantidade):
    """Adiciona um novo produto ao banco de dados."""
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
    """Lista todos os produtos no banco de dados."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall() # Retorna todos os resultados
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
    """Busca um produto pelo ID."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone() # Retorna apenas um resultado
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
    """Atualiza as informações de um produto existente."""
    cursor = conn.cursor()
    set_clauses = []
    params = []

    if nome is not None:
        set_clauses.append("nome = ?")
        params.append(nome)
    if descricao is not None:
        set_clauses.append("descricao = ?")
        params.append(descricao)
    if preco is not None:
        set_clauses.append("preco = ?")
        params.append(preco)
    if quantidade is not None:
        set_clauses.append("quantidade = ?")
        params.append(quantidade)

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
            print(f"Produto com ID {id_produto} não encontrado para atualização.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao atualizar produto: {e}")
        return False

def deletar_produto(conn, id_produto):
    """Remove um produto do banco de dados."""
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Produto com ID {id_produto} removido com sucesso!")
            return True
        else:
            print(f"Produto com ID {id_produto} não encontrado para remoção.")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao deletar produto: {e}")
        return False

# --- 3. Menu Interativo para o Usuário ---

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Sistema de Controle de Produtos ---")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Buscar Produto por ID")
    print("4. Atualizar Produto")
    print("5. Deletar Produto")
    print("6. Sair")
    print("---------------------------------------")

#  <----------------------------------------------------------->

def main():
    
    conn = conectar_bd()
    criar_tabela(conn)
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- Adicionar Novo Produto ---")
            nome = input("Nome do Produto: ")
            descricao = input("Descrição (opcional): ")
            try:
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                adicionar_produto(conn, nome, descricao, preco, quantidade)
            except ValueError:
                print("Preço e Quantidade devem ser números válidos.")
    
        elif opcao == "2":
            listar_produtos(conn)
        
        elif opcao == "3":
            try:
                id_busca = int(input("Digite o ID do produto para buscar: "))
                buscar_produto_por_id(conn, id_busca)
            except ValueError:
                print("O ID deve ser um número inteiro.")
        
        elif opcao == "4":
            print("\n--- Atualizar Produto ---")
            try:
                id_atualizar = int(input("Digite o ID do produto para atualizar: "))
                produto_existente = buscar_produto_por_id(conn, id_atualizar)
                if produto_existente:
                    print("Deixe o campo em branco para não alterar o valor atual.")
                    novo_nome = input(f"Novo Nome ({produto_existente[1]}): ") or None
                    nova_descricao = input(f"Nova Descrição ({produto_existente[2]}): ") or None

                    novo_preco_str = input(f"Novo Preço (R${produto_existente[3]:.2f}): ")
                    novo_preco = float(novo_preco_str) if novo_preco_str else None
                    nova_quantidade_str = input(f"Nova Quantidade ({produto_existente[4]}): ")
                    nova_quantidade = int(nova_quantidade_str) if nova_quantidade_str else None

                    atualizar_produto(conn, id_atualizar, novo_nome, nova_descricao, novo_preco, nova_quantidade)
            except ValueError:
                print("ID, Preço e Quantidade devem ser números válidos.")
            
        elif opcao == "5":
            try:
                id_deletar = int(input("Digite o ID do produto para deletar: "))
                deletar_produto(conn, id_deletar)
            except ValueError:
                print("O ID deve ser um número inteiro.")
        
        elif opcao == "6":
            print("Saindo do programa. Até logo!")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    conn.close()

if __name__ == '__main__':
    main()