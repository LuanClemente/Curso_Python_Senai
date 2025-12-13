def verificar_login(usuario, senha):
    usuarios_validos = {
        "admin": "123",
        "bezerra.da.silva": "samba",
        "zeca.urubu": "321"
    }

    if usuario in usuarios_validos:
        if senha == usuarios_validos[usuario]:
            return "Sucesso login feito! \nSeja bem vindo."
        else:
            return "Senha inválida"
    else:
        return "Este usuário não existe"

username_input = input("Digite o nome de usuário: ")
password_input = input("Digite a senha: ")

resultado = verificar_login(username_input, password_input)

print(f"\nResultado da verificação: {resultado}")
