#  Passo 1 entrar no sistema da empresa
    # # https://dlp.hashtagtreinamentos.com/python/intensivao/login   
# 
# Automatização de processo de cadastro  de
# produtos em um sistema extraindo as informações
 
#  biblitecas em Python    
import pyautogui
import time

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# acessar o site
pyautogui.write(link)
pyautogui.press('enter') 

# aguarde 5 segundos
time.sleep(2.3)
#   Passo 2 - fazer login
pyautogui.click(x=568, y=380)

pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab')

pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3.0)
#   Passo 3 - importar base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)


for linha in tabela.index:
    #   Passo 4 - cadastrar 1 produto
    pyautogui.click(x=607, y=252)
    # codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    # marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    # tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    # categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    # custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    # obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs): # se a variavel é nan escre
        pyautogui.write(obs)
    # enviar produto 
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.hotkey('fn', 'home')
#   Passo 5 - repetir isso até acabar a base de dados
