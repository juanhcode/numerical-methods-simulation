import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk, Label, Entry, Button, messagebox

def method_newton_raphson(funcion, x0, tolerancia, iteraciones, frame):
    x = sp.symbols('x')
    f = sp.sympify(funcion)
    df = sp.diff(f, x)
    
    # Generar el gráfico usando matplotlib
    x_vals = np.linspace(x0 - 3, x0 + 3, 400)  # Rango de valores de x
    y_vals_F = [float(f.subs(x, val)) for val in x_vals]  # Valores de la función original f(x)
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals_F, label=f"f(x) = {funcion}", color='blue')
    ax.set_title(f"Método de Newton-Raphson para f(x) = {funcion} con x0 = {x0}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    
    # Incrustar el gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)  # Crear el canvas de matplotlib
    canvas.draw()  # Dibujar el gráfico
    canvas.get_tk_widget().grid(row=6, column=0, padx=10, pady=10, sticky="nsew")  # Colocar el gráfico en el frame
    
    # Calcular las iteraciones del método de Newton-Raphson
    x_vals = [x0]
    y_vals = [float(f.subs(x, x0))]
    for i in range(1, iteraciones + 1):
        fx = float(f.subs(x, x_vals[-1]))
        dfx = float(df.subs(x, x_vals[-1]))
        x1 = x_vals[-1] - fx / dfx
        x_vals.append(x1)
        y_vals.append(float(f.subs(x, x1)))
        if abs(x_vals[-1] - x_vals[-2]) < tolerancia:
            break
        
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
    
    tree.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")  # Colocar la tabla al lado derecho del gráfico

def newton(frame, ventana_principal):
    # Crear interfaz para el método de Newton
    label = Label(frame, text="Método de Newton", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

    # Entrada para la ecuación f(x)
    Label(frame, text="Ingresa la ecuación f(x) = 0 (por ejemplo, x^2 - 2):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_funcion = Entry(frame)
    entrada_funcion.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para la aproximación inicial x0
    Label(frame, text="Ingresa una aproximación inicial x0:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_x0 = Entry(frame)
    entrada_x0.grid(row=2, column=1, padx=10, pady=5)

    # Entrada para la tolerancia
    Label(frame, text="Ingresa la tolerancia para el método de Newton:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_tolerancia = Entry(frame)
    entrada_tolerancia.grid(row=3, column=1, padx=10, pady=5)

    # Entrada para el número máximo de iteraciones
    Label(frame, text="Ingresa el número máximo de iteraciones:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entrada_iteraciones = Entry(frame)
    entrada_iteraciones.grid(row=4, column=1, padx=10, pady=5)

    # Botón para ejecutar el método de Newton
    def ejecutar_newton():
        try:
            funcion = entrada_funcion.get()  # Obtener la ecuación f(x)
            x0 = float(entrada_x0.get())  # Obtener la aproximación inicial 'x0'
            tolerancia = float(entrada_tolerancia.get())  # Obtener la tolerancia
            iteraciones = int(entrada_iteraciones.get())  # Obtener el número máximo de iteraciones
            # Llamar a la función de Newton con los parámetros
            method_newton_raphson(funcion, x0, tolerancia, iteraciones, frame)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

    # Botón para ejecutar el método de Newton
    Button(frame, text="Generar Método de Newton", command=ejecutar_newton).grid(row=5, column=0, columnspan=2, pady=10)
