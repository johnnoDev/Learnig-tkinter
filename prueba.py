import tkinter as tk
from tkinter import messagebox

def obtener_valores():
    """Intenta convertir los valores a float. Retorna None si hay error."""
    try:
        num1 = float(entrada1.get().strip())
        num2 = float(entrada2.get().strip())
        return num1, num2
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo valores numéricos.")
        return None

def sumar():
    valores = obtener_valores()
    if valores:
        num1, num2 = valores
        resultado.config(text=f"Resultado: {num1 + num2}")

def restar():
    valores = obtener_valores()
    if valores:
        num1, num2 = valores
        resultado.config(text=f"Resultado: {num1 - num2}")

def multiplicar():
    valores = obtener_valores()
    if valores:
        num1, num2 = valores
        resultado.config(text=f"Resultado: {num1 * num2}")

def dividir():
    valores = obtener_valores()
    if valores:
        num1, num2 = valores
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
        else:
            resultado.config(text=f"Resultado: {num1 / num2}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Etiquetas y campos de entrada
tk.Label(ventana, text="Ingrese el primer número:").pack(pady=5)
entrada1 = tk.Entry(ventana, width=20)
entrada1.pack()

tk.Label(ventana, text="Ingrese el segundo número:").pack(pady=5)
entrada2 = tk.Entry(ventana, width=20)
entrada2.pack()

# Botones de operaciones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_suma = tk.Button(frame_botones, text="+", width=5, command=sumar)
btn_suma.grid(row=0, column=0, padx=5)

btn_resta = tk.Button(frame_botones, text="-", width=5, command=restar)
btn_resta.grid(row=0, column=1, padx=5)

btn_multi = tk.Button(frame_botones, text="×", width=5, command=multiplicar)
btn_multi.grid(row=0, column=2, padx=5)

btn_div = tk.Button(frame_botones, text="÷", width=5, command=dividir)
btn_div.grid(row=0, column=3, padx=5)

# Etiqueta de resultado
resultado = tk.Label(ventana, text="Resultado: ", width=40, height=2, relief="solid")
resultado.pack(pady=20)

ventana.mainloop()