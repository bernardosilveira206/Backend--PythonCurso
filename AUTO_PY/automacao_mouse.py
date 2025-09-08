import pyautogui
import time

print (pyautogui.position()) # ver aonde a setinha do mouse esta em plano cartesiano X / Y

print (pyautogui.size()) #ver a resolução da tela

#funções de mouse
#time.sleep(5) # da um tempo de 5 segundos para clicar
#pyautogui.click(x=416 , y=879, button="left") #ele vai clicar automaticamente(X e Y e a posição que ele vai clicar)e pode escolher o botão
#pyautogui.click(x=417, y=866, clicks=2)

#time.sleep(3)
#pyautogui.click(x=403, y=439, clicks=2)
#time.sleep(2)
#pyautogui.click(x=531, y=150, clicks=2)
time.sleep(2)
pyautogui.moveTo(x=299, y=229, duration=2)
pyautogui.moveTo(x=303, y=461,duration=2)
pyautogui.click(x=303, y=461,duration=2)
pyautogui.click(x=560, y=333,duration=2)

pyautogui.scroll(-1300)

