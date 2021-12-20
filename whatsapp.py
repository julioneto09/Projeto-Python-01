import pywhatkit
import pyautogui 
import time

def zap(numero):
    pywhatkit.sendwhatmsg_instantly(numero,"Atenção! Ocorrência detectada")
    time.sleep(10)
    pyautogui.press('enter')