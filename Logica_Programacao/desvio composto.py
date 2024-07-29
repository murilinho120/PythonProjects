#pedir nome
nome = input("qual seu nome: ")
#pedir nota
nota = float(input("qual foi sua nota"))
#pedir idade
idade = int(input("qual sua idade: "))

#verificar se é maior de idade
if idade >= 18:
    print("o aluno é maior de idade")
    if nota >= 6:
        print(f"passou de ano, sua nota final é de {nota}")

    else:
        print(f"aluno reprovou de ano, sua nota final é de {nota}")
else:
    print(f"você é menor de idade")