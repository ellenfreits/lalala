peso = float(input("Digite seu peso em kg: "))
altura = float(input("Coloque sua altura: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9: 
   print("Peso normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")

N = int(input("Digite um número inteiro: "))
for i in range(1, N+1):
    if i % 2 == 0:
        print(f"{i} - par")
    else:
        print(f"{i} - ímpar")