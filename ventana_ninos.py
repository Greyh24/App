import tkinter as tk
from tkinter import ttk, filedialog
import sqlite3

class VentanaNinos(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

         # Crear un área de desplazamiento
        canvas = tk.Canvas(self)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Añadir una barra de desplazamiento vertical al área de desplazamiento
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un nuevo marco que será el contenedor de todas las secciones
        container = ttk.Frame(canvas)
        container.grid(row=0, column=0, sticky="nsew")

        # Configurar las columnas y fila del contenedor principal
        for i in range(6):  # Ajusta el número de columnas según sea necesario
            container.columnconfigure(i, weight=1)  # Configura cada columna para que se expanda igualmente
        container.rowconfigure(0, weight=1)  # Configura la fila para que se expanda

        # Sección: Datos
        datos_frame = ttk.LabelFrame(container, text="Datos")
        datos_frame.grid(row=0, column=0, padx=15, pady=15, sticky="w")

        ttk.Label(datos_frame, text="Nº de HC:").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_frame).grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(datos_frame, text="Médico:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(datos_frame, text="Nº de HC:").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_frame).grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(datos_frame, text="Médico:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(datos_frame, text="Especialidad:").grid(row=1, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_frame).grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(datos_frame, text="Fecha de atención:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_frame).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(datos_frame, text="Hora de atención:").grid(row=2, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_frame).grid(row=2, column=3, padx=5, pady=5)


        # Sección: Datos Generales
        datos_generales_frame = ttk.LabelFrame(container, text="Datos Generales")
        datos_generales_frame.grid(row=1, column=0, padx=15, pady=15, sticky="w")

        ttk.Label(datos_generales_frame, text="Pacientes:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(datos_generales_frame, text="DNI:").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=0, column=3, pady=5)

        ttk.Label(datos_generales_frame, text="Edad:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(datos_generales_frame, text="Fecha de nacimiento:").grid(row=1, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(datos_generales_frame, text="Grupo sanguíneo:").grid(row=1, column=4, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=1, column=5, padx=5, pady=5)

        ttk.Label(datos_generales_frame, text="Rh:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(datos_generales_frame, text="Sexo:").grid(row=2, column=2, sticky="e", pady=5)
        sexo_var = tk.StringVar()
        ttk.Radiobutton(datos_generales_frame, text="Masculino", variable=sexo_var, value="Masculino").grid(row=2, column=3)
        ttk.Radiobutton(datos_generales_frame, text="Femenino", variable=sexo_var, value="Femenino").grid(row=2, column=4)

        ttk.Label(datos_generales_frame, text="Dirección:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=3, column=1, columnspan=5, sticky="we", padx=5, pady=5)

        ttk.Label(datos_generales_frame, text="Ocupación:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_generales_frame).grid(row=4, column=1, columnspan=5, sticky="we", padx=5, pady=5)

        # Sección: Datos de los padres y/o apoderado
        datos_padres_frame = ttk.LabelFrame(container, text="Datos de los padres y/o apoderado")
        datos_padres_frame.grid(row=2, column=0, padx=20, pady=15, sticky="w")

        ttk.Label(datos_padres_frame, text="Nombre del padre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="DNI:").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="Teléfono:").grid(row=0, column=4, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=0, column=5, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="Nombre de la madre:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="DNI:").grid(row=1, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="Teléfono:").grid(row=1, column=4, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=1, column=5, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="Nombre del apoderado:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="DNI:").grid(row=2, column=2, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=2, column=3, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="Teléfono:").grid(row=2, column=4, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=2, column=5, padx=5, pady=5)

        ttk.Label(datos_padres_frame, text="Vínculo con el menor:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(datos_padres_frame).grid(row=3, column=1, columnspan=8, sticky="we", padx=5, pady=5)

        # Sección: Esquema de vacunación
        vacunacion_frame = ttk.LabelFrame(container, text="Esquema de vacunación")
        vacunacion_frame.grid(row=3, column=0, padx=20, pady=15, sticky="w")

        ttk.Checkbutton(vacunacion_frame, text="BCG").grid(row=0, column=0, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="HVB").grid(row=0, column=1, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="PENTAVALENTE").grid(row=0, column=2, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="ANTIPOLIO").grid(row=0, column=3, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="ANTINEUMOCOCICA").grid(row=0, column=4, padx=15, pady=15)

        ttk.Checkbutton(vacunacion_frame, text="DT").grid(row=1, column=0, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="SPR").grid(row=1, column=1, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="ROTAVIRUS").grid(row=1, column=2, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="INFLUENZA PED.").grid(row=1, column=3, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="VARICELA").grid(row=1, column=4, padx=15, pady=15)

        ttk.Checkbutton(vacunacion_frame, text="DPT").grid(row=2, column=0, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="APO").grid(row=2, column=1, padx=15, pady=15)
        ttk.Checkbutton(vacunacion_frame, text="ANTIAMARILICA").grid(row=2, column=2, padx=15, pady=15)

        ttk.Label(vacunacion_frame, text="OTROS:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(vacunacion_frame).grid(row=3, column=1, columnspan=5, sticky="we", padx=5, pady=5)

        # Sección: Antecedentes
        antecedentes_frame = ttk.LabelFrame(container, text="Antecedentes")
        antecedentes_frame.grid(row=4, column=0, padx=15, pady=15, sticky="w")

        ttk.Label(antecedentes_frame, text="Antecedentes personales:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(antecedentes_frame).grid(row=0, column=1, columnspan=5, sticky="we", padx=5, pady=5)

        ttk.Label(antecedentes_frame, text="Antecedentes familiares:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(antecedentes_frame).grid(row=1, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        ttk.Label(antecedentes_frame, text="RAW/Alergias:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(antecedentes_frame).grid(row=2, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        # Sección: Anamnesis
        anamnesis_frame = ttk.LabelFrame(container, text="Anamnesis")
        anamnesis_frame.grid(row=4, column=1, padx=15, pady=15, sticky="w")

        ttk.Label(anamnesis_frame, text="Motivo de consulta:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(anamnesis_frame).grid(row=0, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        ttk.Label(anamnesis_frame, text="Forma de inicio:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(anamnesis_frame).grid(row=1, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        ttk.Label(anamnesis_frame, text="Tiempo de enfermedad:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(anamnesis_frame).grid(row=2, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        ttk.Label(anamnesis_frame, text="Signos y síntomas principales:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(anamnesis_frame).grid(row=3, column=1, columnspan=4, sticky="we", padx=5, pady=5)

        # Sección: Examen físico
        examen_fisico_frame = ttk.LabelFrame(container, text="Examen físico")
        examen_fisico_frame.grid(row=6, column=0, padx=15, pady=15, sticky="w")

        ttk.Label(examen_fisico_frame, text="Frecuencia cardiaca:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(examen_fisico_frame).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(examen_fisico_frame, text="x min").grid(row=0, column=2, sticky="e", padx=5, pady=5)

        ttk.Label(examen_fisico_frame, text="Frecuencia respiratoria:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(examen_fisico_frame).grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(examen_fisico_frame, text="x min").grid(row=1, column=2, sticky="e", padx=5, pady=5)

        ttk.Label(examen_fisico_frame, text="Presión arterial:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(examen_fisico_frame).grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(examen_fisico_frame, text="mmHg").grid(row=2, column=2, sticky="e", padx=5, pady=5)

        ttk.Label(examen_fisico_frame, text="Tº:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(examen_fisico_frame).grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(examen_fisico_frame, text="ºC").grid(row=3, column=2, sticky="e", padx=5, pady=5)

        ttk.Label(examen_fisico_frame, text="Peso:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(examen_fisico_frame).grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(examen_fisico_frame, text="Talla:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(examen_fisico_frame).grid(row=5, column=1, padx=5, pady=5)

       # Sección: Treeview para mostrar los datos en forma de tabla
        columns = ["ID", "Nº de HC", "Médico", "Pacientes", "DNI", "Edad", "Fecha de Nacimiento", "Grupo Sanguíneo", "Rh", "Dirección"]
        self.tree = ttk.Treeview(container, columns=columns, show="headings", selectmode="browse")

        # Configurar las columnas
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  # Ajusta el ancho de las columnas según sea necesario

        # Agregar la tabla al área de desplazamiento
        self.tree.grid(row=7, column=0, padx=15, pady=15, sticky="nsew")

        # Configurar el área de desplazamiento para que se expanda con el tamaño del contenedor
        container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Asegurar que el contenedor se ajuste al tamaño del canvas
        canvas.create_window((0, 0), window=container, anchor="nw")

    def crear_tabla(self):
        cursor = self.conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ninos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hc_numero TEXT,
        medico TEXT,
        dni TEXT,
        especialidad TEXT,
        fecha_atencion TEXT,
        hora_atencion TEXT,
        pacientes TEXT,
        dni_paciente TEXT,
        sexo TEXT,
        edad TEXT,
        fecha_nacimiento TEXT,
        grupo_sanguineo TEXT,
        rh TEXT,
        direccion TEXT,
        ocupacion TEXT,
        nombre_padre TEXT,
        dni_padre TEXT,
        telefono_padre TEXT,
        nombre_madre TEXT,
        dni_madre TEXT,
        telefono_madre TEXT,
        nombre_apoderado TEXT,
        dni_apoderado TEXT,
        telefono_apoderado TEXT,
        vinculo_apoderado TEXT,
        vacuna_bcg TEXT,
        vacuna_hvb TEXT,
        vacuna_pentavalente TEXT,
        vacuna_antipolio TEXT,
        vacuna_antineumococica TEXT,
        vacuna_dt TEXT,
        vacuna_spr TEXT,
        vacuna_rotavirus TEXT,
        vacuna_influenza_ped TEXT,
        vacuna_varicela TEXT,
        vacuna_dpt TEXT,
        vacuna_apo TEXT,
        vacuna_antiamarilica TEXT,
        otros_vacunas TEXT,
        antecedentes_personales TEXT,
        antecedentes_familiares TEXT,
        raw_alergias TEXT,
        motivo_consulta TEXT,
        forma_inicio TEXT,
        tiempo_enfermedad TEXT,
        signos_sintomas TEXT,
        frecuencia_cardiaca TEXT,
        frecuencia_respiratoria TEXT,
        presion_arterial TEXT,
        temperatura TEXT,
        peso TEXT,
        talla TEXT
    )
''')

        self.conn.commit()

    def guardar_en_db(self, datos):
        cursor = self.conn.cursor()

        cursor.execute('''
            INSERT INTO ninos VALUES (NULL, ?, ?)
        ''', datos)

        self.conn.commit()

    def guardar(self):
        hc_numero = self.hc_numero_entry.get()
        medico = self.medico_entry.get()

        self.guardar_en_db((hc_numero, medico))

    def cargar_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ninos")
        filas = cursor.fetchall()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for fila in filas:
            self.tree.insert("", "end", values=fila)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Formulario de Niños")
    app = VentanaNinos(master=root)
    app.mainloop()
