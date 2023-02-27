#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@autora: TaisTeixeira
import os
from ast import Pass
from sys import displayhook
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
import time
import urllib
from easygui import *
import win32gui
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows
from pathlib import Path
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType



#lendo a planilha
contatos_df = pd.read_excel("Enviar.xlsx", engine="openpyxl")
total = len(contatos_df.index)

#caixa de mensagem inicio
try:
    message = " Planilha contem total de {} pessoas.\n \n O Boot envia cada mensagem de 9 em 9 segundos por motivos de seguranca do WPP. \n \n Clique em OK para continuar.".format(total)
    title = "Inicializando"
    output = msgbox(message, title) 
    print("User pressed  : " + output)
except (ValueError, TypeError, NameError, RuntimeError):
    pass  

agentes = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		];

agente = agentes[random.randint(0, len(agentes) - 1)]

chrome_options = Options()
#chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3") 
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("user-agent=" + agente)
chrome_options.add_argument("user-data-dir=/path/to/your/custom/profile/")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-offline-load-stale-cache')
chrome_options.add_argument('--disk-cache-size=0')

#abrir navegador 
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
wpp = 'https://web.whatsapp.com/'
navegador.get(wpp)


#Escondendo cmd do webdriver
def enumWindowFunc(hwnd, windowList):
    """ win32gui.EnumWindows() callback """
    text = win32gui.GetWindowText(hwnd)
    className = win32gui.GetClassName(hwnd)
    if 'chromedriver' in text.lower() or 'chromedriver' in className.lower():
        win32gui.ShowWindow(hwnd, False)
win32gui.EnumWindows(enumWindowFunc, [])

try:
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(random.uniform(1, 5))

except (NoSuchWindowException, NoSuchElementException):
    print("Algo de Errado Aconteceu. Feche Tudo e Abra Novamente.")
    try:
        message = "Você Fechou o Navegador e Não Foi Possivel Terminar a Execução"
        title = "Erro"
        output = msgbox(message, title) 
        print("User pressed  : " + output)
        sys.exit()   
    except (ValueError, TypeError, NameError, RuntimeError):
        sys.exit()


def roadr(texto):
    global contatos_df
    # já estamos com o login feito no whatsapp web
    try:            
        for i, pessoa in enumerate(contatos_df['Pessoa']):
            pessoa = contatos_df.loc[i, "Pessoa"]
            numero = contatos_df.loc[i, "Número"]
    
            #contrato = contatos_df.loc[i, "Contrato"]
            #texto = urllib.parse.quote(f"Olá! {pessoa} \n \n {mensagem}")
            #link = f"https://web.whatsapp.com/send?phone=55{numero}&text={texto}"
            link2 = f"https://web.whatsapp.com/send?phone=55{numero}"
            time.sleep(random.uniform(6, 9))
            

            while len(navegador.find_elements(By.ID, "side")) < 1:
                time.sleep(random.uniform(3, 9))
           
            
            try:
                navegador.get(link2)
                time.sleep(random.uniform(7, 9))
                mensagem = str(texto)
                linhas = mensagem.split('\n')
                variaveis = []
                for linha in linhas:
                    linha_sem_espaco = linha.strip()
                    variaveis.append(linha_sem_espaco)

                campo_texto = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
                primeiro = f"Olá {pessoa}"
                for letra in primeiro:
                    campo_texto.send_keys(letra)
                campo_texto.send_keys(Keys.SHIFT + Keys.ENTER)

                
                for variavel in variaveis:
                    for letra in variavel:
                        campo_texto.send_keys(letra)
                    campo_texto.send_keys(Keys.SHIFT + Keys.ENTER)
                time.sleep(random.uniform(2, 3))
                navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)

            except:
                navegador.get(link2)
                try:
                    for letra in mensagem:
                        campo_texto.send_keys(letra)
                        time.sleep(0.4)
                    time.sleep(random.uniform(2, 3))
                    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
                except:
                    pass
                            
                     
            time.sleep(2)
        # Selecione todas as linhas depois da primeira
        linhas_para_remover = contatos_df.iloc[0:]
        # Remova as linhas selecionadas
        contatos_df.drop(linhas_para_remover.index, inplace=True)
        contatos_df.to_excel('Enviar.xlsx', index=False)
    except (NoSuchWindowException, NoSuchElementException):
        print("Algo de Errado Aconteceu. Feche Tudo e Abra Novamente.")
        try:
            message = "Você Fechou o Navegador e Não Foi Possivel Terminar a Execução"
            title = "Erro"
            output = msgbox(message, title) 
            print("User pressed  : " + output)
            sys.exit()   
        except (ValueError, TypeError, NameError, RuntimeError):
            sys.exit()
        
    
    #caixa de mensagem
    try:
        message = "Mensagens enviadas com sucesso."
        title = "FINALIZADO"
        output = msgbox(message, title) 
        print("User pressed  : " + output)
        navegador.quit()
    except (ValueError, TypeError, NameError, RuntimeError):
        sys.exit()



#roadr()


    




