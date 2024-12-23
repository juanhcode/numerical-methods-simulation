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

    # Definir el método Jacobi
    def jacobi(A, b, tolerancia, iteraciones):
        x = np.zeros_like(b, dtype=np.double)
        D = np.diag(A)
        R = A - np.diagflat(D)
        iter_count = 0

        for _ in range(iteraciones):
            x_prev = np.copy(x)
            x = (b - np.dot(R, x)) / D
            iter_count += 1
            if np.linalg.norm(x - x_prev) < tolerancia:
                return x, iter_count
        return x, iter_count

    # Resolver el sistema de ecuaciones
    try:
        resultado, iteraciones_usadas = jacobi(np.array(sistema).astype(float), np.array(vector).astype(float), tolerancia, iteraciones)
        resultado_label.config(text=f"Resultado: {resultado}\nIteraciones: {iteraciones_usadas}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Resolver el sistema de ecuaciones
    try:
        resultado = jacobi(np.array(sistema).astype(float), np.array(vector).astype(float), tolerancia, iteraciones)
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
