import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Button, Label

def ecuaciones_diferenciales_parciales(funcion, condicion, intervalo, puntos, frame):
    # Crear figura y ejes para la gráfica
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Preparar los datos para resolver la ecuación diferencial parcial
    x = np.linspace(intervalo[0], intervalo[1], puntos)
    y = np.linspace(intervalo[0], intervalo[1], puntos)  # Suponiendo que el intervalo es cuadrado

    u = np.zeros((100, puntos, puntos))  # 100 frames por defecto
    u[0, :, :] = condicion(x[:, None], y[None, :])

    dx = x[1] - x[0]
    dt = 0.01
    alpha = dt / dx**2

    # Resolución de la ecuación diferencial
    for n in range(0, 99):  # Iterar a través de los frames
        for i in range(1, puntos - 1):
            for j in range(1, puntos - 1):
                u[n + 1, i, j] = u[n, i, j] + alpha * (
                    u[n, i + 1, j] + u[n, i - 1, j] + u[n, i, j + 1] + u[n, i, j - 1] - 4 * u[n, i, j]
                ) + funcion(x[i], y[j])

    # Configuración inicial de la gráfica
    cax = ax.imshow(u[0, :, :], extent=[intervalo[0], intervalo[1], intervalo[0], intervalo[1]], origin='lower')
    ax.set_title('Solución de Ecuaciones Diferenciales Parciales')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.colorbar(cax)

    # Función para actualizar la gráfica
    def update(frame):
        cax.set_array(u[frame, :, :])
        canvas.draw()

    # Crear widget de Canvas para insertar en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

    # Botón para iniciar la animación manualmente
    def iniciar_animacion():
        for f in range(1, 100):
            frame_after = f * 50  # Velocidad de la animación
            frame_time = lambda frame=f: update(frame)
            frame.after(frame_after, frame_time)

    Button(frame, text="Iniciar Animación", command=iniciar_animacion).grid(row=6, column=0, pady=10)

    # Mostrar la solución de la ecuación diferencial parcial en un texto
    solucion_texto = f"Solución de la EDP:\n{u[-1, :, :]}"
    solucion_label = Label(frame, text=solucion_texto, justify='left')
    solucion_label.grid(row=0, column=1, rowspan=7, padx=10, pady=10, sticky='n')
