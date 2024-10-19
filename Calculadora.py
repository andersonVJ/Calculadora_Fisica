import tkinter as tk
from tkinter import messagebox
import math

# Función para calcular trabajo e incertidumbre
def calcular_trabajo():
    try:
        # Obtener los valores de entrada
        fuerza = float(entry_fuerza.get())
        angulo = float(entry_angulo.get())
        masa = float(entry_masa.get())
        desplazamiento = float(entry_desplazamiento.get())
        friccion_coef = float(entry_friccion.get())

        # Constantes
        g = 9.81  # gravedad

        # Convertir ángulo a radianes
        angulo_rad = math.radians(angulo)

        # Cálculo del peso
        peso = masa * g

        # Fuerza normal (considerando plano inclinado)
        fuerza_normal = peso * math.cos(angulo_rad)

        # Fuerza de fricción
        fuerza_friccion = friccion_coef * fuerza_normal

        # Cálculo del trabajo de la fuerza aplicada
        trabajo_fuerza = fuerza * desplazamiento * math.cos(angulo_rad)

        # Cálculo del trabajo de la fricción (opuesto al desplazamiento)
        trabajo_friccion = -fuerza_friccion * desplazamiento

        # Trabajo total
        trabajo_total = trabajo_fuerza + trabajo_friccion

        # Calcular incertidumbre (suponiendo un 1% de error en las mediciones)
        incertidumbre = 0.01 * abs(trabajo_total)

        # Mostrar resultados
        resultado_trabajo.config(text=f"Peso: {peso:.2f} N\n"
                                      f"Fuerza Normal: {fuerza_normal:.2f} N\n"
                                      f"Fuerza de Fricción: {fuerza_friccion:.2f} N\n"
                                      f"Trabajo de la Fuerza: {trabajo_fuerza:.2f} J\n"
                                      f"Trabajo de la Fricción: {trabajo_friccion:.2f} J\n"
                                      f"Trabajo Total: {trabajo_total:.2f} J\n"
                                      f"Incertidumbre: ±{incertidumbre:.2f} J")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Función para calcular energía (no implementada)
def calcular_energia():
    messagebox.showinfo("Información", "Función 'Calcular Energía' aún no está implementada.")

# Mostrar la interfaz de cálculo de trabajo
def mostrar_calculadora_trabajo():
    resultado_trabajo.config(text="")
    for widget in trabajo_widgets:
        widget.pack(pady=5)

# Mostrar la interfaz de cálculo de energía
def mostrar_calculadora_energia():
    resultado_trabajo.config(text="Función 'Calcular Energía' aún no implementada.")
    for widget in trabajo_widgets:
        widget.pack_forget()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora Física")

ventana_principal.config(bg="#F5F5F5")

# Título principal
titulo = tk.Label(ventana_principal, text="Calculadora Física", font=("Arial", 24, "bold"), bg="#F5F5F5", fg="#2c3e50")
titulo.pack(pady=20)

# Botones para seleccionar la calculadora
boton_trabajo = tk.Button(ventana_principal, text="Calcular Trabajo", command=mostrar_calculadora_trabajo, bg="#3498db", fg="white", font=("Arial", 12), width=20)
boton_trabajo.pack(pady=10)

boton_energia = tk.Button(ventana_principal, text="Calcular Energía", command=mostrar_calculadora_energia, bg="#2ecc71", fg="white", font=("Arial", 12), width=20)
boton_energia.pack(pady=10)

# Campos de entrada para Calcular Trabajo
trabajo_widgets = []

etiqueta_fuerza = tk.Label(ventana_principal, text="Fuerza (N):", font=("Arial", 12), bg="#F5F5F5")
entry_fuerza = tk.Entry(ventana_principal)
trabajo_widgets.append(etiqueta_fuerza)
trabajo_widgets.append(entry_fuerza)

etiqueta_angulo = tk.Label(ventana_principal, text="Ángulo (°):", font=("Arial", 12), bg="#F5F5F5")
entry_angulo = tk.Entry(ventana_principal)
trabajo_widgets.append(etiqueta_angulo)
trabajo_widgets.append(entry_angulo)

etiqueta_masa = tk.Label(ventana_principal, text="Masa (kg):", font=("Arial", 12), bg="#F5F5F5")
entry_masa = tk.Entry(ventana_principal)
trabajo_widgets.append(etiqueta_masa)
trabajo_widgets.append(entry_masa)

etiqueta_desplazamiento = tk.Label(ventana_principal, text="Desplazamiento (m):", font=("Arial", 12), bg="#F5F5F5")
entry_desplazamiento = tk.Entry(ventana_principal)
trabajo_widgets.append(etiqueta_desplazamiento)
trabajo_widgets.append(entry_desplazamiento)

etiqueta_friccion = tk.Label(ventana_principal, text="Coef. de Fricción (μ):", font=("Arial", 12), bg="#F5F5F5")
entry_friccion = tk.Entry(ventana_principal)
trabajo_widgets.append(etiqueta_friccion)
trabajo_widgets.append(entry_friccion)

# Botón para calcular el trabajo
boton_calcular = tk.Button(ventana_principal, text="Calcular Trabajo", command=calcular_trabajo, bg="#3498db", fg="white", font=("Arial", 12))
trabajo_widgets.append(boton_calcular)

# Etiqueta para mostrar resultados
resultado_trabajo = tk.Label(ventana_principal, text="", font=("Arial", 12), bg="#F5F5F5", justify="left")
resultado_trabajo.pack(pady=20)

# Iniciar la interfaz gráfica
ventana_principal.mainloop()
