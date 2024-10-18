import tkinter as tk
from tkinter import ttk, messagebox
import math

def convertir_unidades(valor, unidad_entrada, unidad_salida):
    # Diccionario de conversiones a la unidad base (kg, m, s)
    conversiones = {
        'kg': 1, 'g': 0.001, 'mg': 1e-6,
        'm': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000,
        's': 1, 'min': 60, 'h': 3600,
        'm/s': 1, 'km/h': 1/3.6,
        'N/m': 1, 'kN/m': 1000
    }
    
    # Convertir a la unidad base
    valor_base = valor * conversiones[unidad_entrada]
    
    # Convertir de la unidad base a la unidad de salida
    return valor_base / conversiones[unidad_salida]

def calcular_energia_cinetica(masa, velocidad):
    return 0.5 * masa * velocidad**2

def calcular_energia_potencial_gravitatoria(masa, altura, gravedad=9.8):
    return masa * gravedad * altura

def calcular_energia_potencial_elastica(constante_elastica, deformacion):
    return 0.5 * constante_elastica * deformacion**2

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Energia")
        master.geometry("600x500")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        self.crear_tab_energia_cinetica()
        self.crear_tab_energia_potencial_gravitatoria()
        self.crear_tab_energia_potencial_elastica()
        
        menubar = tk.Menu(master)
        master.config(menu=menubar)
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Instrucciones", command=self.mostrar_instrucciones)

    def crear_tab_energia_cinetica(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Energia Cinetica")

        ttk.Label(tab, text="Masa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.masa_ec_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.masa_ec_entry.grid(row=0, column=1, padx=5, pady=5)
        self.masa_ec_unidad = ttk.Combobox(tab, values=['kg', 'g', 'mg'])
        self.masa_ec_unidad.set('kg')
        self.masa_ec_unidad.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Velocidad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.velocidad_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.velocidad_entry.grid(row=1, column=1, padx=5, pady=5)
        self.velocidad_unidad = ttk.Combobox(tab, values=['m/s', 'km/h'])
        self.velocidad_unidad.set('m/s')
        self.velocidad_unidad.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Unidad de resultado:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.resultado_ec_unidad = ttk.Combobox(tab, values=['J', 'kJ', 'W', 'kW', 'hp'])
        self.resultado_ec_unidad.set('J')
        self.resultado_ec_unidad.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_energia_cinetica).grid(row=3, column=0, columnspan=3, pady=10)

        self.resultado_ec = ttk.Label(tab, text="")
        self.resultado_ec.grid(row=4, column=0, columnspan=3)

        self.pasos_ec = tk.Text(tab, height=5, width=60)
        self.pasos_ec.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def crear_tab_energia_potencial_gravitatoria(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="E. Potencial Gravitatoria")

        ttk.Label(tab, text="Masa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.masa_epg_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.masa_epg_entry.grid(row=0, column=1, padx=5, pady=5)
        self.masa_epg_unidad = ttk.Combobox(tab, values=['kg', 'g', 'mg'])
        self.masa_epg_unidad.set('kg')
        self.masa_epg_unidad.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Altura:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.altura_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.altura_entry.grid(row=1, column=1, padx=5, pady=5)
        self.altura_unidad = ttk.Combobox(tab, values=['m', 'cm', 'mm', 'km'])
        self.altura_unidad.set('m')
        self.altura_unidad.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Unidad de resultado:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.resultado_epg_unidad = ttk.Combobox(tab, values=['J', 'kJ', 'W', 'kW', 'hp'])
        self.resultado_epg_unidad.set('J')
        self.resultado_epg_unidad.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_energia_potencial_gravitatoria).grid(row=3, column=0, columnspan=3, pady=10)

        self.resultado_epg = ttk.Label(tab, text="")
        self.resultado_epg.grid(row=4, column=0, columnspan=3)

        self.pasos_epg = tk.Text(tab, height=5, width=60)
        self.pasos_epg.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def crear_tab_energia_potencial_elastica(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="E. Potencial Elastica")

        ttk.Label(tab, text="Constante elastica:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.k_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.k_entry.grid(row=0, column=1, padx=5, pady=5)
        self.k_unidad = ttk.Combobox(tab, values=['N/m', 'kN/m'])
        self.k_unidad.set('N/m')
        self.k_unidad.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Desplazamiento:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.deformacion_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.deformacion_entry.grid(row=1, column=1, padx=5, pady=5)
        self.deformacion_unidad = ttk.Combobox(tab, values=['m', 'cm', 'mm'])
        self.deformacion_unidad.set('m')
        self.deformacion_unidad.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Unidad de resultado:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.resultado_epe_unidad = ttk.Combobox(tab, values=['J', 'kJ', 'W', 'kW', 'hp'])
        self.resultado_epe_unidad.set('J')
        self.resultado_epe_unidad.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_energia_potencial_elastica).grid(row=3, column=0, columnspan=3, pady=10)

        self.resultado_epe = ttk.Label(tab, text="")
        self.resultado_epe.grid(row=4, column=0, columnspan=3)

        self.pasos_epe = tk.Text(tab, height=5, width=60)
        self.pasos_epe.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def validar_numero(self, P):
        if P == "" or P == "-":
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False

    def calcular_energia_cinetica(self):
        try:
            masa = float(self.masa_ec_entry.get())
            velocidad = float(self.velocidad_entry.get())
            
            masa_kg = convertir_unidades(masa, self.masa_ec_unidad.get(), 'kg')
            velocidad_ms = convertir_unidades(velocidad, self.velocidad_unidad.get(), 'm/s')
            
            resultado_j = calcular_energia_cinetica(masa_kg, velocidad_ms)
            resultado_convertido = self.convertir_resultado(resultado_j, self.resultado_ec_unidad.get())
            
            self.resultado_ec.config(text=f"La energia cinetica es: {resultado_convertido:.2f} {self.resultado_ec_unidad.get()}")
            self.pasos_ec.delete('1.0', tk.END)
            self.pasos_ec.insert(tk.END, f"1. Convertir masa: {masa} {self.masa_ec_unidad.get()} = {masa_kg:.4f} kg\n")
            self.pasos_ec.insert(tk.END, f"2. Convertir velocidad: {velocidad} {self.velocidad_unidad.get()} = {velocidad_ms:.4f} m/s\n")
            self.pasos_ec.insert(tk.END, f"3. Calcular Ec = (1/2) * m * v^2:\n   0.5 * {masa_kg:.4f} * {velocidad_ms:.4f}^2 = {resultado_j:.4f} J\n")
            self.pasos_ec.insert(tk.END, f"4. Convertir resultado: {resultado_j:.4f} J = {resultado_convertido:.4f} {self.resultado_ec_unidad.get()}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos")

    def calcular_energia_potencial_gravitatoria(self):
        try:
            masa = float(self.masa_epg_entry.get())
            altura = float(self.altura_entry.get())
            
            masa_kg = convertir_unidades(masa, self.masa_epg_unidad.get(), 'kg')
            altura_m = convertir_unidades(altura, self.altura_unidad.get(), 'm')
            
            resultado_j = calcular_energia_potencial_gravitatoria(masa_kg, altura_m)
            resultado_convertido = self.convertir_resultado(resultado_j, self.resultado_epg_unidad.get())
            
            self.resultado_epg.config(text=f"La energia potencial gravitatoria es: {resultado_convertido:.2f} {self.resultado_epg_unidad.get()}")
            self.pasos_epg.delete('1.0', tk.END)
            self.pasos_epg.insert(tk.END, f"1. Convertir masa: {masa} {self.masa_epg_unidad.get()} = {masa_kg:.4f} kg\n")
            self.pasos_epg.insert(tk.END, f"2. Convertir altura: {altura} {self.altura_unidad.get()} = {altura_m:.4f} m\n")
            self.pasos_epg.insert(tk.END, f"3. Calcular Epg = m * g * h:\n   {masa_kg:.4f} * 9.8 * {altura_m:.4f} = {resultado_j:.4f} J\n")
            self.pasos_epg.insert(tk.END, f"4. Convertir resultado: {resultado_j:.4f} J = {resultado_convertido:.4f} {self.resultado_epg_unidad.get()}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos")

    def calcular_energia_potencial_elastica(self):
        try:
            k = float(self.k_entry.get())
            deformacion = float(self.deformacion_entry.get())
            
            k_nm = convertir_unidades(k, self.k_unidad.get(), 'N/m')
            deformacion_m = convertir_unidades(deformacion, self.deformacion_unidad.get(), 'm')
            
            resultado_j = calcular_energia_potencial_elastica(k_nm, deformacion_m)
            resultado_convertido = self.convertir_resultado(resultado_j, self.resultado_epe_unidad.get())
            
            self.resultado_epe.config(text=f"La energia potencial elastica es: {resultado_convertido:.2f} {self.resultado_epe_unidad.get()}")
            self.pasos_epe.delete('1.0', tk.END)
            self.pasos_epe.insert(tk.END, f"1. Convertir constante elastica: {k} {self.k_unidad.get()} = {k_nm:.4f} N/m\n")
            self.pasos_epe.insert(tk.END, f"2. Convertir desplazamiento: {deformacion} {self.deformacion_unidad.get()} = {deformacion_m:.4f} m\n")
            self.pasos_epe.insert(tk.END, f"3. Calcular Epe = (1/2) * k * x^2:\n   0.5 * {k_nm:.4f} * {deformacion_m:.4f}^2 = {resultado_j:.4f} J\n")
            self.pasos_epe.insert(tk.END, f"4. Convertir resultado: {resultado_j:.4f} J = {resultado_convertido:.4f} {self.resultado_epe_unidad.get()}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numericos validos")

    def convertir_resultado(self, valor_j, unidad_salida):
        if unidad_salida == 'J':
            return valor_j
        elif unidad_salida == 'kJ':
            return valor_j / 1000
        elif unidad_salida == 'W':
            return valor_j  # Asumiendo que la energía se libera en 1 segundo
        elif unidad_salida == 'kW':
            return valor_j / 1000  # Asumiendo que la energía se libera en 1 segundo
        elif unidad_salida == 'hp':
            return valor_j / 745.7  # 1 hp = 745.7 J/s

    def mostrar_instrucciones(self):
        instrucciones = """
        Calculadora de Energía

        Esta calculadora permite realizar cálculos de diferentes formas de energía:
        - Energía Cinética
        - Energía Potencial Gravitatoria
        - Energía Potencial Elástica

        Instrucciones de uso:
        1. Seleccione la pestaña correspondiente al tipo de energía que desea calcular.
        2. Ingrese los valores solicitados en los campos correspondientes.
        3. Seleccione las unidades de medida para cada valor ingresado.
        4. Elija la unidad de medida para el resultado.
        5. Haga clic en el botón "Calcular" para obtener el resultado.
        6. Observe los pasos del cálculo en el cuadro de texto debajo del resultado.

        Notas:
        - Asegúrese de ingresar solo valores numéricos.
        - Use el punto (.) como separador decimal.
        - Puede cambiar las unidades de medida para adaptarse a sus necesidades.
        - El resultado se puede mostrar en Joules (J), kiloJoules (kJ), Watts (W), kiloWatts (kW) o caballos de fuerza (hp).

        Si tiene alguna duda, consulte a su profesor o instructor.
        """
        messagebox.showinfo("Instrucciones", instrucciones)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()