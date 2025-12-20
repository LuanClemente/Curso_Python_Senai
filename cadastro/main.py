from funcoes_estoque import *

def main():
    # Inicializa conexão e tabela
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