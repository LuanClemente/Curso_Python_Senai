# Este é o nosso kit de ferramentas para trabalhar com textos.
# Cada função aqui é uma "peça" reutilizável.

def contar_palavras(texto: str) -> int:
    """Função global que conta o número de palavras em um texto."""
    palavras = texto.split()
    return len(palavras)

def remover_pontuacao(texto: str) -> str:
    """Função global que remove pontuações comuns de um texto."""
    pontuacoes = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    texto_sem_pontuacao = ""
    for char in texto:
        if char not in pontuacoes:
            texto_sem_pontuacao += char
    return texto_sem_pontuacao

def encontrar_palavra_mais_comum(texto: str) -> str:
    """Função global que encontra a palavra mais frequente em um texto."""
    texto_limpo = remover_pontuacao(texto.lower())
    palavras = texto_limpo.split()
    
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    
    if not contagem:
        return ""
        
    palavra_comum = max(contagem, key=contagem.get)
    return palavra_comum

# --- Note que este arquivo NÃO FAZ NADA se você o executar.
# --- Ele apenas DEFINE as ferramentas. Ele é uma biblioteca.

