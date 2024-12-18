from tkinter import ttk, Frame, Scrollbar, VERTICAL, HORIZONTAL, messagebox
from sympy import sympify, symbols
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def method_biseccion(funcion, intervalo, tolerancia, iteraciones, frame):
    try:
        # Limpiar el frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Configurar variables
        x = symbols('x')
        f = sympify(funcion)
        a, b = map(float, intervalo.split(","))
        if f.subs(x, a) * f.subs(x, b) > 0:
            raise ValueError("La función debe tener signos opuestos en los extremos del intervalo o uno de los extremos debe ser una raíz")

        i = 1
        error = tolerancia + 1
        x_vals = []
        f_vals = []
        a_vals = []
        b_vals = []
        mid_vals = []

        # Calcular iteraciones
        while error > tolerancia and i <= iteraciones:
            x1 = (a + b) / 2
            f1 = f.subs(x, x1)
            x_vals.append(x1)
            f_vals.append(f1)
            a_vals.append(a)
            b_vals.append(b)
            mid_vals.append(x1)

            if f.subs(x, a) * f1 < 0:
                b = x1
            else:
                a = x1

            error = abs(f1)
            i += 1

        # Crear contenedor para Treeview con scroll
        container = Frame(frame)
        container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        scrollbar_y = Scrollbar(container, orient=VERTICAL)
        scrollbar_x = Scrollbar(container, orient=HORIZONTAL)

        tree = ttk.Treeview(container, columns=("Iteración", "a", "b", "x", "f(a)", "f(b)", "f(x)"),
                            show='headings', yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        tree.heading("Iteración", text="Iteración")
        tree.heading("a", text="a")
        tree.heading("b", text="b")
        tree.heading("x", text="x")
        tree.heading("f(a)", text="f(a)")
        tree.heading("f(b)", text="f(b)")
        tree.heading("f(x)", text="f(x)")

        scrollbar_y.config(command=tree.yview)
        scrollbar_x.config(command=tree.xview)

        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        tree.pack(side="left", fill="both", expand=True)

        # Insertar datos
        for i in range(len(x_vals)):
            tree.insert("", "end", values=(
                i + 1, f"{a_vals[i]:.6f}", f"{b_vals[i]:.6f}", f"{x_vals[i]:.6f}",
                f"{f.subs(x, a_vals[i]):.6f}", f"{f.subs(x, b_vals[i]):.6f}", f"{f_vals[i]:.6f}"
            ))

        # Graficar resultados
        fig, ax = plt.subplots(figsize=(8, 4))

        # Graficar la función en el intervalo
        x_range = np.linspace(a_vals[0], b_vals[0], 400)
        y_range = [f.subs(x, val) for val in x_range]
        ax.plot(x_range, y_range, label=f"f(x) = {funcion}")

        # Graficar las iteraciones
        colors = plt.cm.viridis(np.linspace(0, 1, len(x_vals)))
        for i in range(len(x_vals)):
            ax.plot(x_vals[i], f_vals[i], 'o', color=colors[i], label=f"Iteración {i+1}")
            if i > 0:
                ax.plot([x_vals[i-1], x_vals[i]], [f_vals[i-1], f_vals[i]], color=colors[i])
        ax.axhline(0, color='red', linestyle='--')
        ax.set_title("Convergencia del Método de Bisección")
        ax.set_xlabel("Punto medio (x)")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid()

        # Insertar gráfico en el frame
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")
        canvas.draw()

        # Configuración del frame principal
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.update_idletasks()

    except Exception as e:
        messagebox.showerror("Error", str(e))
