#cadastrar nota
#exibir notas 
#calcular média
#sair
import os

notas = []

opcao = -1

while opcao != 4:
    os.system('cls')

    def cadastro():
        os.system('cls')
        print("vc escolheu a opçao cadastro de notas")
        nota = float(input("digite a nota que quer cadastrar? "))
        if nota > 10:
            os.system('cls')
            input(print('nota invalida \naperte enter para continuar'))
            cadastro()
        else:
            notas.append(nota)
            input(print('Nota cadastrada \nAperte o enter para continuar: '))


    def exibir():
        os.system('cls')
        print(f"vc escolheu a opção EXIBIR {notas}")
        input(print('Aperte o enter para continuar: '))




    def calc():
        os.system('cls')
        print("vc escolheu a opçao calc")
        soma = 0
        for nota in notas:
            soma = soma + nota
        media =  soma / len(notas)
        print(f"Sua média foi de {media} ")
        input(print(f'Aperte o enter para continuar:'))
#poderia só usar media = sum(nota) / len(notas)


    def sair():
        os.system('cls')
        print("voce saiu")


    print("1 - CADASTRAR NOTA \n2 - EXIBIR NOTA \n3 - CALCULAR NOTA \n4 - SAIR")
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        cadastro()

    elif opcao == 2:
        exibir()

    elif opcao == 3:
        calc()

    elif opcao == 4:
        sair()

    else:
        os.system('cls')
        input(print("opçao invalida, digite enter para continuar: "))