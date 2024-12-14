# metodos.py
from tkinter import messagebox, Label, Entry, Button
from taylor import serieTaylor
from newton import method_newton_raphson

def series_de_taylor(frame):  # Recibir 'frame' como argumento
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


def newton(frame):
    # Crear interfaz para el método de Newton
    label = Label(frame, text="Método de Newton", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Entrada para el punto de evaluación
    Label(frame, text="Digite el punto inicial:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_x0 = Entry(frame)
    entrada_x0.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para el número de iteraciones
    Label(frame, text="Digite el número de iteraciones:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_n = Entry(frame)
    entrada_n.grid(row=2, column=1, padx=10, pady=5)

    # Botón para ejecutar el método de Newton
    def ejecutar_newton():
        try:
            x0 = float(entrada_x0.get())  # Obtener el punto inicial 'x0'
            n = int(entrada_n.get())  # Obtener el número de iteraciones 'n'
            # Llamar a la función de Newton con los parámetros
            method_newton_raphson(x0, n, frame)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

    # Botón para ejecutar el método de Newton
    Button(frame, text="Generar Método de Newton", command=ejecutar_newton).grid(row=3, column=0, columnspan=2, pady=10)
