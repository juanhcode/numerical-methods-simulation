# Función para calcular y graficar el método de Newton-Raphson también la tabla y sus iteraciones
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

def method_newton_raphson(x0, n, frame):
    x = sp.symbols('x')
    f = sp.exp(x) - x**2
    df = sp.diff(f, x)
    
    # Generar el gráfico usando matplotlib
    x_vals = np.linspace(x0 - 3, x0 + 3, 400)  # Rango de valores de x
    y_vals_F = np.exp(x_vals) - x_vals**2  # Valores de la función original f(x) = e^x - x^2
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals_F, label="f(x) = e^x - x^2", color='blue')
    ax.set_title(f"Método de Newton-Raphson para f(x) = e^x - x^2 con x0 = {x0}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    
    # Incrustar el gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)  # Crear el canvas de matplotlib
    canvas.draw()  # Dibujar el gráfico
    canvas.get_tk_widget().grid(row=4, column=0, padx=10, pady=10, sticky="n")  # Colocar el gráfico en el frame
    
    # Calcular las iteraciones del método de Newton-Raphson
    x_vals = [x0]
    y_vals = [float(f.subs(x, x0))]
    for i in range(1, n + 1):
        x1 = x_vals[-1] - float(f.subs(x, x_vals[-1])) / float(df.subs(x, x_vals[-1]))
        x_vals.append(x1)
        y_vals.append(float(f.subs(x, x1)))
        
    # Mostrar la tabla de iteraciones
    print("Iteración\t x\t\t f(x)")
    for i in range(len(x_vals)):
        print(f"{i}\t\t {x_vals[i]:.6f}\t {y_vals[i]:.6f}")
        
    # Mostrar las iteraciones en un tablero de Tkinter
    tree = ttk.Treeview(frame, columns=("Iteración", "x", "f(x)"), show='headings')
    tree.heading("Iteración", text="Iteración")
    tree.heading("x", text="x")
    tree.heading("f(x)", text="f(x)")
    
    for i in range(len(x_vals)):
        tree.insert("", "end", values=(i, f"{x_vals[i]:.6f}", f"{y_vals[i]:.6f}"))
    
    tree.grid(row=4, column=1, padx=10, pady=10, sticky="n")
# Ejemplo de uso
# method_newton_raphson(0.5, 10, some_frame)
