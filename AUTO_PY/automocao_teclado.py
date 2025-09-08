import pyautogui
import time



#funções do teclado
time.sleep(2)

pyautogui.click(x=423, y=171, duration=1)
pyautogui.write("AOC", interval=0.2) #digitar no site AOC com pesquisa
time.sleep(0.5) # espera 5 segundos para garantir que a janela/site esteja carregado
pyautogui.hotkey("ctrl","a")
time.sleep(0.2)
pyautogui.hotkey("ctrl","c") #apertar duas teclas juntas
time.sleep(0.2)
pyautogui.press("enter") #pressionar enter
