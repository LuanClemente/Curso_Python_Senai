usuarios_cadastrados = ["ana", "carlos", "beatriz", "daniel", "elaine"]
novo_usuario = input(f"Digite um usuário: ")
usuario_existe = False
print(f"Verificando se o usuário '{novo_usuario}' já existe...")
for usuario in usuarios_cadastrados:
    print(f"Comparando com '{usuario}'...")
    if usuario == novo_usuario:
        print("Usuário encontrado!")
        usuario_existe = True
        break # Sai do laço, pois não há necessidade de continuar a busca
if usuario_existe:
    print(f"O nome de usuário '{novo_usuario}' já está em uso.")
else:
        print(f"O nome de usuário '{novo_usuario}' está disponível.")