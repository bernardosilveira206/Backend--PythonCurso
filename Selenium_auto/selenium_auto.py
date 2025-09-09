#comando para instalar o selenium | py -m pip install selenium
import selenium
from selenium import webdriver
import time
# Abrir o navegador 
navegador = webdriver.Chrome()

navegador.maximize_window() #maximizar a tela do site

navegador.get("https://www.python.org/")  #abrir um site

botao_donate = navegador.find_element("class name", "donate-button")#selecionar um elemento no site

botao_donate.click() #clicar em um elemento

time.sleep(7)