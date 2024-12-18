import tkinter as tk
from tkinter import messagebox
import numpy as np

def method_ecuaciones_lineales(sistema, vector, frame, tolerancia, iteraciones):
    # Limpiar el contenido del frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Título de la vista
    title_label = tk.Label(
        frame,
        text="Ecuaciones Lineales",
        font=("Helvetica", 20, "bold"),
        bg="#F3F4F6",
        fg="#2C3E50",
        pady=20
    )
    title_label.pack(fill="x")

    # Frame para mostrar resultados
    result_frame = tk.Frame(frame, bg="#F3F4F6")
    result_frame.pack(expand=True, pady=20)

    # Campo para mostrar el resultado
    resultado_label = tk.Label(result_frame, text="", bg="#F3F4F6", fg="black", font=("Helvetica", 14))
    resultado_label.pack(pady=10)

    # Definir el método Gauss-Seidel
    def gauss_seidel(A, b, tol, max_iter):
        n = len(A)
        x = np.zeros_like(b, dtype=np.double)
        for k in range(max_iter):
            x_old = x.copy()
            for i in range(n):
                s1 = np.dot(A[i, :i], x[:i])
                s2 = np.dot(A[i, i + 1:], x_old[i + 1:])
                x[i] = (b[i] - s1 - s2) / A[i, i]
            if np.linalg.norm(x - x_old, ord=np.inf) < tol:
                return x
        raise Exception("El método no converge")

    # Resolver el sistema de ecuaciones
    try:
        resultado = gauss_seidel(np.array(sistema), np.array(vector), tolerancia, iteraciones)
        resultado_label.config(text=f"Resultado: {resultado}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Mostrar la matriz de coeficientes
    coeficientes_frame = tk.Frame(frame, bg="#F3F4F6")
    coeficientes_frame.pack(expand=True, pady=20)

    coeficientes_label = tk.Label(coeficientes_frame, text="Matriz de Coeficientes:", bg="#F3F4F6", fg="black", font=("Helvetica", 14))
    coeficientes_label.pack(pady=10)

    for row in sistema:
        row_label = tk.Label(coeficientes_frame, text=str(row), bg="#F3F4F6", fg="black", font=("Helvetica", 12))
        row_label.pack()
