import tkinter as tk
from tkinter import ttk, messagebox
import math

from Energia import calcular_energia_cinetica, calcular_energia_potencial_elastica, calcular_energia_potencial_gravitatoria

def convertir_unidades(valor, unidad_entrada, unidad_salida):
    conversiones = {
        'kg': 1, 'g': 0.001, 'mg': 1e-6,
        'm': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000,
        's': 1, 'min': 60, 'h': 3600,
        'm/s': 1, 'km/h': 1/3.6,
        'N/m': 1, 'kN/m': 1000
    }
    valor_base = valor * conversiones[unidad_entrada]
    return valor_base / conversiones[unidad_salida]

def calcular_trabajo(fuerza, angulo, desplazamiento, coef_friccion, masa):
    angulo_rad = math.radians(angulo)
    
    # Cálculo del peso y fuerza normal
    gravedad = 9.81  # m/s^2
    peso = masa * gravedad
    fuerza_normal = peso * math.cos(angulo_rad)
    
    # Cálculo de la fuerza de fricción
    fuerza_friccion = coef_friccion * fuerza_normal
    
    # Trabajo de la fuerza (considerando fricción)
    trabajo_fuerza = fuerza * desplazamiento * math.cos(angulo_rad)
    trabajo_friccion = fuerza_friccion * desplazamiento
    
    # Trabajo total
    trabajo_total = trabajo_fuerza - trabajo_friccion

    # Calcular incertidumbre (ejemplo: ±5% del trabajo total)
    incertidumbre = 0.05 * abs(trabajo_total)

    return peso, fuerza_normal, fuerza_friccion, trabajo_fuerza, trabajo_friccion, trabajo_total, incertidumbre

class CalculadoraFisicaApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Física")
        master.geometry("600x600")
        
        # Estilo
        master.configure(bg="#F5F5F5")
        
        # Título principal
        self.titulo = tk.Label(master, text="Calculadora Física", font=("Arial", 24, "bold"), 
                             bg="#F5F5F5", fg="#2c3e50")
        self.titulo.pack(pady=20)
        
        # Crear notebook para las pestañas
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=5)
        
        # Crear las pestañas
        self.tab_trabajo = ttk.Frame(self.notebook)
        self.tab_energia = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_trabajo, text="Calculadora de Trabajo")
        self.notebook.add(self.tab_energia, text="Calculadora de Energía")
        
        # Inicializar ambas calculadoras
        self.inicializar_calculadora_trabajo()
        self.inicializar_calculadora_energia()
        
        # Crear menú
        self.crear_menu()

    def crear_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        # Menú de ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Instrucciones", command=self.mostrar_instrucciones)

    def inicializar_calculadora_trabajo(self):
        # Widgets para la calculadora de trabajo
        self.trabajo_widgets = []
        
        campos = [
            ("Fuerza (N):", "entry_fuerza"),
            ("Ángulo (°):", "entry_angulo"),
            ("Desplazamiento (m):", "entry_desplazamiento"),
            ("Coeficiente de Fricción:", "entry_coef_friccion"),
            ("Masa (kg):", "entry_masa")  # Nueva entrada para la masa
        ]
        
        for i, (label_text, entry_name) in enumerate(campos):
            label = ttk.Label(self.tab_trabajo, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(self.tab_trabajo)
            entry.grid(row=i, column=1, padx=5, pady=5)
            setattr(self, entry_name, entry)
            self.trabajo_widgets.extend([label, entry])
        
        # Botón calcular trabajo
        self.boton_calcular_trabajo = ttk.Button(self.tab_trabajo, 
                                               text="Calcular Trabajo",
                                               command=self.calcular_trabajo)
        self.boton_calcular_trabajo.grid(row=len(campos), column=0, 
                                       columnspan=2, pady=10)
        
        # Resultado trabajo
        self.resultado_trabajo = ttk.Label(self.tab_trabajo, text="")
        self.resultado_trabajo.grid(row=len(campos)+1, column=0, 
                                  columnspan=2, pady=10)

    def inicializar_calculadora_energia(self):
        # Crear pestañas para los diferentes tipos de energía
        self.energia_notebook = ttk.Notebook(self.tab_energia)
        self.energia_notebook.pack(expand=True, fill="both")
        
        # Crear sub-pestañas para cada tipo de energía
        self.tab_ec = ttk.Frame(self.energia_notebook)
        self.tab_epg = ttk.Frame(self.energia_notebook)
        self.tab_epe = ttk.Frame(self.energia_notebook)
        
        self.energia_notebook.add(self.tab_ec, text="Energía Cinética")
        self.energia_notebook.add(self.tab_epg, text="E. Potencial Gravitatoria")
        self.energia_notebook.add(self.tab_epe, text="E. Potencial Elástica")
        
        self.inicializar_energia_cinetica()
        self.inicializar_energia_potencial_gravitatoria()
        self.inicializar_energia_potencial_elastica()

    def inicializar_energia_cinetica(self):
        # Campos para energía cinética
        ttk.Label(self.tab_ec, text="Masa:").grid(row=0, column=0, padx=5, pady=5)
        self.masa_ec_entry = ttk.Entry(self.tab_ec)
        self.masa_ec_entry.grid(row=0, column=1, padx=5, pady=5)
        self.masa_ec_unidad = ttk.Combobox(self.tab_ec, values=['kg', 'g', 'mg'])
        self.masa_ec_unidad.set('kg')
        self.masa_ec_unidad.grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(self.tab_ec, text="Velocidad:").grid(row=1, column=0, padx=5, pady=5)
        self.velocidad_entry = ttk.Entry(self.tab_ec)
        self.velocidad_entry.grid(row=1, column=1, padx=5, pady=5)
        self.velocidad_unidad = ttk.Combobox(self.tab_ec, values=['m/s', 'km/h'])
        self.velocidad_unidad.set('m/s')
        self.velocidad_unidad.grid(row=1, column=2, padx=5, pady=5)
        
        ttk.Button(self.tab_ec, text="Calcular", 
                  command=self.calcular_energia_cinetica).grid(row=3, column=0, 
                                                             columnspan=3, pady=10)
        
        self.resultado_ec = ttk.Label(self.tab_ec, text="")
        self.resultado_ec.grid(row=4, column=0, columnspan=3)

    def inicializar_energia_potencial_gravitatoria(self):
        # Campos para energía potencial gravitatoria
        ttk.Label(self.tab_epg, text="Masa:").grid(row=0, column=0, padx=5, pady=5)
        self.masa_epg_entry = ttk.Entry(self.tab_epg)
        self.masa_epg_entry.grid(row=0, column=1, padx=5, pady=5)
        self.masa_epg_unidad = ttk.Combobox(self.tab_epg, values=['kg', 'g', 'mg'])
        self.masa_epg_unidad.set('kg')
        self.masa_epg_unidad.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(self.tab_epg, text="Altura:").grid(row=1, column=0, padx=5, pady=5)
        self.altura_entry = ttk.Entry(self.tab_epg)
        self.altura_entry.grid(row=1, column=1, padx=5, pady=5)
        self.altura_unidad = ttk.Combobox(self.tab_epg, values=['m', 'cm', 'mm', 'km'])
        self.altura_unidad.set('m')
        self.altura_unidad.grid(row=1, column=2, padx=5, pady=5)

        ttk.Button(self.tab_epg, text="Calcular", 
                  command=self.calcular_energia_potencial_gravitatoria).grid(row=3, 
                                                                         column=0, 
                                                                         columnspan=3, pady=10)

        self.resultado_epg = ttk.Label(self.tab_epg, text="")
        self.resultado_epg.grid(row=4, column=0, columnspan=3)

    def inicializar_energia_potencial_elastica(self):
        # Campos para energía potencial elástica
        ttk.Label(self.tab_epe, text="Constante elástica (N/m):").grid(row=0, column=0, padx=5, pady=5)
        self.constante_entry = ttk.Entry(self.tab_epe)
        self.constante_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.tab_epe, text="Deformación (m):").grid(row=1, column=0, padx=5, pady=5)
        self.deformacion_entry = ttk.Entry(self.tab_epe)
        self.deformacion_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.tab_epe, text="Calcular", 
                  command=self.calcular_energia_potencial_elastica).grid(row=3, 
                                                                         column=0, 
                                                                         columnspan=2, 
                                                                         pady=10)

        self.resultado_epe = ttk.Label(self.tab_epe, text="")
        self.resultado_epe.grid(row=4, column=0, columnspan=2)

    def calcular_trabajo(self):
        try:
            fuerza = float(self.entry_fuerza.get())
            angulo = float(self.entry_angulo.get())
            desplazamiento = float(self.entry_desplazamiento.get())
            coef_friccion = float(self.entry_coef_friccion.get())
            masa = float(self.entry_masa.get())

            # Cálculo del trabajo
            peso, fuerza_normal, fuerza_friccion, trabajo_fuerza, trabajo_friccion, trabajo_total, incertidumbre = calcular_trabajo(fuerza, angulo, desplazamiento, coef_friccion, masa)
            
            resultado = (f"Peso: {peso:.2f} N\n"
                         f"Fuerza Normal: {fuerza_normal:.2f} N\n"
                         f"Fuerza de Fricción: {fuerza_friccion:.2f} N\n"
                         f"Trabajo de la Fuerza: {trabajo_fuerza:.2f} J\n"
                         f"Trabajo de la Fricción: {trabajo_friccion:.2f} J\n"
                         f"Trabajo Total: {trabajo_total:.2f} J\n"
                         f"Incertidumbre: ±{incertidumbre:.2f} J")

            self.resultado_trabajo.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    def calcular_energia_cinetica(self):
        try:
            masa = float(self.masa_ec_entry.get())
            velocidad = float(self.velocidad_entry.get())
            # Convertir unidades de masa
            masa_unidad = self.masa_ec_unidad.get()
            masa = convertir_unidades(masa, masa_unidad, 'kg')
            # Convertir unidades de velocidad
            velocidad_unidad = self.velocidad_unidad.get()
            velocidad = convertir_unidades(velocidad, velocidad_unidad, 'm/s')
            
            energia_cinetica = calcular_energia_cinetica(masa, velocidad)
            self.resultado_ec.config(text=f"Energía Cinética: {energia_cinetica:.2f} J")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    def calcular_energia_potencial_gravitatoria(self):
        try:
            masa = float(self.masa_epg_entry.get())
            altura = float(self.altura_entry.get())
            # Convertir unidades de masa
            masa_unidad = self.masa_epg_unidad.get()
            masa = convertir_unidades(masa, masa_unidad, 'kg')
            # Convertir unidades de altura
            altura_unidad = self.altura_unidad.get()
            altura = convertir_unidades(altura, altura_unidad, 'm')
            
            energia_potencial = calcular_energia_potencial_gravitatoria(masa, altura)
            self.resultado_epg.config(text=f"Energía Potencial Gravitatoria: {energia_potencial:.2f} J")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    def calcular_energia_potencial_elastica(self):
        try:
            constante = float(self.constante_entry.get())
            deformacion = float(self.deformacion_entry.get())
            
            energia_potencial = calcular_energia_potencial_elastica(constante, deformacion)
            self.resultado_epe.config(text=f"Energía Potencial Elástica: {energia_potencial:.2f} J")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    def mostrar_instrucciones(self):
        messagebox.showinfo("Instrucciones", "Use esta calculadora para calcular trabajo y energía. "
                                              "Ingrese los valores necesarios y presione 'Calcular'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraFisicaApp(root)
    root.mainloop()
