import random

print("🎲 Bem-vindo ao jogo da adivinhação! 🎲")

# Número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        break
    elif chute < numero_secreto:
        print("🔼 O número secreto é maior!")
    else:
        print("🔽 O número secreto é menor!")
