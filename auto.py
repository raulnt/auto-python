# pip install pyautogui
import pyautogui
import time

# Comandos mais usados:
# pyautogui.click => clicar
# pyautogui.press => pressiona tecla
# pyautogui.write => escrever

# ------ PASSO A PASSO ------

# 1- Abrir o sistema
# SISTEMA: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win")
time.sleep(2)

pyautogui.write("edge")
time.sleep(2)

pyautogui.press("enter")
time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(2)

pyautogui.press("enter")
time.sleep(2)

# 2- Logar no sistema
pyautogui.click(x=759, y=387)
time.sleep(3)

pyautogui.write("raul@email.com")
time.sleep(2)

pyautogui.press("tab")
time.sleep(2)

pyautogui.write("123456")
time.sleep(2)

pyautogui.press("tab")
time.sleep(2)

pyautogui.press("enter")
time.sleep(2)

# 3- Importar os dados
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("C:/Users/Raul/Desktop/MeuAutoPython/auto-python/produtos.csv")

print(tabela)

time.sleep(2)
# 4- Registrar um produto
for linha in tabela.index:
    pyautogui.click(x=840, y=283)
    time.sleep(2)

    # Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    time.sleep(1)

    pyautogui.press("tab")
    time.sleep(1)

    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    time.sleep(1)

    pyautogui.press("tab")
    time.sleep(1)

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))

    pyautogui.press("tab")
    time.sleep(1)

    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    time.sleep(1)

    pyautogui.press("tab")
    time.sleep(1)

    # Preco
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    time.sleep(1)

    pyautogui.press("tab")
    time.sleep(1)

    # Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    time.sleep(1)

    pyautogui.press("tab")
    time.sleep(1)

    # Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        time.sleep(1)

    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.press("pg up")
    time.sleep(2)

# 5- Registrar todos os produtos