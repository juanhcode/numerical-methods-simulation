# metodos.py
from tkinter import messagebox, Label, Entry, Button
from taylor import serieTaylor
from newton import method_newton_raphson
from diferencias_finitas import method_diferencias_finitas
from ecuaciones_no_lineales import method_jacobiano
from ecuaciones_lineales import method_ecuaciones_lineales
from ecuaciones_diferenciales_parciales import ecuaciones_diferenciales_parciales

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
    # Crear interfaz para el método de Jacobiano
    label = Label(frame, text="Ecuaciones No Lineales (Método de Jacobiano)", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

    # Entrada para la primera ecuación f1(x, y)
    Label(frame, text="Ingresa la primera ecuación f1(x, y) = 0: ").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_funcion1 = Entry(frame)
    entrada_funcion1.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para la segunda ecuación f2(x, y)
    Label(frame, text="Ingresa la segunda ecuación f2(x, y) = 0: ").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_funcion2 = Entry(frame)
    entrada_funcion2.grid(row=2, column=1, padx=10, pady=5)



    # Entrada para la aproximación inicial
    Label(frame, text="Ingresa la aproximación inicial (x0, y0): ").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entrada_aproximacion = Entry(frame)
    entrada_aproximacion.grid(row=4, column=1, padx=10, pady=5)

    def ejecutar_jacobiano():
        try:
            funcion1 = entrada_funcion1.get()
            funcion2 = entrada_funcion2.get()
            aproximacion = eval(entrada_aproximacion.get())
            method_jacobiano(funcion1, funcion2, aproximacion, frame)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

    Button(frame, text="Ejecutar Método de Jacobiano", command=ejecutar_jacobiano).grid(row=5, column=0, columnspan=2, pady=10)

def resolver_ecuaciones_lineales(frame, ventana_principal):
    # Crear interfaz para resolver ecuaciones lineales
    label = Label(frame, text="Resolver Ecuaciones Lineales", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

    # Entrada para el sistema de ecuaciones
    Label(frame, text="Ingresa el sistema de ecuaciones:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_sistema = Entry(frame)
    entrada_sistema.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para el vector de términos independientes
    Label(frame, text="Ingresa el vector de términos independientes:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_vector = Entry(frame)
    entrada_vector.grid(row=2, column=1, padx=10, pady=5)

    # Entradas para tolerancia e iteraciones
    Label(frame, text="Tolerancia:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_tolerancia = Entry(frame)
    entrada_tolerancia.grid(row=3, column=1, padx=10, pady=5)

    Label(frame, text="Máximo de iteraciones:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entrada_iteraciones = Entry(frame)
    entrada_iteraciones.grid(row=4, column=1, padx=10, pady=5)

    # Botón para ejecutar la resolución de ecuaciones lineales
    def ejecutar_resolver_ecuaciones():
        try:
            sistema = eval(entrada_sistema.get())  # Obtener el sistema de ecuaciones
            vector = eval(entrada_vector.get())  # Obtener el vector de términos independientes
            tolerancia = float(entrada_tolerancia.get())  # Obtener la tolerancia
            iteraciones = int(entrada_iteraciones.get())  # Obtener el máximo de iteraciones

            # Llamar a la función method_ecuaciones_lineales con los datos
            method_ecuaciones_lineales(sistema, vector, frame, tolerancia, iteraciones)
        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    Button(frame, text="Resolver Ecuaciones Lineales", command=ejecutar_resolver_ecuaciones).grid(row=5, column=0, columnspan=2, pady=10)

def ecuaciones_parciales(frame, ventana_principal):
    # Crear interfaz para resolver ecuaciones parciales
    label = Label(frame, text="Resolver Ecuaciones Parciales", font=("Helvetica", 16))
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Botón para volver al menú principal
    Button(frame, text="Volver", command=ventana_principal).grid(row=0, column=0, pady=10, sticky="w")

    # Entrada para la ecuación f(x, y)
    Label(frame, text="Ingresa la ecuación f(x, y) = 0 (por ejemplo, x^2 - y^2):").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entrada_funcion = Entry(frame)
    entrada_funcion.grid(row=1, column=1, padx=10, pady=5)

    # Entrada para la condición inicial u(x, y)
    Label(frame, text="Ingresa la condición inicial u(x, y) = g(x, y):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entrada_condicion = Entry(frame)
    entrada_condicion.grid(row=2, column=1, padx=10, pady=5)

    # Entrada para el intervalo [a, b] x [c, d]
    Label(frame, text="Ingresa el intervalo [a, b]:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_intervalo = Entry(frame)
    entrada_intervalo.grid(row=3, column=1, padx=10, pady=5)

    # Entrada para el número de puntos en x
    Label(frame, text="Ingresa el número de puntos en x (por ejemplo, 50):").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entrada_puntos = Entry(frame)
    entrada_puntos.grid(row=4, column=1, padx=10, pady=5)

    # Botón para ejecutar la resolución de ecuaciones parciales
    def ejecutar_ecua_parciales():
        try:
            funcion_str = entrada_funcion.get()  # Obtener la ecuación f(x, y)
            condicion_str = entrada_condicion.get()  # Obtener la condición inicial u(x, y)
            intervalo_str = entrada_intervalo.get()  # Obtener el intervalo
            puntos = int(entrada_puntos.get())  # Obtener el número de puntos

            # Convertir las entradas en funciones utilizables
            funcion = eval(f"lambda x, y: {funcion_str}")  # Asegúrate de pasar tanto 'x' como 'y'
            condicion = eval(f"lambda x, y: {condicion_str}")  # Asegúrate de pasar tanto 'x' como 'y'
            intervalo = list(map(float, intervalo_str.split(',')))  # Convertir a lista de floats

            # Llamar a la función de ecuaciones parciales
            ecuaciones_diferenciales_parciales(funcion, condicion, intervalo, puntos, frame)
        except Exception as e:
            messagebox.showerror("Error", f"Por favor verifica tus entradas: {e}")
    
    # Botón para resolver las ecuaciones
    Button(frame, text="Resolver Ecuaciones Parciales", command=ejecutar_ecua_parciales).grid(row=5, column=0, columnspan=2, pady=10)