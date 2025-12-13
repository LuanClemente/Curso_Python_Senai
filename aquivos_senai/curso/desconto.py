status_vip = input("Você é cliente VIP? (sim/não): ").lower()

while True:
    try:
        valor_compra = float(input("Qual é o valor da sua compra (em R$)? "))
        if valor_compra >= 0:
            break
        else:
            print("O valor da compra deve ser um número positivo.")
    except ValueError:
        print("Valor de compra inválido. Por favor, insira um número.")

percentual_desconto = 0.0
mensagem_desconto = "\nNão há desconto aplicável."

if status_vip == "sim":
    percentual_desconto = 0.15
    mensagem_desconto = "\nParabéns! Você é um cliente VIP e ganhou 15% de desconto!"

elif status_vip == "não":
    if valor_compra > 200.00:
        percentual_desconto = 0.15
        mensagem_desconto = "\nSua compra é superior a R$ 200,00. Você ganhou 15% de desconto!"
    elif valor_compra >= 100.00:
        percentual_desconto = 0.05
        mensagem_desconto = "\nSua compra está entre R$ 100,00 e R$ 200,00. Você ganhou 5% de desconto."
    
else:
    mensagem_desconto = "\nResposta inválida para o status VIP. Nenhum desconto será aplicado."

print(mensagem_desconto)

desconto_aplicado = valor_compra * percentual_desconto
valor_final = valor_compra - desconto_aplicado

print(f"\nDetalhes da Compra:")
print(f"Valor Original: R$ {valor_compra:.2f}")
print(f"Desconto ({percentual_desconto * 100:.0f}%): -R$ {desconto_aplicado:.2f}")
print(f"**Valor Final a Pagar: R$ {valor_final:.2f}**")