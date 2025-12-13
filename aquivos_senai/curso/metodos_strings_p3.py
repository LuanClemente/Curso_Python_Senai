# metodos em strings

def main():

    texto = "Ola, Mundo!, ola"
    
    print(texto)
    print(texto.upper()) # todos maisculos
    print(texto.lower()) # todos minusculos
    print(texto.capitalize())  # 1ª letra em maisculo 
    print(texto.title())       # 1ª letra de cada palavra em maisculo
    print(texto.find("Mundo")) # retornar o indice da palavra
    print(texto.count("o"))    # quantidade de strings ou caracteres tem dentro da frase
    print(texto.split(","))    #

    palavras = ["ola", "mundo", "ola"]
    frase = "-".join(palavras) # join - junta as palavras
    print(frase)



if __name__ == "__main__":
    main()