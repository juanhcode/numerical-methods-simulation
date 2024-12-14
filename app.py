import tkinter as tk
from metodos import *

# Crear la ventana principal
root = tk.Tk()
root.title("Simulación y Computación Numérica")
root.geometry("600x500")
root.config(bg="#F3F4F6")  # Fondo claro para mejor contraste

# Título principal
title_label = tk.Label(
    root, 
    text="Simulación y Computación Numérica", 
    font=("Helvetica", 20, "bold"), 
    bg="#2C3E50", 
    fg="#ECF0F1", 
    pady=20
)
title_label.pack(fill="x")

# Frame para organizar los botones
frame = tk.Frame(root, bg="#F3F4F6")
frame.pack(expand=True, pady=20)

# Botones estilizados con dimensiones cuadradas
button_style = {
    "font": ("Helvetica", 14),
    "bg": "#1ABC9C",
    "fg": "black",
    "activebackground": "#16A085",
    "activeforeground": "black",
    "relief": "flat",
    "width": 15,  # Anchura uniforme
    "height": 2   # Altura uniforme para lograr un diseño cuadrado
}

# Crear los botones en una sola columna
tk.Button(frame, text="Series de Taylor", command=lambda: cambiar_vista("taylor"), **button_style).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame, text="Método de Newton", command=lambda: cambiar_vista("newton"), **button_style).grid(row=1, column=0, padx=10, pady=10)
tk.Button(frame, text="Diferencias Finitas", command=lambda: cambiar_vista("diferencias_finitas"), **button_style).grid(row=2, column=0, padx=10, pady=10)
tk.Button(frame, text="Ecuaciones No Lineales", command=lambda: cambiar_vista("no_lineales"), **button_style).grid(row=3, column=0, padx=10, pady=10)
tk.Button(frame, text="Ecuaciones Lineales", command=lambda: cambiar_vista("lineales"), **button_style).grid(row=4, column=0, padx=10, pady=10)
tk.Button(frame, text="Ecuaciones Parciales", command=lambda: cambiar_vista("parciales"), **button_style).grid(row=5, column=0, padx=10, pady=10)


# app.py
def cambiar_vista(vista):
    # Limpiar el contenido de la ventana principal
    for widget in frame.winfo_children():
        widget.destroy()

    # Dependiendo de la vista seleccionada, cargar el contenido correspondiente
    if vista == "taylor":
        series_de_taylor(frame)  # Pasar 'frame' como argumento
    elif vista == "newton":
        newton(frame)



# Iniciar la aplicación
root.mainloop()