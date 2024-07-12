import os

procurapeca = []

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolher_opcoes()
    

def invalido():
    os.system('cls')
    print('Opção inválida')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def errado():
    os.system('cls')
    print("\nEscolha uma opção de 1 à 4, por favor")

def compra():
    os.system('cls')
    peça = input("Qual peça você procurando: ")
    procurapeca.append(peça)
    print(f"\nIremos procurar {peça} para você, lhe retornaremos em breve!!!\n")
    input('Aperte enter para continuar')
    main()

def espera():
    os.system('cls')
    for peca in procurapeca:
        print(f'.{peca}')
    input('Aperte enter para continuar')
    main()

def escolher_opcoes(): 
    print('OLÁ, SOMOS A RVC AUTO PEÇAS\n')
    #trasformar em button mais para frente
    print('1 - COMPRA')
    print('2 - DEVOLUÇÕES')
    print('3 - MERCADO LIVRE')
    print('4 - PEÇAS A ESPERA\n')

    try:
        mtv = int(input('Qual o motivo do seu contato: '))
        if mtv == 1:
            os.system('cls')
            print('\nVocê escolheu a opção compra')
            input('\nAperte enter para continuar')
            compra()
        elif mtv == 2:
            print('\nVocê escolheu a opção devolução')
        elif mtv == 3:
            print('\nVocê escolheu a opção mercado livre')
        elif mtv == 4:
            os.system('cls')
            print("\nVocê escolheu a opção PEÇAS A ESPERA")
            input("Aperte ENTER para continuar")
            espera()
        else:
            errado()
    except ValueError:
        invalido()

if __name__ == '__main__':
    main()