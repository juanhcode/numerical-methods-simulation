from tkinter import Label, Entry, Button, messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para calcular y graficar la serie de Taylor
def serieTaylor(funcion, a, n, frame):
    print(funcion)
    print(a)
    print(n)
    try:
        x = sp.symbols('x')  # Variable simbólica
        f = sp.sympify(funcion)  # Convertir la entrada en una función simbólica
        T = f.subs(x, a)  # Primer término de la serie de Taylor

        # Calcular los términos de la serie de Taylor
        for k in range(1, n + 1):
            dfk = sp.diff(f, x)  # Derivada k-ésima
            T = T + dfk.subs(x, a) * ((x - a)**k) / sp.factorial(k)  # Añadir término k
            f = dfk  # Actualizar la función para la próxima derivada

        # Generar el gráfico usando matplotlib
        x_vals = np.linspace(a - 3, a + 3, 400)  # Rango de valores de x
        y_vals_F = [float(sp.N(f.subs(x, val))) for val in x_vals]  # Evaluar la función original
        y_vals_T = [float(T.subs(x, val)) for val in x_vals]  # Evaluar la serie de Taylor

        # Crear la figura
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals_F, label=f"f(x) = {funcion}", color='blue')
        ax.plot(x_vals, y_vals_T, label=f"Serie de Taylor (n={n})", color='red', linestyle='--')
        ax.set_title(f"Serie de Taylor de f(x) en x = {a}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()

        # Incrustar el gráfico en Tkinter
        for widget in frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()  # Eliminar gráficos previos
        canvas = FigureCanvasTkAgg(fig, master=frame)  # Crear el canvas de matplotlib
        canvas.draw()  # Dibujar el gráfico
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=3, padx=10, pady=10)  # Colocar el gráfico en el frame

    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {str(e)}")

# Función principal de la interfaz para la serie de Taylor
def series_de_taylor(frame):
    # Crear interfaz para la serie de Taylor
    label = Label(frame, text="Serie de Taylor", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Entrada para la función f(x)
    Label(frame, text="Ingresa la función f(x) (por ejemplo, sin(x), exp(x), log(x)):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_funcion = Entry(frame)
    entrada_funcion.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para el punto de evaluación
    Label(frame, text="Ingrese el punto a alrededor del cual se expande la serie:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_a = Entry(frame)
    entrada_a.grid(row=2, column=1, padx=10, pady=5)

    # Entrada para el grado del polinomio de Taylor
    Label(frame, text="Ingresa el grado del polinomio de Taylor (un entero positivo):").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_n = Entry(frame)
    entrada_n.grid(row=3, column=1, padx=10, pady=5)

    # Botón para ejecutar la serie de Taylor
    def ejecutar_serie_taylor():
        try:
            funcion = entrada_funcion.get()  # Obtener la función f(x)
            a = float(entrada_a.get())  # Obtener el punto 'a' de la entrada
            n = int(entrada_n.get())  # Obtener el grado del polinomio de Taylor
            serieTaylor(funcion, a, n, frame)  # Llamar a la función serieTaylor con los parámetros
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

    # Botón para ejecutar la serie de Taylor
    Button(frame, text="Generar Serie de Taylor", command=ejecutar_serie_taylor).grid(row=4, column=0, columnspan=2, pady=10)
