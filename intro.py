import tkinter as tk

window = tk.Tk() # Llamar a la clase de Tkinter

window.title("Mi primer interfaz") # Cambiar el titulo de la ventana
window.geometry("600x600") # Cambia el tamaño de la ventana

window.minsize(400, 200) # Asigna el tamanio minimo de la ventana
window.maxsize(800, 200) # Asigna el tamanio maximo de la ventana

window.iconbitmap("python.ico") # Cambia el icono del programa (se encuentra en el lado izquierdo)

window.configure(bg="SlateBlue1") # Asigna un color al fondo de la ventana

window.resizable(False, False) # Bloquea que se estire la ventana

# window.attributes("-alpha", 0.8) # Asigna transparecia a la ventana


window.mainloop() # Bucle principal de Tiknter: Mantiene la ventana visible