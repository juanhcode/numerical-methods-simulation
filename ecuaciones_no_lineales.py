from tkinter import ttk, Frame, Tk, Scrollbar, VERTICAL, HORIZONTAL
from sympy import sympify, symbols


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

        # Calcular iteraciones
        while error > tolerancia and i <= iteraciones:
            x1 = (a + b) / 2
            f1 = f.subs(x, x1)
            x_vals.append(x1)
            f_vals.append(f1)

            if f.subs(x, a) * f1 < 0:
                b = x1
            else:
                a = x1

            error = abs(f1)
            i += 1

        # Imprimir en consola para verificar
        print("Iteración\t x\t\t f(x)")
        for i in range(len(x_vals)):
            print(f"{i}\t\t {x_vals[i]:.6f}\t {f_vals[i]:.6f}")

        # Crear contenedor para Treeview con scroll
        container = Frame(frame)
        container.grid(row=0, column=0, sticky="nsew")

        scrollbar_y = Scrollbar(container, orient=VERTICAL)
        scrollbar_x = Scrollbar(container, orient=HORIZONTAL)

        tree = ttk.Treeview(container, columns=("Iteración", "x", "f(x)"), show='headings', 
                            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        tree.heading("Iteración", text="Iteración")
        tree.heading("x", text="x")
        tree.heading("f(x)", text="f(x)")

        scrollbar_y.config(command=tree.yview)
        scrollbar_x.config(command=tree.xview)

        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        tree.pack(side="left", fill="both", expand=True)

        # Insertar datos
        for i in range(len(x_vals)):
            tree.insert("", "end", values=(i, f"{x_vals[i]:.6f}", f"{f_vals[i]:.6f}"))

        # Configuración del frame principal
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.update_idletasks()

    except Exception as e:
        print(f"Error: {e}")