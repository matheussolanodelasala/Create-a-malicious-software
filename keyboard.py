import keyboard

def grabar(evento):
    archivo = open("log.txt", "a")
    archivo.write(evento.name + " ") # .name es el nombre de la tecla (ej: 'a', 'space')
    archivo.close()

print("Grabando... Presiona ESC para salir.")

keyboard.on_release(callback=grabar)

keyboard.wait('esc')
