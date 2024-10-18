import tkinter as tk
from tkinter import messagebox
import math

# Función para calcular trabajo
def calcular_trabajo():
    try:
        # Obtener los valores de entrada
        fuerza = float(entry_fuerza.get()) if entry_fuerza.get() else 0
        angulo = float(entry_angulo.get()) if entry_angulo.get() else 0
        masa = float(entry_masa.get()) if entry_masa.get() else 0
        desplazamiento = float(entry_desplazamiento.get()) if entry_desplazamiento.get() else 0
        friccion_coef = float(entry_friccion.get()) if entry_friccion.get() else 0
        # Constantes
        g = 9.81  # gravedad
        # Cálculo del peso y la fuerza normal
        peso = masa * g  # P = m * g
        fuerza_normal = peso if masa > 0 else 30  # Asumimos 30 N como la fuerza normal estándar si no se proporciona la masa
        # Fuerza de fricción
        fuerza_friccion = friccion_coef * fuerza_normal  # Fr = μ * N
        # Conversión a radianes
        angulo_rad = math.radians(angulo)
        # Cálculo del trabajo de la fuerza aplicada en X e Y
        trabajo_fuerza_x = fuerza * desplazamiento * math.cos(angulo_rad)
        trabajo_fuerza_y = fuerza * desplazamiento * math.sin(angulo_rad)
        # Cálculo del trabajo de la fricción
        trabajo_friccion = -fuerza_friccion * desplazamiento
        # Trabajo total
        trabajo_total = trabajo_fuerza_x + trabajo_fuerza_y + trabajo_friccion
        # Mostrar resultados detallados
        resultado_trabajo.config(text=f"Peso: {peso:.2f} N\n"
                                      f"Fuerza Normal: {fuerza_normal:.2f} N\n"
                                      f"Fuerza de Fricción: {fuerza_friccion:.2f} N\n"
                                      f"Trabajo en X: {trabajo_fuerza_x:.2f} J\n"
                                      f"Trabajo en Y: {trabajo_fuerza_y:.2f} J\n"
                                      f"Trabajo de la Fricción: {trabajo_friccion:.2f} J\n"
                                      f"Trabajo Total: {trabajo_total:.2f} J")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Función para mostrar un mensaje de Energía (todavía no implementada)
def calcular_energia():
    messagebox.showinfo("Información", "Función 'Calcular Energía' aún no está implementada.")

# Mostrar la interfaz de cálculo de trabajo
def mostrar_calculadora_trabajo():
    # Limpiar la sección de resultados previos
    resultado_trabajo.config(text="")
    # Hacer visibles todos los campos de entrada para "Calcular Trabajo"
    for widget in trabajo_widgets:
        widget.pack(pady=5)

# Mostrar la interfaz de cálculo de energía
def mostrar_calculadora_energia():
    # Limpiar la sección de resultados previos
    resultado_trabajo.config(text="Función 'Calcular Energía' aún no implementada.")
    # Ocultar los campos que no son necesarios para la energía
    for widget in trabajo_widgets:
        widget.pack_forget()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora Física")
ventana_principal.geometry("600x500")
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
