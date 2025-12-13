lista_de_emails = ["ana@email.com", "bruno.costa@email.com", "carla123@email.com"]
# Para cada 'email' na 'lista_de_emails'...
for email in lista_de_emails:
# ...crie uma mensagem personalizada e simule o envio.
    nome_usuario = email.split('@')[0] # Pega a parte do e-mail antes do @
    mensagem = f"Olá {nome_usuario}, obrigado por se inscrever em nossa newsletter!"
# Aqui iria o código real para enviar o e-mail
    print(f"Enviando para {email}: '{mensagem}'")
print("-" * 30)
print("Todos os e-mails foram enviados com sucesso!")