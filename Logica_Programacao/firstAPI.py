import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    escolher_opcoes()

def invalido():
    os.system('cls')
    print('opção inválida')
    input('digite uma tecla para voltar ao menu principal')
    main()
def errado():
    os.system('cls')
    print("\nescolha uma opção de 1 à 4")


def escolher_opcoes():
    try:
        print('olá, SOMOS A RVC AUTO PEÇAS')
        #trasformar em button mais para frente
        print('1 - COMPRA')
        print('2 - DEVOLUÇÕES')
        print('3 - MERCADO LIVRE')
        print('4 - MOTORES E CÂMBIOS\n')
        mtv = int(input('qual o motivo do seu contato: '))

        if mtv == 1:
            print('\nvocê escolheu a opção compra')
        elif mtv == 2:
            print('\nvocê escolheu a opção devolução')
        elif mtv == 3:
            print('\nvocê escolheu a opção mercado livre')
        elif mtv == 4:
            print("\nVocê escolheu a opção motores e câmbios")
        else:
          errado()
    except:
        invalido()

if __name__ == '__main__':
    main()