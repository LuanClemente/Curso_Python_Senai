import random
numero_secreto = random.randint(1, 200)
palpite = 0
print("Jogo de Adivinhação! Tente adivinhar o número entre 1 e 200.")
# Enquanto o 'palpite' do usuário for diferente do 'numero_secreto'...
while palpite != numero_secreto:
# ...peça um novo palpite.
    try:
        palpite = int(input("Qual o seu palpite? "))

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")
        
print("=" * 30)
print(f"Parabéns! Você acertou! O número secreto era {numero_secreto}.")