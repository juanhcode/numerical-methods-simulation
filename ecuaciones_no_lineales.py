from tkinter import ttk, Frame, Scrollbar, VERTICAL, HORIZONTAL, messagebox, Label, Entry, Button
from sympy import sympify, symbols, diff, Matrix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def method_jacobiano(funcion1, funcion2, aproximacion, frame):
    try:
        # Limpiar el frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Configurar variables
        x, y = symbols('x y')
        f1 = sympify(funcion1)
        f2 = sympify(funcion2)
        x0, y0 = aproximacion
        tol = 1e-6
        max_iter = 50

        # Definir las funciones y el Jacobiano
        F = Matrix([f1, f2])
        J = F.jacobian([x, y])

        iteraciones = []
        x_vals = []
        y_vals = []
        for i in range(max_iter):
            F_val = F.subs({x: x0, y: y0})
            J_val = J.subs({x: x0, y: y0})
            delta = J_val.inv() * (-F_val)
            x0, y0 = x0 + delta[0], y0 + delta[1]
            iteraciones.append((i + 1, x0, y0, F_val[0], F_val[1], J_val))
            x_vals.append(x0)
            y_vals.append(y0)

            if max(abs(delta)) < tol:
                break

        # Crear contenedor para Treeview con scroll
        container = Frame(frame)
        container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        scrollbar_y = Scrollbar(container, orient=VERTICAL)
        scrollbar_x = Scrollbar(container, orient=HORIZONTAL)

        tree = ttk.Treeview(container, columns=("Iteración", "x", "y", "f1(x,y)", "f2(x,y)", "Jacobian"),
                            show='headings', yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        tree.heading("Iteración", text="Iteración")
        tree.heading("x", text="x")
        tree.heading("y", text="y")
        tree.heading("f1(x,y)", text="f1(x,y)")
        tree.heading("f2(x,y)", text="f2(x,y)")
        tree.heading("Jacobian", text="Jacobian")

        scrollbar_y.config(command=tree.yview)
        scrollbar_x.config(command=tree.xview)

        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        tree.pack(side="left", fill="both", expand=True)

        # Insertar datos
        for iteracion in iteraciones:
            i, x_val, y_val, f1_val, f2_val, J_val = iteracion
            tree.insert("", "end", values=(
                i, f"{x_val:.6f}", f"{y_val:.6f}", f"{f1_val:.6f}", f"{f2_val:.6f}", J_val
            ))

        # Crear la gráfica de las iteraciones
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, 'bo-', label='Iteraciones')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Iteraciones del Método de Jacobiano')
        ax.legend()

        # Integrar la gráfica en el frame de tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Configuración del frame principal
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.update_idletasks()

    except Exception as e:
        messagebox.showerror("Error", str(e))

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
    Label(frame, text="Ingresa la aproximación inicial (x0, y0): ").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entrada_aproximacion = Entry(frame)
    entrada_aproximacion.grid(row=3, column=1, padx=10, pady=5)

    def ejecutar_jacobiano():
        try:
            funcion1 = entrada_funcion1.get()
            funcion2 = entrada_funcion2.get()
            aproximacion = eval(entrada_aproximacion.get())
            method_jacobiano(funcion1, funcion2, aproximacion, frame)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

    Button(frame, text="Ejecutar Método de Jacobiano", command=ejecutar_jacobiano).grid(row=4, column=0, columnspan=2, pady=10)
