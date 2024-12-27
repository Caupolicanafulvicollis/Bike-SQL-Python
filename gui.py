import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
from matplotlib import pyplot as plt  # Importar matplotlib
from queries import (
    consult_orders_by_customer_and_period,
    list_most_requested_components,
    list_sold_bicycles_and_warranties,
    list_top_technicians,
    list_technicians_with_increase,
    get_component_usage_data,  # Nueva consulta
)

class CustomBikeApp:
    def __init__(self, db):
        self.db = db
        self.root = tk.Tk()
        self.root.title("Custom Bike Manager")
        self.setup_ui()

    def run(self):
        self.root.mainloop()

    def setup_ui(self):
        tk.Label(self.root, text="Custom Bike Manager", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Consultar Pedidos por Cliente", command=self.consult_orders).pack(pady=5)
        tk.Button(self.root, text="Componentes Más Solicitados", command=self.list_components).pack(pady=5)
        tk.Button(self.root, text="Bicicletas y Garantías", command=self.list_bicycles).pack(pady=5)
        tk.Button(self.root, text="Técnicos Destacados", command=self.top_technicians).pack(pady=5)
        tk.Button(self.root, text="Técnicos con Incremento", command=self.technicians_with_increase).pack(pady=5)
        tk.Button(self.root, text="Gráfico de Clientes Bike", command=self.show_component_usage_chart).pack(pady=5)

    def consult_orders(self):
        first_name = tkinter.simpledialog.askstring("Pedidos por Cliente", "Ingrese el Nombre del Cliente:")
        last_name = tkinter.simpledialog.askstring("Pedidos por Cliente", "Ingrese el Apellido del Cliente:")
        try:
            if first_name and last_name:
                results = consult_orders_by_customer_and_period(self.db, first_name.lower(), last_name.lower())
                if results:
                    fechas = [str(row[2]) for row in results]
                    fechas_legibles = "\n".join(fechas)
                    messagebox.showinfo("Pedidos por Cliente", f"Fechas de pedidos:\n{fechas_legibles}")
                else:
                    messagebox.showinfo("Pedidos por Cliente", "No se encontraron resultados.")
            else:
                messagebox.showwarning("Entrada requerida", "Debe ingresar un nombre y apellido.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def list_components(self):
        try:
            results = list_most_requested_components(self.db)
            if results:
                componentes = [row[0] for row in results]
                componentes_legibles = "\n".join(componentes)
                messagebox.showinfo("Componentes Más Solicitados", f"Componentes más solicitados:\n\n{componentes_legibles}")
            else:
                messagebox.showinfo("Componentes Más Solicitados", "No se encontraron resultados.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def list_bicycles(self):
        try:
            results = list_sold_bicycles_and_warranties(self.db)
            if results:
                tabla = "ID Pedido\tGarantía\tAños\n"
                tabla += "-" * 40 + "\n"
                for row in results:
                    tabla += f"{row[0]}\t{row[1]}\t{row[2]}\n"
                messagebox.showinfo("Bicicletas y Garantías", f"Bicicletas vendidas y garantías:\n\n{tabla}")
            else:
                messagebox.showinfo("Bicicletas y Garantías", "No se encontraron resultados.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def top_technicians(self):
        try:
            results = list_top_technicians(self.db)
            if results:
                tabla = "Nombre\tApellido\tTotal Pedidos\n"
                tabla += "-" * 40 + "\n"
                for row in results:
                    tabla += f"{row[0]}\t{row[1]}\t{row[2]}\n"
                messagebox.showinfo("Técnicos Destacados", f"Técnicos destacados:\n\n{tabla}")
            else:
                messagebox.showinfo("Técnicos Destacados", "No se encontraron resultados.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def technicians_with_increase(self):
        year1 = tkinter.simpledialog.askstring("Técnicos con Incremento", "Ingrese el Primer Año:")
        year2 = tkinter.simpledialog.askstring("Técnicos con Incremento", "Ingrese el Segundo Año:")
        try:
            if year1 and year2:
                results = list_technicians_with_increase(self.db, year1, year2)
                if results:
                    tabla = "Nombre\tApellido\n"
                    tabla += "-" * 30 + "\n"
                    for row in results:
                        tabla += f"{row[0]}\t{row[1]}\n"
                    messagebox.showinfo("Técnicos con Incremento", f"Técnicos con incremento:\n\n{tabla}")
                else:
                    messagebox.showinfo("Técnicos con Incremento", "No se encontraron resultados.")
            else:
                messagebox.showwarning("Entrada requerida", "Debe ingresar dos años válidos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_component_usage_chart(self):
        """
        Genera un gráfico de barras horizontal para mostrar el uso de componentes.
        """
        try:
            results = get_component_usage_data(self.db)
            if results:
                # Extraer datos para el gráfico
                tipos = [row[0] for row in results]  # Tipo de componente
                cantidades = [row[1] for row in results]  # Cantidad total
                
                # Crear el gráfico de barras horizontal
                plt.figure(figsize=(10, 6))
                bars = plt.barh(tipos, cantidades, color='skyblue')
                
                # Agregar etiquetas a las barras
                for bar, cantidad in zip(bars, cantidades):
                    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2, 
                             str(cantidad), va='center', fontsize=10)
                
                # Configuración del gráfico
                plt.title("Clientes Bike", fontsize=16)
                plt.xlabel("Número total de clientes", fontsize=12)
                plt.ylabel("Tipo de componente", fontsize=12)
                plt.tight_layout()
                
                # Mostrar el gráfico
                plt.show()
            else:
                messagebox.showinfo("Gráfico de Clientes Bike", "No se encontraron datos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el gráfico: {str(e)}")