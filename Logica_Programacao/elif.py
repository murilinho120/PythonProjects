#o que é elif

pontos = float(input("quantos pontos você fez: "))

if pontos < 200:
    print("Você fez o minímo")
elif pontos < 400:
    print("você ganhou 4gb de internet")
elif pontos < 600:
    print("você ganhou 6gb de internet")
elif pontos < 800:
    print("você ganhou 8gb de internet")
elif pontos >= 800:
    print("você ganhou 11111gb de internet")