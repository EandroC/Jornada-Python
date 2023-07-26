import pyautogui
import time
import pandas as pd

#definido o tempo de espera de cada instrução do pyautogui
pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

#entrando no link
#os clicks precisão ser ajustados de acordo com a tela do usuario
pyautogui.click(x=664, y=51)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")    
#espera de carregamento
time.sleep(5)


#pyautogui.click(x=689, y=394)
pyautogui.press("tab")
pyautogui.write("seuemail@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaescolhida")

#pyautogui.click(x=683, y=563)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:

    pyautogui.click(x=643, y=280)       
    
    #pyautogui.press("tab")

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    #dando scroll para o inicio da tela scroll ou usando press "pgup"
    #pyautogui.scroll(5000)
    pyautogui.press("pgup")

