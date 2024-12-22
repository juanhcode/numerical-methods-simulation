import sympy as sp
from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox, Frame, Label, Text
from mpmath import *



def serieTaylor(funcion, a, n, frame):
    try:
        x = sp.symbols('x')  # Variable simbólica
        f = sp.parse_expr(funcion)  # Convertir la entrada en una función simbólica
        T = f.subs(x, a)  # Primer término de la serie de Taylor
        derivadas = [f"f(x) = {f}"]
        polinomio_str = f"{f.subs(x, a)}"  # Primer término del polinomio como cadena
        polinomio_exp = sp.sympify(f.subs(x, a))  # Primer término como expresión simbólica

        # Calcular los términos de la serie de Taylor
        for k in range(1, n + 1):
            dfk = sp.diff(f, x)  # Derivada k-ésima
            derivadas.append(f"f^{k}(x) = {dfk}")
            # Añadir el término k al polinomio (expresión simbólica)
            term_k = dfk.subs(x, a) * (x - a)**k / sp.factorial(k)
            polinomio_exp += term_k  # Sumar el término k al polinomio simbólicamente
            polinomio_str += f" + ({dfk.subs(x, a)} * (x - {a})^{k} / {sp.factorial(k)})"
            f = dfk  # Actualizar la función para la próxima derivada

        # Generar el gráfico usando matplotlib
        x_vals = np.linspace(a - 3, a + 3, 400)  # Rango de valores de x
        y_vals_F = [float(sp.N(f.subs(x, val))) for val in x_vals]  # Evaluar la función original
        y_vals_T = [float(sp.N(polinomio_exp.subs(x, val))) for val in x_vals]  # Evaluar la serie de Taylor

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
        canvas.get_tk_widget().grid(row=5, column=0, padx=10, pady=10)  # Colocar el gráfico en el frame

        # Añadir barra de herramientas de navegación
        toolbar_frame = Frame(frame)
        toolbar_frame.grid(row=6, column=0, padx=10, pady=10)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()

        # Crear un frame para las derivadas
        frame_derivadas = Frame(frame, bg='white')
        frame_derivadas.grid(row=5, column=1, padx=10, pady=10, sticky='n')

        # Título para las derivadas
        Label(frame_derivadas, text="Derivadas", bg='black', font=("Helvetica", 14)).pack(pady=5)

        # Mostrar las derivadas en el frame
        text_derivadas = Text(frame_derivadas, height=20, width=50, bg='black')
        text_derivadas.pack(pady=5)
        text_derivadas.insert('1.0', "\n".join(derivadas))
        text_derivadas.config(state='disabled')

       
        # Mostrar el polinomio de Taylor
        f = sp.sympify(funcion)  # Convertir la función a una expresión simbólica

        # Expansión de Taylor alrededor de a hasta el término de grado n
        taylor_expansion = f.series(x, a, n+1).removeO()  # Expansión de Taylor de grado n
        
        # Crear un frame para el polinomio de Taylor
        frame_polinomio = Frame(frame, bg='white')
        frame_polinomio.grid(row=5, column=2, padx=10, pady=10, sticky='n')

        # Título para el polinomio de Taylor
        Label(frame_polinomio, text="Polinomio de Taylor", bg='black', font=("Helvetica", 14)).pack(pady=5)

        # Mostrar el polinomio de Taylor en el frame
        text_polinomio = Text(frame_polinomio, height=5, width=50, bg='black', fg='white')
        text_polinomio.pack(pady=5)
        text_polinomio.insert('1.0', str(taylor_expansion))
        text_polinomio.config(state='disabled')




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
            funcion = entrada_funcion.get().replace(' ', '')  # Obtener la función f(x) y eliminar espacios
            a = float(entrada_a.get())  # Obtener el punto 'a' de la entrada
            n = int(entrada_n.get())  # Obtener el grado del polinomio de Taylor
            serieTaylor(funcion, a, n, frame)  # Llamar a la función serieTaylor con los parámetros
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

    # Botón para ejecutar la serie de Taylor
    Button(frame, text="Generar Serie de Taylor", command=ejecutar_serie_taylor).grid(row=4, column=0, columnspan=2, pady=10)
