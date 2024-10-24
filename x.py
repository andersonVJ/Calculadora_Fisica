import tkinter as tk
from tkinter import ttk, messagebox
import math

def convertir_unidades(valor, unidad_entrada, unidad_salida):
    # Diccionario de conversiones a la unidad base (kg, m, s, N, J)
    conversiones = {
        'kg': 1, 'g': 0.001, 'mg': 1e-6,
        'm': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000,
        's': 1, 'min': 60, 'h': 3600,
        'm/s': 1, 'km/h': 1/3.6,
        'N/m': 1, 'kN/m': 1000,
        'N': 1, 'kN': 1000,
        'J': 1, 'kJ': 1000, 'W': 1, 'kW': 1000, 'hp': 745.7
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

def calcular_trabajo(fuerza, desplazamiento, angulo, coef_friccion=None, masa=None):
    trabajo_fuerza = fuerza * desplazamiento * math.cos(math.radians(angulo))
    if coef_friccion is not None and masa is not None:
        trabajo_friccion = -coef_friccion * masa * 9.8 * desplazamiento
        return trabajo_fuerza + trabajo_friccion
    return trabajo_fuerza

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Energia y Trabajo")
        master.geometry("600x500")

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

        ttk.Label(tab, text="Fuerza:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.fuerza_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.fuerza_entry.grid(row=0, column=1, padx=5, pady=5)
        self.fuerza_unidad = ttk.Combobox(tab, values=['N', 'kN'])
        self.fuerza_unidad.set('N')
        self.fuerza_unidad.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Desplazamiento:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.desplazamiento_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.desplazamiento_entry.grid(row=1, column=1, padx=5, pady=5)
        self.desplazamiento_unidad = ttk.Combobox(tab, values=['m', 'cm', 'km'])
        self.desplazamiento_unidad.set('m')
        self.desplazamiento_unidad.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Ángulo (grados):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.angulo_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.angulo_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Coeficiente de fricción:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.coef_friccion_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.coef_friccion_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(tab, text="Masa:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.masa_trabajo_entry = ttk.Entry(tab, validate="key", validatecommand=(self.master.register(self.validar_numero), '%P'))
        self.masa_trabajo_entry.grid(row=4, column=1, padx=5, pady=5)
        self.masa_trabajo_unidad = ttk.Combobox(tab, values=['kg', 'g'])
        self.masa_trabajo_unidad.set('kg')
        self.masa_trabajo_unidad.grid(row=4, column=2, padx=5, pady=5)

        ttk.Label(tab, text="Unidad de resultado:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.resultado_trabajo_unidad = ttk.Combobox(tab, values=['J', 'kJ', 'W', 'kW', 'hp'])
        self.resultado_trabajo_unidad.set('J')
        self.resultado_trabajo_unidad.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(tab, text="Calcular", command=self.calcular_trabajo).grid(row=6, column=0, columnspan=3, pady=10)

        self.resultado_trabajo = ttk.Label(tab, text="")
        self.resultado_trabajo.grid(row=7, column=0, columnspan=3)

        self.pasos_trabajo = tk.Text(tab, height=8, width=60)
        self.pasos_trabajo.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

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
        
    def calcular_trabajo(self):
        try:
            fuerza = float(self.fuerza_entry.get())
            desplazamiento = float(self.desplazamiento_entry.get())
            angulo = float(self.angulo_entry.get())
            
            fuerza = convertir_unidades(fuerza, self.fuerza_unidad.get(), 'N')
            desplazamiento = convertir_unidades(desplazamiento, self.desplazamiento_unidad.get(), 'm')
            
            coef_friccion = self.coef_friccion_entry.get()
            masa = self.masa_trabajo_entry.get()
            
            if coef_friccion and masa:
                coef_friccion = float(coef_friccion)
                masa = float(masa)
                masa = convertir_unidades(masa, self.masa_trabajo_unidad.get(), 'kg')
                trabajo = calcular_trabajo(fuerza, desplazamiento, angulo, coef_friccion, masa)
            else:
                trabajo = calcular_trabajo(fuerza, desplazamiento, angulo)
            
            trabajo_convertido = convertir_unidades(trabajo, 'J', self.resultado_trabajo_unidad.get())
            
            self.resultado_trabajo.config(text=f"Trabajo: {trabajo_convertido:.2f} {self.resultado_trabajo_unidad.get()}")
            
            pasos = f"Pasos:\n"
            pasos += f"1. Convertir fuerza a N: {fuerza:.2f} N\n"
            pasos += f"2. Convertir desplazamiento a m: {desplazamiento:.2f} m\n"
            pasos += f"3. Calcular trabajo de la fuerza = F * d * cos(θ) = {fuerza:.2f} * {desplazamiento:.2f} * cos({angulo}°) = {fuerza * desplazamiento * math.cos(math.radians(angulo)):.2f} J\n"
            
            if coef_friccion and masa:
                pasos += f"4. Calcular trabajo de la fricción = -μ * m * g * d = -{coef_friccion:.2f} * {masa:.2f} * 9.8 * {desplazamiento:.2f} = {-coef_friccion * masa * 9.8 * desplazamiento:.2f} J\n"
                pasos += f"5. Calcular trabajo total = {trabajo:.2f} J\n"
            
            pasos += f"6. Convertir resultado a {self.resultado_trabajo_unidad.get()}: {trabajo_convertido:.2f} {self.resultado_trabajo_unidad.get()}"
            
            self.pasos_trabajo.delete('1.0', tk.END)
            self.pasos_trabajo.insert(tk.END, pasos)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def calcular_energia_cinetica(self):
        try:
            masa = float(self.masa_ec_entry.get())
            velocidad = float(self.velocidad_entry.get())
            
            masa = convertir_unidades(masa, self.masa_ec_unidad.get(), 'kg')
            velocidad = convertir_unidades(velocidad, self.velocidad_unidad.get(), 'm/s')
            
            ec = calcular_energia_cinetica(masa, velocidad)
            ec_convertida = convertir_unidades(ec, 'J', self.resultado_ec_unidad.get())
            
            self.resultado_ec.config(text=f"Energía Cinética: {ec_convertida:.2f} {self.resultado_ec_unidad.get()}")
            
            pasos = f"Pasos:\n"
            pasos += f"1. Convertir masa a kg: {masa:.2f} kg\n"
            pasos += f"2. Convertir velocidad a m/s: {velocidad:.2f} m/s\n"
            pasos += f"3. Calcular EC = 1/2 * m * v^2 = 1/2 * {masa:.2f} * {velocidad:.2f}^2 = {ec:.2f} J\n"
            pasos += f"4. Convertir resultado a {self.resultado_ec_unidad.get()}: {ec_convertida:.2f} {self.resultado_ec_unidad.get()}"
            
            self.pasos_ec.delete('1.0', tk.END)
            self.pasos_ec.insert(tk.END, pasos)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def calcular_energia_potencial_gravitatoria(self):
        try:
            masa = float(self.masa_epg_entry.get())
            altura = float(self.altura_entry.get())
            
            masa = convertir_unidades(masa, self.masa_epg_unidad.get(), 'kg')
            altura = convertir_unidades(altura, self.altura_unidad.get(), 'm')
            
            epg = calcular_energia_potencial_gravitatoria(masa, altura)
            epg_convertida = convertir_unidades(epg, 'J', self.resultado_epg_unidad.get())
            
            self.resultado_epg.config(text=f"Energía Potencial Gravitatoria: {epg_convertida:.2f} {self.resultado_epg_unidad.get()}")
            
            pasos = f"Pasos:\n"
            pasos += f"1. Convertir masa a kg: {masa:.2f} kg\n"
            pasos += f"2. Convertir altura a m: {altura:.2f} m\n"
            pasos += f"3. Calcular EPG = m * g * h = {masa:.2f} * 9.8 * {altura:.2f} = {epg:.2f} J\n"
            pasos += f"4. Convertir resultado a {self.resultado_epg_unidad.get()}: {epg_convertida:.2f} {self.resultado_epg_unidad.get()}"
            
            self.pasos_epg.delete('1.0', tk.END)
            self.pasos_epg.insert(tk.END, pasos)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def calcular_energia_potencial_elastica(self):
        try:
            k = float(self.k_entry.get())
            deformacion = float(self.deformacion_entry.get())
            
            k = convertir_unidades(k, self.k_unidad.get(), 'N/m')
            deformacion = convertir_unidades(deformacion, self.deformacion_unidad.get(), 'm')
            
            epe = calcular_energia_potencial_elastica(k, deformacion)
            epe_convertida = convertir_unidades(epe, 'J', self.resultado_epe_unidad.get())
            
            self.resultado_epe.config(text=f"Energía Potencial Elástica: {epe_convertida:.2f} {self.resultado_epe_unidad.get()}")
            
            pasos = f"Pasos:\n"
            pasos += f"1. Convertir constante elástica a N/m: {k:.2f} N/m\n"
            pasos += f"2. Convertir deformación a m: {deformacion:.2f} m\n"
            pasos += f"3. Calcular EPE = 1/2 * k * x^2 = 1/2 * {k:.2f} * {deformacion:.2f}^2 = {epe:.2f} J\n"
            pasos += f"4. Convertir resultado a {self.resultado_epe_unidad.get()}: {epe_convertida:.2f} {self.resultado_epe_unidad.get()}"
            
            self.pasos_epe.delete('1.0', tk.END)
            self.pasos_epe.insert(tk.END, pasos)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


    def mostrar_instrucciones(self):
        instrucciones = """
        Instrucciones de uso:
        
        1. Seleccione la pestaña correspondiente al tipo de cálculo que desea realizar.
        2. Ingrese los valores solicitados en los campos correspondientes.
        3. Seleccione las unidades de entrada y salida adecuadas.
        4. Haga clic en el botón "Calcular" para obtener el resultado.
        5. El resultado se mostrará en la parte inferior de la pestaña.
        6. Los pasos del cálculo se mostrarán en el cuadro de texto debajo del resultado.
        
        Nota: Asegúrese de ingresar valores numéricos válidos en todos los campos.
        """
        messagebox.showinfo("Instrucciones", instrucciones)
