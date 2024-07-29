#para navegar até um site (web driver é o navegador)
from selenium import webdriver
#By para selecionar campos
from selenium.webdriver.common.by import By
#pausar entre ações para site não bloquear ou travar automação
from time import sleep
import openpyxl
import os

driver = webdriver.Chrome()
#para navegar até o site https://contabilidade-devaprender.netlify.app/
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5) #pausa de 5 seg para garantir que site carregue



#Digitar email e senha
#usar xpath   ||||  tag[@atributo='valor']    |||||| (encontrar um campo único inspecionando o site)
#            EX:    input[@id='email']|
email = driver.find_element(By.XPATH,"//input[@id='email']")
sleep(2)
email.send_keys('admin@contabilidade.com')

#agora senha
senha = driver.find_element(By.XPATH,"//input[@id='senha']")
sleep(2)
senha.send_keys('minhanovasenha1234'
                )
#clicar em entrar
entrar = driver.find_element(By.XPATH,"//button[@id='Entrar']")
sleep(2)
entrar.click()
sleep(4)


#LOGIN CONCLÚIDO




#extrair informação planilha
empresas = openpyxl.load_workbook('./empresas.xlsx')
pagina1 = empresas['dados empresas']
#iter rows para passar por cada linha e min row para a partir da linha 2
for linha in pagina1.iter_rows(min_row=2,values_only=True):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, qnt_funcionario, data_fundacao = linha


#Modo de fazer mais rápido inspecionar, e se for tudo igual
    driver.find_element(By.ID,'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)

    driver.find_element(By.ID,'emailEmpresa').send_keys(email)
    sleep(1)

    driver.find_element(By.ID,'telefoneEmpresa').send_keys(telefone)
    sleep(1)

    driver.find_element(By.ID,'enderecoEmpresa').send_keys(endereco)
    sleep(1)

    driver.find_element(By.ID,'cnpj').send_keys(cnpj)
    sleep(1)

    driver.find_element(By.ID,'areaAtuacao').send_keys(area_atuacao)
    sleep(1)

    driver.find_element(By.ID,'numeroFuncionarios').send_keys(qnt_funcionario)
    sleep(1)

    driver.find_element(By.ID,'dataFundacao').send_keys(data_fundacao)
    sleep(1)

    #pode não funcionar
    driver.find_element(By.ID,'Cadastrar').click()
    sleep(3)



input("pressione enter para encerrar")