import tkinter as tk
from tkinter import messagebox
import math

# Funciones de cálculo
def calcular_trabajo():
    try:
        # Obtener los valores de entrada
        fuerza = float(entry_fuerza.get())
        masa = float(entry_masa.get())
        desplazamiento = float(entry_desplazamiento.get())
        friccion_coef = float(entry_friccion.get()) if entry_friccion.get() else 0
        angulo = float(entry_angulo.get()) if entry_angulo.get() else 0

        # Constantes
        g = 9.81  # gravedad

        # Conversión a radianes
        angulo_rad = math.radians(angulo)

        # Cálculo del peso
        peso = masa * g  # P = m * g

        # Componentes del peso
        p_x = peso * math.sin(angulo_rad)  # Px = P * sin(θ)
        p_y = peso * math.cos(angulo_rad)  # Py = P * cos(θ)

        # Fuerza normal
        fuerza_normal = p_y  # N = Py

        # Fuerza de fricción
        fuerza_friccion = friccion_coef * fuerza_normal  # Fr = μ * N

        # Cálculos de trabajos
        # WF - Trabajo de la fuerza paralela
        wf = fuerza * desplazamiento  # Ángulo de 0 grados, cos(0) = 1

        # WPx - Trabajo de la componente X del peso
        wpx = -p_x * desplazamiento

        # WFr - Trabajo de la fricción
        wfr = -fuerza_friccion * desplazamiento

        # WN - Trabajo de la fuerza normal (es 0 porque la normal no realiza desplazamiento en la dirección del movimiento)
        wn = 0

        # Trabajo total
        trabajo_total = wf + wn + wpx + wfr

        # Mostrar resultados
        resultado_trabajo.config(text=f"WF (Trabajo de la fuerza): {wf:.2f} J\n"
                                      f"WN (Trabajo de la normal): {wn:.2f} J\n"
                                      f"WPX (Trabajo en X): {wpx:.2f} J\n"
                                      f"WFR (Trabajo de la fricción): {wfr:.2f} J\n"
                                      f"Trabajo Total: {trabajo_total:.2f} J")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Trabajo")

# Etiquetas y entradas para Trabajo
tk.Label(ventana_principal, text="Fuerza (N):").pack()
entry_fuerza = tk.Entry(ventana_principal)
entry_fuerza.pack()

tk.Label(ventana_principal, text="Masa (kg):").pack()
entry_masa = tk.Entry(ventana_principal)
entry_masa.pack()

tk.Label(ventana_principal, text="Desplazamiento (m):").pack()
entry_desplazamiento = tk.Entry(ventana_principal)
entry_desplazamiento.pack()

tk.Label(ventana_principal, text="Fricción (coeficiente μ):").pack()
entry_friccion = tk.Entry(ventana_principal)
entry_friccion.pack()

tk.Label(ventana_principal, text="Ángulo (°):").pack()
entry_angulo = tk.Entry(ventana_principal)
entry_angulo.pack()

# Botón para calcular el trabajo
tk.Button(ventana_principal, text="Calcular Trabajo", command=calcular_trabajo).pack()

# Etiqueta para mostrar resultados
resultado_trabajo = tk.Label(ventana_principal, text="")
resultado_trabajo.pack()

# Iniciar la interfaz gráfica
ventana_principal.mainloop()
