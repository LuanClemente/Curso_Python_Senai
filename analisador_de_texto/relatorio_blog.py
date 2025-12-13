# 1. Importando as "peças de LEGO" (ferramentas) que precisamos.
from analisador_texto import contar_palavras, encontrar_palavra_mais_comum

def main():
    
    # Esta é a função principal. Ela orquestra o trabalho.
    # É o "manual de instruções" que diz qual ferramenta usar e quando.
    
    print("--- Gerador de Relatório de Análise de Blog ---")

    post_blog = """
    Python é uma linguagem de programação incrivelmente versátil e poderosa. 
    Aprender Python abre portas para áreas como desenvolvimento web, ciência de dados e automação.
    A simplicidade da sintaxe de Python é um grande atrativo para iniciantes. 
    """

    # 2. Usando as ferramentas importadas para executar o plano.
    total_palavras = contar_palavras(post_blog)
    palavra_chave = encontrar_palavra_mais_comum(post_blog)

    # 3. Montando o resultado final do nosso projeto.
    print(f"\nAnálise do Post:")
    print(f"O post contém {total_palavras} palavras.")
    print(f"A palavra-chave mais frequente (potencial) é: '{palavra_chave}'.")
    print("\n--- Fim do Relatório ---")


# 4. O "Botão de Ligar" do nosso projeto.
# Este código só roda quando executamos "python relatorio_blog.py".
# Ele não rodará se outro script importar 'relatorio_blog'.
if __name__ == "__main__":
    main()

