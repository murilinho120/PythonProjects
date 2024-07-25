import os

# Dicionário global para armazenar usuários
usuarios = {}

# Defina o caminho do diretório e do arquivo
diretorio = r"C:\Users\Administrator\PycharmProjects\pythonProject\ghub\arquivos\bigdata"
arquivo_nome = "bd.txt"

# Cria o diretório se não existir
os.makedirs(diretorio, exist_ok=True)

def main():
    os.system('cls')
    print("O que deseja realizar???\n\n1 - INSERIR USUÁRIO\n2 - PESQUISAR UM USUÁRIO\n3 - EXCLUIR UM USUÁRIO:")
    op1()

def op1():
    try:
        opcao = int(input("\n\nQual: "))
        os.system('cls')
        if opcao == 1:
            login = input("Digite o login: ").upper()
            nome = input('Digite o seu nome: ')
            dt_acesso = input("Qual foi sua última data de acesso: ")
            usuarios[login] = {'nome': nome, 'dt_acesso': dt_acesso}
            salvar()
            print(f"Usuário {login} inserido com sucesso!")
            input('Digite uma tecla para voltar ao menu principal')
            main()
        else:
            print('Opção inválida')
            input('Digite uma tecla para voltar ao menu principal')
            main()
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')
        input('Digite uma tecla para voltar ao menu principal')
        main()

def salvar():
    caminho_arquivo = os.path.join(diretorio, arquivo_nome)
    #print(f"Salvando no caminho: {caminho_arquivo}")  # Adicione esta linha para depuração
    with open(caminho_arquivo, "a") as arquivo:
        for login, dados in usuarios.items():
            # Linha formatada corretamente
            linha = f"{login},{dados['nome']},{dados['dt_acesso']}\n"
            arquivo.write(linha)

if __name__ == '__main__':
    main()
