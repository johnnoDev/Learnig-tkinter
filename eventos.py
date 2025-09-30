'''
Eventos y Callbacks en Tkinter
'''
import tkinter as tk

window = tk.Tk()
window.geometry("600x600")

def on_click(event):
    print("Boton presionado")

button = tk.Button(window, text="Haz clic aqui")
button.pack()

button.bind("<Button-3>", on_click) # Se asocia con el evento
# El evento button 1 que es apretar el boton izquierdo del mouse
# El evento button 2 que es apretar el boton en medio del mouse (la rueda)
# El evento button 3 que es apretar el boton derecho del mouse

def on_key_press(event):
    if event.char == "a":
        print("Tecla 'a' presionada.")

window.bind("<KeyPress>", on_key_press)

 # Eventos de redimensionar pantalla
# def on_resize(event):
#     print(f'La ventana ha sido redimensionada, {event.width} {event.height}')

# window.bind("<Configure>", on_resize)

# Evento para cuando mueva el mouse nos indique las coordenadas de x y y

# def on_mouse_move(event):
#     print(f"Raton movido a {event.x} {event.y}")

# window.bind("<Motion>", on_mouse_move)















window.mainloop()