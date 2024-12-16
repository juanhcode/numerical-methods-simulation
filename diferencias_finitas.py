from sympy import sympify, symbols
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def method_diferencias_finitas(funcion, puntos, intervalo, frame):
    """
    Aplica el método de diferencias finitas a una función dada y muestra los resultados en una interfaz Tkinter.

    Parameters:
    funcion (str): La función a evaluar en formato de cadena.
    puntos (int): El número de puntos a utilizar en el intervalo.
    intervalo (str): El intervalo en el que se evaluará la función, en formato "a,b".
    frame (tkinter.Frame): El frame de Tkinter donde se mostrarán los resultados.

    Returns:
    None
    """
    try:
        # Convertir la cadena de texto a una expresión matemática
        f = sympify(funcion)
        n = int(puntos)
        a, b = map(float, intervalo.split(","))
        if n <= 1:
            raise ValueError("El número de puntos debe ser mayor que 1")
        h = (b - a) / (n - 1)
        
        # Crear una lista de puntos en el intervalo [a, b]
        x_vals = [a + i * h for i in range(n)]
        x = symbols('x')
        y_vals = [float(f.subs(x, x_vals[i])) for i in range(n)]
        
        # Crear una matriz de diferencias finitas
        matriz = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            matriz[i][0] = y_vals[i]
        
        for j in range(1, n):
            for i in range(n - j):
                matriz[i][j] = matriz[i + 1][j - 1] - matriz[i][j - 1]
        
        # Mostrar la tabla de diferencias finitas
        print("Tabla de Diferencias Finitas")
        for i in range(n):
            print("\t".join([f"{matriz[i][j]:.6f}" for j in range(n - i)]))
        
        # Mostrar la tabla en un tablero de Tkinter
        tree = ttk.Treeview(frame, columns=[f"Columna {i}" for i in range(n)], show='headings')
        for i in range(n):
            tree.heading(f"Columna {i}", text=f"Columna {i}")
        
        for i in range(n):
            tree.insert("", "end", values=[f"{matriz[i][j]:.6f}" for j in range(n - i)])
        
        tree.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        
        # Imprimir la matriz a un lado de la gráfica
        for i in range(n):
            print(f"Fila {i}: ", end="")
            for j in range(n - i):
                print(f"{matriz[i][j]:.6f} ", end="")
            print()
        
        # Crear la figura de matplotlib con tamaño ajustado
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Graficar la función original
        x_vals_dense = np.linspace(a, b, 400)
        y_vals_dense = [float(f.subs(x, val)) for val in x_vals_dense]
        ax.plot(x_vals_dense, y_vals_dense, label='Función Original', color='blue')
        
        # Graficar las diferencias finitas
        for j in range(1, n):
            ax.plot(x_vals[:n-j], [matriz[i][j] for i in range(n-j)], label=f"Diferencias de orden {j}")
        
        ax.set_xlabel('x')
        ax.set_ylabel('Diferencias finitas')
        ax.set_title('Gráfica de Diferencias Finitas')
        ax.legend()
        ax.grid(True)
        
        # Mostrar la gráfica en el frame de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        
        # Generar la matriz de Gauss
        gauss_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n - i):
                gauss_matrix[i, j] = matriz[i][j]
        
        print("Matriz de Gauss:")
        print(gauss_matrix)
        
        # Mostrar la matriz de Gauss en un Treeview de Tkinter
        gauss_tree = ttk.Treeview(frame, columns=[f"Columna {i}" for i in range(n)], show='headings')
        for i in range(n):
            gauss_tree.heading(f"Columna {i}", text=f"Columna {i}")
        
        for i in range(n):
            gauss_tree.insert("", "end", values=[f"{gauss_matrix[i, j]:.6f}" for j in range(n)])
        
        gauss_tree.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos")