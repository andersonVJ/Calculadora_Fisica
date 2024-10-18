import tkinter as tk
from tkinter import ttk, messagebox
import math

def calcular_trabajo(fuerza, distancia, angulo):
    return fuerza * distancia * math.cos(math.radians(angulo))

def calcular_energia_cinetica(masa, velocidad):
    return 0.5 * masa * velocidad**2

def calcular_energia_potencial_gravitatoria(masa, altura, gravedad=9.8):
    return masa * gravedad * altura

def calcular_energia_potencial_elastica(constante_elastica, deformacion):
    return 0.5 * constante_elastica * deformacion**2

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Trabajo y Energia")
        master.geometry("500x400")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        self.crear_tab_trabajo()
        self.crear_tab_energia_cinetica()
        self.crear_tab_energia_potencial_gravitatoria()
        self.crear_tab_energia_potencial_elastica()
        
        menubar = tk.Menu(master)
        master.config(menu=menubar)
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Instrucciones", command=self.mostrar_instrucciones)

    def crear_tab_trabajo(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Trabajo")

        ttk.Label(tab, text="Fuerza (N):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.fuerza_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.fuerza_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Distancia (m):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.distancia_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.distancia_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Angulo (grados):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.angulo_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.angulo_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_trabajo).grid(row=3, column=0, columnspan=2, pady=10)

        self.resultado_trabajo = ttk.Label(tab, text="")
        self.resultado_trabajo.grid(row=4, column=0, columnspan=2)

        self.pasos_trabajo = tk.Text(tab, height=5, width=50)
        self.pasos_trabajo.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def crear_tab_energia_cinetica(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Energia Cinetica")

        ttk.Label(tab, text="Masa (kg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.masa_ec_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.masa_ec_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Velocidad (m/s):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.velocidad_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.velocidad_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_energia_cinetica).grid(row=2, column=0, columnspan=2, pady=10)

        self.resultado_ec = ttk.Label(tab, text="")
        self.resultado_ec.grid(row=3, column=0, columnspan=2)

        self.pasos_ec = tk.Text(tab, height=5, width=50)
        self.pasos_ec.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def crear_tab_energia_potencial_gravitatoria(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="E. Potencial Gravitatoria")

        ttk.Label(tab, text="Masa (kg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.masa_epg_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.masa_epg_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Altura (m):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.altura_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.altura_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_energia_potencial_gravitatoria).grid(row=2, column=0, columnspan=2, pady=10)

        self.resultado_epg = ttk.Label(tab, text="")
        self.resultado_epg.grid(row=3, column=0, columnspan=2)

        self.pasos_epg = tk.Text(tab, height=5, width=50)
        self.pasos_epg.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def crear_tab_energia_potencial_elastica(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="E. Potencial Elastica")

        ttk.Label(tab, text="Constante elastica (N/m):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.k_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.k_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Desplazamiento (m):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.deformacion_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.deformacion_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_energia_potencial_elastica).grid(row=2, column=0, columnspan=2, pady=10)

        self.resultado_epe = ttk.Label(tab, text="")
        self.resultado_epe.grid(row=3, column=0, columnspan=2)

        self.pasos_epe = tk.Text(tab, height=5, width=50)
        self.pasos_epe.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def validar_numero(self, P):
        if P == "" or P == "-":
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False

    def calcular_trabajo(self):
        try:
            fuerza = float(self.fuerza_entry.get())
            distancia = float(self.distancia_entry.get())
            angulo = float(self.angulo_entry.get())
            resultado = calcular_trabajo(fuerza, distancia, angulo)
            self.resultado_trabajo.config(text=f"El trabajo es: {resultado:.2f} J")
            self.pasos_trabajo.delete('1.0', tk.END)
            self.pasos_trabajo.insert(tk.END, f"1. Convertir ángulo a radianes: {angulo} * (π/180) = {math.radians(angulo):.4f} rad\n")
            self.pasos_trabajo.insert(tk.END, f"2. Calcular cos(ángulo): cos({math.radians(angulo):.4f}) = {math.cos(math.radians(angulo)):.4f}\n")
            self.pasos_trabajo.insert(tk.END, f"3. Multiplicar fuerza * distancia * cos(ángulo):\n   {fuerza} * {distancia} * {math.cos(math.radians(angulo)):.4f} = {resultado:.2f} J")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos")

    def calcular_energia_cinetica(self):
        try:
            masa = float(self.masa_ec_entry.get())
            velocidad = float(self.velocidad_entry.get())
            resultado = calcular_energia_cinetica(masa, velocidad)
            self.resultado_ec.config(text=f"La energia cinetica es: {resultado:.2f} J")
            self.pasos_ec.delete('1.0', tk.END)
            self.pasos_ec.insert(tk.END, f"1. Calcular el cuadrado de la velocidad: {velocidad}^2 = {velocidad**2:.2f}\n")
            self.pasos_ec.insert(tk.END, f"2. Multiplicar (1/2) * masa * velocidad^2:\n   0.5 * {masa} * {velocidad**2:.2f} = {resultado:.2f} J")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos")

    def calcular_energia_potencial_gravitatoria(self):
        try:
            masa = float(self.masa_epg_entry.get())
            altura = float(self.altura_entry.get())
            resultado = calcular_energia_potencial_gravitatoria(masa, altura)
            self.resultado_epg.config(text=f"La energia potencial gravitatoria es: {resultado:.2f} J")
            self.pasos_epg.delete('1.0', tk.END)
            self.pasos_epg.insert(tk.END, f"1. Multiplicar masa * gravedad * altura:\n")
            self.pasos_epg.insert(tk.END, f"   {masa} * 9.8 * {altura} = {resultado:.2f} J")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos")

    def calcular_energia_potencial_elastica(self):
        try:
            k = float(self.k_entry.get())
            deformacion = float(self.deformacion_entry.get())
            resultado = calcular_energia_potencial_elastica(k, deformacion)
            self.resultado_epe.config(text=f"La energia potencial elastica es: {resultado:.2f} J")
            self.pasos_epe.delete('1.0', tk.END)
            self.pasos_epe.insert(tk.END, f"1. Calcular el cuadrado de la deformación: {deformacion}^2 = {deformacion**2:.4f}\n")
            self.pasos_epe.insert(tk.END, f"2. Multiplicar (1/2) * k * deformación^2:\n   0.5 * {k} * {deformacion**2:.4f} = {resultado:.2f} J")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos")

    def mostrar_instrucciones(self):
        instrucciones = """
        Calculadora de Trabajo y Energía

        Esta calculadora permite realizar cálculos relacionados con trabajo y diferentes formas de energía.

        Instrucciones de uso:
        1. Seleccione la pestaña correspondiente al cálculo que desea realizar.
        2. Ingrese los valores solicitados en los campos correspondientes.
        3. Haga clic en el botón "Calcular" para obtener el resultado.
        4. Observe los pasos del cálculo en el cuadro de texto debajo del resultado.

        Notas:
        - Asegúrese de ingresar solo valores numéricos.
        - Use el punto (.) como separador decimal.
        - Los resultados se muestran en Joules (J).

        Si tiene alguna duda, consulte a su profesor o instructor.
        """
        messagebox.showinfo("Instrucciones", instrucciones)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()