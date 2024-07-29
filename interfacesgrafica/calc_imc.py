import PySimpleGUI as sg

# Tema/cores da API visual
sg.theme('reddit')

# Criando layout
firstlayout = [
    [sg.Text('Peso:'), sg.Input(key='peso')],
    [sg.Text('Altura:'), sg.Input(key='alt')],
    [sg.Button('Calcular IMC')],
    [sg.Text('', key='resultado')]
]

# Função para calcular o IMC
def calc_imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura)
        resultado_imc = peso / (altura ** 2)
        if resultado_imc < 18.5:
            return f"IMC: {resultado_imc:.2f} - Muito Magro"
        elif 18.5 <= resultado_imc < 24.9:
            return f"IMC: {resultado_imc:.2f} - Peso Normal"
        elif 25 <= resultado_imc < 29.9:
            return f"IMC: {resultado_imc:.2f} - Sobrepeso"
        else:
            return f"IMC: {resultado_imc:.2f} - Obesidade"
    except ValueError:
        return "Por favor, insira valores numéricos válidos."

# Criar a janela
janela = sg.Window('Calculadora de IMC', layout=firstlayout)

# Loop de eventos
while True:
    event, values = janela.read()
    
    # Fechar a janela
    if event == sg.WIN_CLOSED:
        break
    
    # Se o botão 'Calcular IMC' for pressionado
    if event == 'Calcular IMC':
        peso = values['peso']
        altura = values['alt']
        imc = calc_imc(peso, altura)
        janela['resultado'].update(imc)  # Atualizar o campo de resultado

# Fechar a janela
janela.close()

#agora preciso aprender a formatar