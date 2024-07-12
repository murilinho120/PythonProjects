import csv

# Caminho para o arquivo CSV (ajuste conforme o seu ambiente)
arquivo_csv = 'us-counties.csv'

# Função para contar as linhas referentes ao dia 27 de setembro de 2021
def contar_linhas_27_set_2021(arquivo):
    contador = 0
    with open(arquivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pula o cabeçalho
        for linha in reader:
            data = linha[0]  # A data está na primeira coluna (índice 0)
            if data == '2021-09-27':
                contador += 1
    return contador

# Chamada da função para contar as linhas
quantidade_linhas = contar_linhas_27_set_2021(arquivo_csv)

# Imprime a quantidade de linhas encontradas
print(quantidade_linhas)
