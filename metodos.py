# metodos.py
from tkinter import messagebox, Label, Entry, Button
from taylor import serieTaylor
from newton import method_newton_raphson
from diferencias_finitas import method_diferencias_finitas
from ecuaciones_no_lineales import method_biseccion

def series_de_taylor(frame, ventana_principal):
    # Crear interfaz para la serie de Taylor
    label = Label(frame, text="Serie de Taylor", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

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


def diferencias_finitias(frame, ventana_principal):
    # Crear interfaz para el método de diferencias finitas
    label = Label(frame, text="Método de Diferencias Finitas", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

    # Entrada para la ecuación f(x)
    Label(frame, text="Ingresa la ecuación f(x) = 0 (por ejemplo, x^2 - 2):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_funcion = Entry(frame)
    entrada_funcion.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para el número de puntos
    Label(frame, text="Ingresa el número de puntos (un entero positivo):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_puntos = Entry(frame)
    entrada_puntos.grid(row=2, column=1, padx=10, pady=5)

    # Entrada para el intervalo
    Label(frame, text="Ingresa el intervalo [a, b] de la función:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_intervalo = Entry(frame)
    entrada_intervalo.grid(row=3, column=1, padx=10, pady=5)

    # Botón para ejecutar el método de diferencias finitas
    def ejecutar_diferencias_finitas():
        try:
            funcion = entrada_funcion.get()  # Obtener la ecuación f(x)
            puntos = int(entrada_puntos.get())  # Obtener el número de puntos
            intervalo = entrada_intervalo.get()  # Obtener el intervalo
            # Llamar a la función de diferencias finitas con los parámetros
            method_diferencias_finitas(funcion, puntos, intervalo, frame)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")
    
    # Botón para ejecutar el método de diferencias finitas
    Button(frame, text="Generar Método de Diferencias Finitas", command=ejecutar_diferencias_finitas).grid(row=4, column=0, columnspan=2, pady=10)


def ecuaciones_no_lineales(frame, ventana_principal):
    # Crear interfaz para el método de Bisección
    label = Label(frame, text="Ecuaciones No Lineales (Método de Bisección)", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

    # Entrada para la ecuación f(x)
    Label(frame, text="Ingresa la ecuación f(x) = 0 (por ejemplo, x^2 - 2): ").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_funcion = Entry(frame)
    entrada_funcion.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para el intervalo inicial [a, b]
    Label(frame, text="Ingresa el intervalo inicial [a, b]: ").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_intervalo = Entry(frame)
    entrada_intervalo.grid(row=2, column=1, padx=10, pady=5)

    # Entrada para la tolerancia
    Label(frame, text="Ingresa la tolerancia: ").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_tolerancia = Entry(frame)
    entrada_tolerancia.grid(row=3, column=1, padx=10, pady=5)

    # Entrada para el número máximo de iteraciones
    Label(frame, text="Ingresa el número máximo de iteraciones: ").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entrada_iteraciones = Entry(frame)
    entrada_iteraciones.grid(row=4, column=1, padx=10, pady=5)

    def ejecutar_biseccion():
        try:
            funcion = entrada_funcion.get()
            intervalo = entrada_intervalo.get()
            tolerancia = float(entrada_tolerancia.get())
            iteraciones = int(entrada_iteraciones.get())
            method_biseccion(funcion, intervalo, tolerancia, iteraciones, frame)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

    Button(frame, text="Ejecutar Método de Bisección", command=ejecutar_biseccion).grid(row=5, column=0, columnspan=2, pady=10)

def ecuaciones_lineales(frame, ventana_principal):
    # Crear interfaz para el método de Gauss-Seidel
    label = Label(frame, text="Ecuaciones Lineales (Método de Gauss-Seidel)", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

    # Entrada para el sistema de ecuaciones
    Label(frame, text="Ingresa el sistema de ecuaciones (por ejemplo, [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1]]):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_sistema = Entry(frame)
    entrada_sistema.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para el vector de términos independientes
    Label(frame, text="Ingresa el vector de términos independientes (por ejemplo, [1, 1, 1]):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_vector = Entry(frame)
    entrada_vector.grid(row=2, column=1, padx=10, pady=5)

    # Entrada para la tolerancia
    Label(frame, text="Ingresa la tolerancia:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_tolerancia = Entry(frame)
    entrada_tolerancia.grid(row=3, column=1, padx=10, pady=5)

    # Entrada para el número máximo de iteraciones
    Label(frame, text="Ingresa el número máximo de iteraciones:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entrada_iteraciones = Entry(frame)
    entrada_iteraciones.grid(row=4, column=1, padx=10, pady=5)

    def ejecutar_gauss_seidel():
        try:
            sistema = eval(entrada_sistema.get())  # Obtener el sistema de ecuaciones
            vector = eval(entrada_vector.get())  # Obtener el vector de términos independientes
            tolerancia = float(entrada_tolerancia.get())  # Obtener la tolerancia
            iteraciones = int(entrada_iteraciones.get())  # Obtener el número máximo de iteraciones
            # Llamar a la función de Gauss-Seidel con los parámetros
            method_gauss_seidel(sistema, vector, tolerancia, iteraciones, frame)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")
        except SyntaxError:
            messagebox.showerror("Error", "Por favor ingresa el sistema de ecuaciones y el vector en el formato correcto")

    # Botón para ejecutar el método de Gauss-Seidel
    Button(frame, text="Ejecutar Método de Gauss-Seidel", command=ejecutar_gauss_seidel).grid(row=5, column=0, columnspan=2, pady=10)