import pyautogui
import pyperclip
import time
from datetime import datetime, timedelta

# === CONFIGURAÇÕES ===
FORMATO_DATA = "%d/%m/%Y"  # Ex: 26/01/2026
categoria = "Atividades Técnico Operacionais"
categoria2 = "Atividades Administrativas"
departamento = "CQ-DNRI - Núcleo Regional Londrina"
NOVO_DIA = (1732, 208)
DATA_INICIAL = datetime(2026, 1, 7)
QUANTIDADE = range(0, 3)


def escrever(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.4)


def preencher(dia):
    data_str = dia.strftime(FORMATO_DATA)
    if data_str == '10/12/2025':
        return
    pyautogui.click(x=NOVO_DIA[0], y=NOVO_DIA[1])
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(0.5)
    escrever(categoria)
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(0.5)
    escrever(departamento)
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    escrever(data_str)
    time.sleep(0.5)
    pyautogui.press('tab')
    escrever("12:00")
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    escrever(data_str)
    pyautogui.press('tab')
    time.sleep(0.5)
    escrever("19:00")
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')


# === LOOP PARA MÚLTIPLOS REGISTROS ===
print("Iniciando automação em 5 segundos... Posicione o cursor no PRIMEIRO campo!")
time.sleep(5)

for i in QUANTIDADE:
    data_atual = DATA_INICIAL + timedelta(days=i)  # Incrementa 1 dia por registro
    preencher(data_atual)
    time.sleep(1)  # Pausa para o sistema processar e abrir o próximo formulário

print("Automação concluída!")

