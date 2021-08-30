# entrar no sistema
# navegar no sistema
# baixar arquivo de vendas
# calcular o faturamento
# enviar email para diretoria


import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 2

# download do arquivo

link = "https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyautogui.write(link)
pyautogui.press("enter")
'''time.sleep(5)
    pyautogui.position()'''
time.sleep(3)
pyautogui.click(x=-1523, y=121)  # sel
pyautogui.click(x=-205, y=25)  # op
pyautogui.click(x=-441, y=466)  # down
time.sleep(5)

# analise dados tabela

data_vendas = pd.read_excel(r"D:\downloads\Vendas - Dez.xlsx")
faturamento = data_vendas["Valor Final"].sum()
quant = data_vendas["Quantidade"].sum()

print(f'''\n
      --Faturamento: R${faturamento}\n
      --Quantidade vendida: {quant} peças''')

# enviar email

link_email = "https://mail.google.com/mail/u/0/#inbox"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyautogui.write(link_email)
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=-1827, y=40)
pyautogui.click(x=-590, y=338)
pyautogui.write("emailxxx@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
assunto = "Teste 1"
# pyautogui.write(assunto)
pyautogui.press("tab")


# corpo email
texto = f"""
Prezados, bom dia

O faturamento foi de R${faturamento:,.2f}
A quantidade de produtos foi de {quant:,}

Abs
allets"""

pyautogui.write(texto)


# enviar
pyautogui.hotkey("ctrl", "enter")
