import pyautogui
import time

# Função para mover o mouse e clicar em coordenadas específicas
print("voce tem 5 segundos para posicionar o mouse no local desejado...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Posição capturada: ({x}, {y})")
    