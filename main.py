import tkinter as tk
from tkinter import ttk
from ventana_adultos import VentanaAdultos
from ventana_ninos import VentanaNinos

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Historia Clínica")
        self.geometry("800x640")

        self.barra_opciones = ttk.Notebook(self)
        self.barra_opciones.grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky="w")

        self.vista_adultos = VentanaAdultos(self.barra_opciones)
        self.barra_opciones.add(self.vista_adultos, text="Adultos")

        self.vista_ninos = VentanaNinos(self.barra_opciones)
        self.barra_opciones.add(self.vista_ninos, text="Niños")

        self.bind("<<NotebookTabChanged>>", self.seleccionar_opcion)

        # Centrar la ventana en la pantalla
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

    def seleccionar_opcion(self, event):
        opcion = self.barra_opciones.tab(self.barra_opciones.select(), "text")
        if opcion == "Adultos":
            self.vista_adultos.cargar_formulario()
        elif opcion == "Niños":
            self.vista_ninos.cargar_formulario()

if __name__ == "__main__":
    app = App()
    app.mainloop()
